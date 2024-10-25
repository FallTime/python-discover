from random import choice
from linkedlist import LinkedList
import numpy as np


class CpuInteligente:
    def __init__(self):
        self.database = [LinkedList() for _ in range(10)]
        self.board = [0 for _ in range(1, 10)]
        self.temp = []
        self.adv_fisrt_pos = 0
        self.count = 0

    def analisa_tabuleiro(self, tabuleiro):
        diferenca = np.where(np.array(self.board) != np.array(tabuleiro))[0]
        # se o tabuleiro se encontra no estado inicial, ou seja, cpu como primeiro jogador
        if len(diferenca) == 0:
            # ele retorna a posição do adversário, zero nesse caso, já que ninguem jogou ainda.
            return 0

        # caso alguem tenha jogado ele atualiza seu proprio tabuleiro e retorna a posição que mudou
        self.board[diferenca[0]] = tabuleiro[diferenca[0]]
        return int(diferenca[0] + 1)

    def jogada_aleatoria(self, turno):
        posicao = choice(range(1, 10))
        while self.board[posicao - 1] != 0:
            posicao = choice(range(1, 10))
        if turno:
            self.board[posicao - 1] = 1
        else:
            self.board[posicao - 1] = -1
        return posicao

    def registra_jogada(self, posicao, adv_pos):
        temp = [posicao, adv_pos]
        self.temp.append(temp)
        self.count += 1
        return posicao

    def escolher_jogada(self, adv_pos, turno):
        if self.count == 0:
            self.adv_fisrt_pos = adv_pos

        if self.database[self.adv_fisrt_pos].head:
            aux = self.database[self.adv_fisrt_pos].head

            if aux.qualidade < -3:
                return self.registra_jogada(self.jogada_aleatoria(turno), adv_pos)

            if self.count == 0:
                posicao = aux.posicao
                while self.board[posicao - 1] != 0:
                    if aux.next:
                        aux = aux.next
                    else:
                        return self.registra_jogada(self.jogada_aleatoria(turno), adv_pos)
                    posicao = aux.posicao
            else:
                for i in range(self.count):
                    if aux.child:
                        aux = aux.child
                    else:
                        return self.registra_jogada(self.jogada_aleatoria(turno), adv_pos)

                while aux.adv_pos != adv_pos:
                    if aux.next:
                        aux = aux.next
                    else:
                        return self.registra_jogada(self.jogada_aleatoria(turno), adv_pos)

                posicao = aux.posicao
                while self.board[posicao - 1] != 0:
                    while aux.adv_pos != adv_pos:
                        if aux.next:
                            aux = aux.next
                        else:
                            return self.registra_jogada(self.jogada_aleatoria(turno), adv_pos)

                    posicao = aux.posicao
        else:
            return self.registra_jogada(self.jogada_aleatoria(turno), adv_pos)

        return self.registra_jogada(posicao, adv_pos)

    def qualificar_jogadas(self, resultado_jogo):
        if self.adv_fisrt_pos != 0:
            resultado_jogo = -resultado_jogo

        for i in range(len(self.temp)):
            if i == 0:
                self.database[self.adv_fisrt_pos].append(self.temp[i][0], self.temp[i][1], resultado_jogo)
                no_pai = self.database[self.adv_fisrt_pos].buscar_no(self.temp[i][0], self.temp[i][1])
            else:
                self.database[self.adv_fisrt_pos].append_child(no_pai, self.temp[i][0], self.temp[i][1], resultado_jogo)
                no_pai = self.database[self.adv_fisrt_pos].buscar_no(self.temp[i][0], self.temp[i][1])


        print(self.temp)

        self.board = [0 for _ in range(1, 10)]
        self.count = 0
        self.temp = []
        for i in range(10):
            self.database[i].print_list()

