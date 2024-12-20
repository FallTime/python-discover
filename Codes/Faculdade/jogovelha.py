from random import choice
from cpuinteligente import CpuInteligente
import csv
import cpucampeao

def cpu_inteligente():
    if jogador_turno:
        return aix.escolher_jogada(tabuleiro[1:10])
    else:
        return aio.escolher_jogada(tabuleiro[1:10])

def cpu(escolha):
    match escolha:
        case 1:
            return choice(range(1, 10))
        case 2:
            return cpucampeao.cpu_campeao(jogador_turno,tabuleiro)
        case 3:
            return cpu_inteligente()

def selecionar_cpu(opcao):
    global cpu_escolha
    match opcao:
        case 1:
            cpu_escolha = 1
            return False
        case 2:
            cpu_escolha = 2
            return False
        case 3:
            cpu_escolha = 3
            return False
        case _:
            print("Opção inválida!")
    return True

def numero_jogos(quantidade):
    global partidas
    if quantidade < 1:
        print("número inválido de jogos")
        return True
    partidas = quantidade
    return False

def resultado_jogo():
    global jogador_vencedor
    if tabuleiro[0] == 9 and jogador_vencedor == 0:
        #print("\nVelha")
        return 0
    elif jogador_vencedor == 1:
        #print("\nX venceu")
        return 1
    else:
        #print("\nO Venceu")
        return -1

def relatorio_partida(tabuleiro, num_partida, resultado):
    global contador_vitoria1, contador_vitoria2, contador_empate
    add = []
    if resultado == 0:
        contador_empate += 1
    elif resultado == 1:
        contador_vitoria1 += 1
        ultima_derrota2 = num_partida
    else:
        contador_vitoria2 += 1
        ultima_derrota1 = num_partida

    add.append(num_partida)
    add.append(tabuleiro.copy())
    add.append(resultado)
    add.append(contador_vitoria1)
    add.append(contador_empate)
    add.append(contador_vitoria2)
    return add

def zerar_tabuleiro():
    zerado = [0 for i in range(10)]
    return zerado.copy()

def main(opcao):
    conta = 0
    global tabuleiro, jogador_turno, jogador_vencedor

    match opcao:
        # player vs player 
        case 1:
            while numero_jogos(int(input("Insira o número de jogos:"))):
                pass
            while conta < partidas:
                while verificar_vitoria(tabuleiro) and tabuleiro[0] < 9:
                    exibirtab(tabuleiro)
                    if jogada(tabuleiro):
                        tabuleiro[0] += 1

                conta += 1
                exibirtab(tabuleiro)
                relatorio.append(relatorio_partida(tabuleiro, conta, resultado_jogo()))
                tabuleiro = zerar_tabuleiro()
                jogador_turno = True
                jogador_vencedor = 0

            return False
        # player vs cpu
        case 2:
            while numero_jogos(int(input("Insira o número de jogos:"))):
                pass
            print("\nSeleção de CPU:\n1 - Aleatório\n2 - Campeão\n3 - Inteligente")
            while selecionar_cpu(int(input("Insira a opção:"))):
                pass
            while conta < partidas:
                exibirtab(tabuleiro)
                while verificar_vitoria(tabuleiro) and tabuleiro[0] < 9:

                    if jogador_turno:
                        if jogada(tabuleiro):
                            exibirtab(tabuleiro)
                            tabuleiro[0] += 1
                    else:
                        if jogada_cpu(tabuleiro, cpu(cpu_escolha)):
                            exibirtab(tabuleiro)
                            tabuleiro[0] += 1

                conta += 1
                exibirtab(tabuleiro)
                if cpu_escolha == 3:
                    aio.atualizar_ranks(resultado_jogo(), 2)
                relatorio.append(relatorio_partida(tabuleiro, conta, resultado_jogo()))
                tabuleiro = zerar_tabuleiro()
                jogador_turno = True
                jogador_vencedor = 0

            return False
        # cpu vs cpu
        case 3:
            while numero_jogos(int(input("Insira o número de jogos:"))):
                pass
            print("\nSeleção da CPU:\n1 - Aleatório\n2 - Campeão\n3 - Inteligente")
            while selecionar_cpu(int(input("Insira a opção:"))):
                pass
            cpu_escolha1 = cpu_escolha
            print(cpu_escolha1)
            print("\nSeleção da CPU:\n1 - Aleatório\n2 - Campeão\n3 - Inteligente")
            while selecionar_cpu(int(input("Insira a opção:"))):
                pass
            cpu_escolha2 = cpu_escolha
            print(cpu_escolha2)

            while conta < partidas:
                #exibirtab(tabuleiro)
                while verificar_vitoria(tabuleiro) and tabuleiro[0] < 9:
                    if jogador_turno:
                        if jogada_cpu(tabuleiro, cpu(cpu_escolha1)):
                            #exibirtab(tabuleiro)
                            tabuleiro[0] += 1
                    else:
                        if jogada_cpu(tabuleiro, cpu(cpu_escolha2)):
                            #exibirtab(tabuleiro)
                            tabuleiro[0] += 1

                conta += 1
                if cpu_escolha1 == 3:
                    aix.atualizar_ranks(resultado_jogo(), 1)
                if cpu_escolha2 == 3:
                    aio.atualizar_ranks(resultado_jogo(), 2)
                relatorio.append(relatorio_partida(tabuleiro, conta, resultado_jogo()))
                tabuleiro = zerar_tabuleiro()
                jogador_turno = True
                jogador_vencedor = 0

            return False
        # default case
        case _:
            print("Opção inválida!")
    return True

def exibirtab(tabuleiro):
    print("\n")
    for i in range(1, 10):
        if tabuleiro[i] == 0:
            print("   ", end='')
        elif tabuleiro[i] == 1:
            print(" X ", end='')
        else:
            print(" O ", end='')

        if i % 3 == 0 and i < 9:
            print("\n-----------")
        else:
            if i != 9:
                print("|", end='')

def jogada(tabuleiro):
    global jogador_turno
    casa = int(input(
        "\nInsira a posição:"))

    if casa < 0 or casa > 9:
        print("\nPosição invalida")
        return False

    ehdisponivel = tabuleiro[casa] == 0

    if ehdisponivel:
        if jogador_turno:
            tabuleiro[casa] = 1
            jogador_turno = False
        else:
            tabuleiro[casa] = -1
            jogador_turno = True
        return True
    else:
        print("\nCasa indisponível")
        return False

def jogada_cpu(tabuleiro, casa):
    global jogador_turno

    ehdisponivel = tabuleiro[casa] == 0

    if ehdisponivel:
        if jogador_turno:
            tabuleiro[casa] = 1
            jogador_turno = False
        else:
            tabuleiro[casa] = -1
            jogador_turno = True
        return True
    else:
        return False

def verificar_vitoria(tabuleiro):
    global jogador_vencedor
    combinacoes_vencedoras = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Linhas
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Colunas
        [1, 5, 9], [3, 5, 7]  # Diagonais
    ]

    for combinacao in combinacoes_vencedoras:
        soma = sum(tabuleiro[i] for i in combinacao)
        if soma == 3:
            jogador_vencedor = 1
            return False
        elif soma == -3:
            jogador_vencedor = -1
            return False

    return True

aix = CpuInteligente('databaseX.csv')
aio = CpuInteligente('databaseO.csv')
relatorio = []
partidas = 0
jogador_turno = True
jogador_vencedor = 0
cpu_escolha = 0
tabuleiro = zerar_tabuleiro()
contador_vitoria1 = 0
contador_vitoria2 = 0
contador_empate = 0

print("Modos de Jogo:\n1 - Jogador VS Jogador\n2 - Jogador VS CPU\n3 - CPU VS CPU")
while main(int(input("Insira a opção:"))):
    pass

aix.atualizar_jogada_no_csv()
aio.atualizar_jogada_no_csv()
with open('relatorio.csv', mode='w', newline='') as file:
    campos_header = [
        'Numero da Partida', 'Tabuleiro', 'Resultado',
        'Vitoria do Primeiro', 'Velha', 'Vitoria do Segundo'
    ]
    writer = csv.DictWriter(file, fieldnames=campos_header)

    writer.writeheader()
    for i in range(len(relatorio)):
        writer.writerow({
            'Numero da Partida': relatorio[i][0],
            'Tabuleiro': relatorio[i][1],
            'Resultado': relatorio[i][2],
            'Vitoria do Primeiro': relatorio[i][3],
            'Velha': relatorio[i][4],
            'Vitoria do Segundo': relatorio[i][5],
        })
