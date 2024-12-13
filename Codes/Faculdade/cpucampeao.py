def cpu_campeao(jogador_turno, tabuleiro):
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
