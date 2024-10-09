from random import choice


def cpu_aleatoria():
    return choice(range(1, 10))


def cpu_campeao():
    global jogador_turno
    combinacoes_vencedoras = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Linhas
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Colunas
        [1, 5, 9], [3, 5, 7]  # Diagonais
    ]
    grande_diagonal = [[1, 9], [3, 7]]
    pequena_diagonal = [[2, 4], [2, 6], [8, 4], [8, 6]]
    golpe_horizontal = [[6, 1], [6, 7], [4, 3], [4, 9]]
    golpe_vertical = [[2, 7], [2, 9], [8, 1], [8, 3]]
    resposta = [1, 3, 7, 9]
    resposta_h = [2, 8, 2, 8]
    resposta_v = [4, 6, 4, 6]

    # jogando como X
    if jogador_turno:
        if tabuleiro[0] >= 3:
            # prioridade em vitoria
            for combinacao in combinacoes_vencedoras:
                soma = sum(tabuleiro[i] for i in combinacao)
                if soma == 2:
                    for i in combinacao:
                        if tabuleiro[i] == 0:
                            return int(i)
            # caso não tenha vitoria, visa os bloqueios
            for combinacao in combinacoes_vencedoras:
                soma = sum(tabuleiro[i] for i in combinacao)
                if soma == -2:
                    for i in combinacao:
                        if tabuleiro[i] == 0:
                            return int(i)

        if tabuleiro[1] == 0:
            return 1
        if tabuleiro[9] == 0:
            return 9
        if tabuleiro[3] == 0:
            return 3
        if tabuleiro[7] == 0:
            return 7

    # jogando como O
    else:
        if tabuleiro[0] >= 3:
            # prioridade em vitoria
            for combinacao in combinacoes_vencedoras:
                soma = sum(tabuleiro[i] for i in combinacao)
                if soma == -2:
                    for i in combinacao:
                        if tabuleiro[i] == 0:
                            return int(i)

            # caso não tenha vitoria, visa os bloqueios
            for combinacao in combinacoes_vencedoras:
                soma = sum(tabuleiro[i] for i in combinacao)
                if soma == 2:
                    for i in combinacao:
                        if tabuleiro[i] == 0:
                            return int(i)

            for combinacao in pequena_diagonal:
                soma = sum(tabuleiro[i] for i in combinacao)
                if soma == 2:
                        if tabuleiro[resposta[pequena_diagonal.index(combinacao)]] == 0:
                            return resposta[pequena_diagonal.index(combinacao)]

            for combinacao in golpe_horizontal:
                soma = sum(tabuleiro[i] for i in combinacao)
                if soma == 2:
                        if tabuleiro[resposta_h[golpe_horizontal.index(combinacao)]] == 0:
                            return resposta_h[golpe_horizontal.index(combinacao)]

            for combinacao in golpe_vertical:
                soma = sum(tabuleiro[i] for i in combinacao)
                if soma == 2:
                        if tabuleiro[resposta_v[golpe_vertical.index(combinacao)]] == 0:
                            return resposta_v[golpe_vertical.index(combinacao)]
                    
            for combinacao in grande_diagonal:
                soma = sum(tabuleiro[i] for i in combinacao)
                if soma == 2:
                    if tabuleiro[4] == 0:
                        return 4

        if tabuleiro[5] == 0:
            return 5
        if tabuleiro[1] == 0:
            return 1
        if tabuleiro[9] == 0:
            return 9
        if tabuleiro[3] == 0:
            return 3
        if tabuleiro[7] == 0:
            return 7



def cpu(escolha):
    match escolha:
        case 1:
            return cpu_aleatoria()
        case 2:
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
        print("\nVelha")
        return 0
    elif jogador_vencedor == 1:
        print("\nX venceu")
        return 1
    else:
        print("\nO Venceu")
        return -1


def relatorio_partida(tabuleiro, num_partida, resultado):
    global contador_vitoria1, contador_vitoria2, contador_empate
    add = []
    if resultado == 0:
        contador_empate += 1
    elif resultado == 1:
        contador_vitoria1 += 1
    else:
        contador_vitoria2 += 1

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
            print("\nSeleção de CPU:\n1 - Aleatório\n2 - Campeão")
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
                relatorio.append(relatorio_partida(tabuleiro, conta, resultado_jogo()))
                tabuleiro = zerar_tabuleiro()
                jogador_turno = True
                jogador_vencedor = 0

            return False
        # cpu vs cpu
        case 3:
            while numero_jogos(int(input("Insira o número de jogos:"))):
                pass
            print("\nSeleção da CPU:\n1 - Aleatório\n2 - Campeão")
            while selecionar_cpu(int(input("Insira a opção:"))):
                pass
            cpu_escolha1 = cpu_escolha
            print(cpu_escolha1)
            print("\nSeleção da CPU:\n1 - Aleatório\n2 - Campeão")
            while selecionar_cpu(int(input("Insira a opção:"))):
                pass
            cpu_escolha2 = cpu_escolha
            print(cpu_escolha2)

            while conta < partidas:
                exibirtab(tabuleiro)
                while verificar_vitoria(tabuleiro) and tabuleiro[0] < 9:
                    if jogador_turno:
                        if jogada_cpu(tabuleiro, cpu(cpu_escolha1)):
                            exibirtab(tabuleiro)
                            tabuleiro[0] += 1
                    else:
                        if jogada_cpu(tabuleiro, cpu(cpu_escolha2)):
                            exibirtab(tabuleiro)
                            tabuleiro[0] += 1

                conta += 1
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

print(relatorio)
