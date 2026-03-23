from playwright.sync_api import sync_playwright
import time

def wait(page):
    page.wait_for_load_state("networkidle")

# Lê credenciais do arquivo
with open("credenciais.txt", "r") as f:
    usuario = f.readline().strip()
    senha = f.readline().strip()

# Lê modelo do chamado
with open("modelo.txt", "r", encoding="utf-8") as f:
    linhas = f.readlines()
    titulo = linhas[0].strip()              # primeira linha = título
    descricao = "".join(linhas[1:]).strip() # restante = descrição

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # headless=False abre a janela
    page = browser.new_page()

    # Página de login
    page.goto("https://glpi.rj.def.br/front/ticket.form.php")
    page.fill("#login_name", usuario)
    page.fill("#login_password", senha)
    page.click("button[name='submit']")
    wait(page)

    # Título do chamado
    page.fill("input[name='name']", titulo)

    # Descrição do chamado
    frame = page.frame_locator("iframe[id^='content_']")
    frame.locator("body#tinymce").fill(descricao)

    # Tipo do chamado
    page.click("span[title='Incidente']")
    page.locator(".select2-results__option", has_text="Requisição").click()
    wait(page)

    # Alterar categoria 
    page.locator("span.select2-selection__rendered", has_text="-----").nth(0).click()
    page.locator("input.select2-search__field").last.fill("Recolhimento")
    page.wait_for_selector("li.select2-results__option[title*='Recolhimento de aparelho']")
    page.locator("li.select2-results__option[title*='Recolhimento de aparelho']").click()

    # Atribuir localização (por hora não sei como fazer)
    
    print("Chamado preenchido. Insira a localização")
    input()
    time.sleep(2)
    browser.close()