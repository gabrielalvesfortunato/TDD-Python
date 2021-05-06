from src.leilao.excecoes import *

class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor   = valor


class Usuario:

    def __init__(self, nome, carteira=0):
        self.__carteira = carteira
        self.__nome     = nome

    @property
    def carteira(self):
        return self.__carteira

    @property
    def nome(self):
        return self.__nome

    def _valor_e_valido(self, valor):
        return self.__carteira >= valor

    def depositar_valor_carteira(self, valor):
        self.__carteira += valor

    def retirar_valor_carteira(self, valor):
        if self._valor_e_valido(valor):
            self.__carteira -= valor
        else:
            raise ValorInsuficiente("Valor em carteira insuficiente para retirada")

    def propor_lance(self, leilao, valor):
        if self._valor_e_valido(valor):
            lance = Lance(self, valor)
            leilao.propor_lance(lance)
            self.retirar_valor_carteira(self, valor)
        else:
            raise LanceInvalido("Não pode propor um lance com o valor maior que o valor em carteira")


class Leilao:

    def __init__(self, descricao):
        self.descricao   = descricao
        self.maior_lance = 0.0
        self.menor_lance = 0.0
        self.__lances = []

    @property
    def lances(self):
        return self.__lances[:]  # copia rasa da lista

    def _tem_lances(self):
        return self.__lances

    def _usuarios_diferentes(self, lance):
        if self.__lances[-1].usuario != lance.usuario:
            return True
        raise LanceInvalido("O mesmo usuário não pode dar dois lances seguidos")

    def _valor_maior_que_lance_anterior(self, lance):
        if lance.valor > self.__lances[-1].valor:
            return True
        raise LanceInvalido("O valor do lance tem que ser maior que o lance anterior")

    def _lance_e_valido(self, lance):
        return not self._tem_lances() or (self._usuarios_diferentes(lance) and
                                          self._valor_maior_que_lance_anterior(lance))

    def propor_lance(self, lance: Lance):
        if self._lance_e_valido(lance):
            if not self._tem_lances():
                self.menor_lance = lance.valor

            self.maior_lance = lance.valor
            self.__lances.append(lance)
