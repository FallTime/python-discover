from random import choice


def cpu_aleatoria():
    return choice(range(0, 10))


def cpu_inexperiente():
    global contador
    contador += 1
    return contador


def cpu_campeao():
    pass


def cpu(escolha):
    match escolha:
        case 1:
            return cpu_inexperiente()
        case 2:
            return cpu_aleatoria()
        case 3:
            return cpu_campeao()


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
    text = "Velha" if tabuleiro[0] == 9 else "X venceu" if jogador_vencedor == 1 else "O Venceu"
    return text


def zerar_tabuleiro():
    zerado = [0 for i in range(10)]
    return zerado.copy()


def main(opcao):
    conta = 0
    global tabuleiro, contador
    while numero_jogos(int(input("Insira o número de jogos:"))):
        pass

    match opcao:
        # player vs player 
        case 1:
            while conta < partidas:
                while estado(tabuleiro) and tabuleiro[0] < 9:
                    exibirtab(tabuleiro)
                    if jogada(tabuleiro):
                        tabuleiro[0] += 1

                conta += 1
                exibirtab(tabuleiro)
                print('\n\n', resultado_jogo())
                relatorio.append(resultado_jogo())
                tabuleiro = zerar_tabuleiro()
                if cpu_escolha == 1:
                    contador = 0

            return False
        # player vs cpu
        case 2:

            print("\nSeleção de CPU:\n1 - Inexperiente\n2 - Aleatório\n3 - Campeão")
            while selecionar_cpu(int(input("Insira a opção:"))):
                pass
            while conta < partidas:
                while estado(tabuleiro) and tabuleiro[0] < 9:
                    exibirtab(tabuleiro)
                    if jogador_turno:
                        if jogada(tabuleiro):
                            tabuleiro[0] += 1
                    else:
                        if jogada_cpu(tabuleiro, cpu(cpu_escolha)):
                            tabuleiro[0] += 1

                conta += 1
                exibirtab(tabuleiro)
                print('\n\n', resultado_jogo())
                relatorio.append(resultado_jogo())
                tabuleiro = zerar_tabuleiro()

            return False
        # cpu vs cpu
        case 3:
            print("\nSeleção da CPU:\n1 - Inexperiente\n2 - Aleatório\n3 - Campeão")
            while selecionar_cpu(int(input("Insira a opção:"))):
                pass
            while conta < partidas:
                while estado(tabuleiro) and tabuleiro[0] < 9:
                    exibirtab(tabuleiro)
                    if jogada_cpu(tabuleiro, cpu(cpu_escolha)):
                        tabuleiro[0] += 1

                conta += 1
                exibirtab(tabuleiro)
                print('\n\n', resultado_jogo())
                relatorio.append(resultado_jogo())
                tabuleiro = zerar_tabuleiro()
                if cpu_escolha == 1:
                    contador = 0

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
        print("\nCasa indisponível")
        return False


def estado(tabuleiro):
    # victory cases 123,147,159,528,546,537,987,963
    global jogador_vencedor

    if tabuleiro[1] + tabuleiro[2] + tabuleiro[3] == 3 or \
            tabuleiro[1] + tabuleiro[4] + tabuleiro[7] == 3 or \
            tabuleiro[1] + tabuleiro[5] + tabuleiro[9] == 3 or \
            tabuleiro[5] + tabuleiro[2] + tabuleiro[8] == 3 or \
            tabuleiro[5] + tabuleiro[4] + tabuleiro[6] == 3 or \
            tabuleiro[5] + tabuleiro[3] + tabuleiro[7] == 3 or \
            tabuleiro[9] + tabuleiro[8] + tabuleiro[7] == 3 or \
            tabuleiro[9] + tabuleiro[6] + tabuleiro[3] == 3:
        jogador_vencedor = 1
        return False

    elif tabuleiro[1] + tabuleiro[2] + tabuleiro[3] == -3 or \
            tabuleiro[1] + tabuleiro[4] + tabuleiro[7] == -3 or \
            tabuleiro[1] + tabuleiro[5] + tabuleiro[9] == -3 or \
            tabuleiro[5] + tabuleiro[2] + tabuleiro[8] == -3 or \
            tabuleiro[5] + tabuleiro[4] + tabuleiro[6] == -3 or \
            tabuleiro[5] + tabuleiro[3] + tabuleiro[7] == -3 or \
            tabuleiro[9] + tabuleiro[8] + tabuleiro[7] == -3 or \
            tabuleiro[9] + tabuleiro[6] + tabuleiro[3] == -3:
        jogador_vencedor = -1
        return False

    return True


relatorio = []
partidas = 0
contador = 0
jogador_turno = True
jogador_vencedor = 0
cpu_escolha = 0
tabuleiro = zerar_tabuleiro()

print("Modos de Jogo:\n1 - Jogador VS Jogador\n2 - Jogador VS CPU\n3 - CPU VS CPU")
while main(int(input("Insira a opção:"))):
    pass

print(relatorio)
