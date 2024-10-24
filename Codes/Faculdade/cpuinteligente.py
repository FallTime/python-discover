from random import choice
from linkedlist import LinkedList
import numpy as np


class CpuInteligente:
    def __init__(self):
        self.database = [LinkedList() for _ in range(10)]
        self.board = [0 for _ in range(1, 10)]
        self.temp = []
        self.adv_fisrt_pos
        self.count = 0

    def analisa_tabuleiro(self, tabuleiro):
        diferenca = np.where(np.array(self.board) != np.array(tabuleiro))[0]
        # se o tabuleiro se encontra no estado inicial, ou seja, cpu como primeiro jogador
        if len(diferenca) == 0:
            # ele retorna a posição do adversário, zero nesse caso, já que ninguem jogou ainda.
            return 0

        # caso alguem tenha jogado ele atualiza seu proprio tabuleiro e retorna a posição que mudou
        self.board[diferenca[0]] = tabuleiro[diferenca[0]]
        return diferenca[0] + 1

    def escolher_jogada(self, adv_pos, turno):
        if self.count == 0:
            self.adv_fisrt_pos = adv_pos
        if self.database[self.adv_fisrt_pos].head is None:
            posicao = self.jogada_aleatoria(turno)
        else:
            aux = self.database[self.adv_fisrt_pos].head
            posicao = aux.posicao
            while self.board[posicao-1] != 0:
                aux = aux.next
                posicao = aux.posicao

        self.temp.append([adv_pos, posicao])
        return posicao

    def jogada_aleatoria(self, turno):
        posicao = choice(range(1, 10))
        while self.board[posicao - 1] != 0:
            posicao = choice(range(1, 10))
        if turno:
            self.board[posicao - 1] = 1
        else:
            self.board[posicao - 1] = -1
        return posicao
    def qualificar_jogadas(self, resultado_jogo):
        pass



