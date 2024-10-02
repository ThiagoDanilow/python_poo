import pickle
from typing import List
from common import *
from datetime import date

class Urna:
    mesario : Pessoa
    __secao : int
    __zona : int
    __eleitores_presentes : List[Eleitor] = []
    __votos = {} #dicionario chave = numero do candidato, valor é a quantidade de votos

    def __init__(self, mesario : Pessoa, secao : int, zona : int,
                 candidatos : List[Candidato], eleitores : List[Eleitor]):
        self.mesario = mesario
        self.__secao = secao
        self.__zona = zona
        self.__nome_arquivo = f'{self.__zona}_{self.__secao}.pkl'
        self.__candidatos = candidatos
        self.__eleitores = []
        for eleitor in eleitores:
            if eleitor.zona == zona and eleitor.secao == secao:
                self.__eleitores.append(eleitor)

        for candidato in self.__candidatos:
            self.__votos[candidato.get_numero()] = 0
        self.__votos['BRANCO'] = 0
        self.__votos['NULO'] = 0

        with open(self.__nome_arquivo, 'wb') as arquivo:
            pickle.dump(self.__votos, arquivo)

    def get_eleitor(self, titulo : int):
        for eleitor in self.__eleitores:
            if eleitor.get_titulo() == titulo:
                return eleitor
        return False

    def registrar_voto(self, eleitor : Eleitor, n_cand : str):
        self.__eleitores_presentes.append(eleitor)
        if n_cand == 'branco' or 'BRANCO' or 'Branco' or '0':
            self.__votos['BRANCO'] += 1
        elif int(n_cand) in self.__votos:
            self.__votos[n_cand] += 1
        else:
            self.__votos['NULO'] += 1

        with open(self.__nome_arquivo, 'wb') as arquivo:
            pickle.dump(self.__votos, arquivo)

    def zeresima(self):
        with ('zeresima_'+ self.__nome_arquivo,'wb') as arquivo:
            pickle_dump(self.__votos,arquivo)
        return

    def encerrar(self):
        with ('final_' + self.__nome_arquivo, 'wb') as arquivo:
            pickle_dump(self.__nome_arquivo)
        return
    def __str__(self):
        data_atual = date.today()
        info = (f'Data atual: {data_atual.ctime()}\n'
                f'Urna da seção {self.__secao}, zona {self.__zona}\n'
                f'Mesario {self.mesario}')

        for k,v in self.__votos.items():
            info += f'Candidato {k} = {v} Votos\n'
        return info


