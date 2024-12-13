import csv
import matplotlib.pyplot as plt

def carregar_dados(filename):
    dados = []
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            dados.append({
                'Numero da Partida': int(row['Numero da Partida']),
                'Tabuleiro': row['Tabuleiro'],
                'Resultado': int(row['Resultado']),
                'Vitoria do Primeiro': int(row['Vitoria do Primeiro']),
                'Velha': int(row['Velha']),
                'Vitoria do Segundo': int(row['Vitoria do Segundo']),
            })
    return dados

def gerar_grafico_vitorias(dados):
    partidas = [d['Numero da Partida'] for d in dados]
    vitorias1 = [d['Vitoria do Primeiro'] for d in dados]
    vitorias2 = [d['Vitoria do Segundo'] for d in dados]
    empates = [d['Velha'] for d in dados]

    plt.plot(partidas, vitorias1, label='Vitórias do Primeiro')
    plt.plot(partidas, vitorias2, label='Vitórias do Segundo')
    plt.plot(partidas, empates, label='Empates')

    plt.xlabel('Número da Partida')
    plt.ylabel('Quantidade')
    plt.title('Desempenho ao Longo das Partidas')
    plt.legend()
    plt.grid(True)
    plt.show()

def calcular_evolucao(dados):
    evolucao = []
    acumulado = 0

    for d in dados:
        if d['Resultado'] == 1:
            acumulado += 1
        elif d['Resultado'] == -1:
            acumulado -= 1
        evolucao.append(acumulado)

    return evolucao

def gerar_grafico_evolucao(dados):
    partidas = [d['Numero da Partida'] for d in dados]
    evolucao = calcular_evolucao(dados)

    plt.plot(partidas, evolucao, label='Evolução do Desempenho')

    plt.xlabel('Número da Partida')
    plt.ylabel('Desempenho Acumulado')
    plt.title('Evolução do Desempenho dos Jogadores')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    dados = carregar_dados('relatorio.csv')
    gerar_grafico_vitorias(dados)
    gerar_grafico_evolucao(dados)
