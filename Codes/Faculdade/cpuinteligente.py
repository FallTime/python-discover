from random import choice
import csv


class CpuInteligente:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.database = self.carregar_jogadas()
        self.jogadas_partida = []

    def carregar_jogadas(self):
        jogadas = []
        try:
            with open(self.csv_file, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == 'rank':
                        continue
                    jogadas.append({
                        'rank': int(row[0]),
                        'tabuleiro': list(map(int, row[1].strip('[]').split(', '))),
                        'posicao': int(row[2])
                    })
        except FileNotFoundError:
            pass
        return jogadas

    def salvar_jogada(self, rank, tabuleiro, posicao):
        for jogada in self.database:
            if jogada['tabuleiro'] == tabuleiro and jogada['posicao'] == posicao:
                jogada['rank'] = rank
                return  # Não adiciona jogada duplicada
        self.database.append({'rank': rank, 'tabuleiro': tabuleiro, 'posicao': posicao})

    def escolher_jogada(self, tabuleiro):
        for jogada in self.database:
            if jogada['tabuleiro'] == tabuleiro and jogada['rank'] > 0:
                self.jogadas_partida.append(jogada)
                return jogada['posicao']
        posicoes_disponiveis = [i for i in range(1, 10) if tabuleiro[i-1] == 0]
        jogada_aleatoria = choice(posicoes_disponiveis)
        self.salvar_jogada(0, tabuleiro, jogada_aleatoria)
        self.jogadas_partida.append({'rank': 0, 'tabuleiro': tabuleiro, 'posicao': jogada_aleatoria})
        return jogada_aleatoria

    def atualizar_ranks(self, resultado, jogador):
        for jogada in self.jogadas_partida:
            if jogador == 2:
                if resultado == -1:
                    jogada['rank'] += 1
                elif resultado == 1:
                    jogada['rank'] -= 1
            else:
                if resultado == 1:
                    jogada['rank'] += 1
                elif resultado == -1:
                    jogada['rank'] -= 1
            self.salvar_jogada(jogada['rank'], jogada['tabuleiro'], jogada['posicao'])
        self.atualizar_jogada_no_csv()
        self.jogadas_partida = []

    def atualizar_jogada_no_csv(self):
        with open(self.csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['rank', 'tabuleiro', 'posicao'])
            for jogada in sorted(self.database, key=lambda x: x['rank'], reverse=True):
                writer.writerow([jogada['rank'], jogada['tabuleiro'], jogada['posicao']])
