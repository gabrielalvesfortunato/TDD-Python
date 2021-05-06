from unittest import TestCase
from src.leilao.dominio import *
from src.leilao.excecoes import *


# Classe responsável por testar a classe avaliador em dominio.py
class TestLeilao(TestCase):

    # Criação do cenário de testes
    def setUp(self):
        self.usuario_gabriel = Usuario("Gabriel")
        self.lance_gabriel = Lance(self.usuario_gabriel, 100.00)
        self.leilao = Leilao("Celular")

    def test_deve_retornar_o_maior_e_o_menor_lance_quando_adicionados_em_ordem_crescente(self):
        usuario_miguel = Usuario("Miguel")
        lance_miguel = Lance(usuario_miguel, 200.00)
        self.leilao.propor_lance(self.lance_gabriel)  # 100.00
        self.leilao.propor_lance(lance_miguel)  # 200.00
        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0
        # O .assertEqual testa se o valor da variavel e igual ao valor esperado para a variavel
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_nao_deve_permitir_propor_um_lance_quando_o_lance_atual_for_menor_que_o_anterior(self):
        with self.assertRaises(LanceInvalido):
            usuario_miguel = Usuario("Miguel")
            lance_miguel = Lance(usuario_miguel, 200.00)
            self.leilao.propor_lance(lance_miguel)  # 200.00
            self.leilao.propor_lance(self.lance_gabriel)  # 100.00

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):
        self.leilao.propor_lance(self.lance_gabriel)
        lance_unico = 100.0
        # O .assertEqual testa se o valor da variavel e igual ao valor esperado para a variavel
        self.assertEqual(lance_unico, self.leilao.menor_lance)
        self.assertEqual(lance_unico, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_lance_quando_o_leilao_tiver_tres_lances(self):
        usuario_rafael = Usuario("Rafael")
        lance_rafael = Lance(usuario_rafael, 290.00)
        usuario_miguel = Usuario("Miguel")
        lance_miguel = Lance(usuario_miguel, 200.00)
        self.leilao.propor_lance(self.lance_gabriel)
        self.leilao.propor_lance(lance_miguel)
        self.leilao.propor_lance(lance_rafael)
        menor_valor_esperado = 100.00
        maior_valor_esperado = 290.00
        # O .assertEqual testa se o valor da variavel e igual ao valor esperado para a variavel
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_permitir_propor_um_lance_quando_o_leilao_nao_tiver_lances(self):
        self.leilao.propor_lance(self.lance_gabriel)
        quantidade_de_lances_recebido = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances_recebido)

    def test_deve_permitir_propor_um_lance_quando_o_ultimo_usuario_for_diferente_do_atual(self):
        novo_usuario = Usuario("Miguel")
        novo_lance = Lance(novo_usuario, 200.00)
        self.leilao.propor_lance(self.lance_gabriel)
        self.leilao.propor_lance(novo_lance)
        quantidade_lances_recebido = len(self.leilao.lances)
        self.assertEqual(2, quantidade_lances_recebido)

    def test_nao_deve_permitir_propor_lance_quando_usuario_for_o_mesmo(self):
        novo_lance_gabriel = Lance(self.usuario_gabriel, 200.00)
        with self.assertRaises(LanceInvalido):
            self.leilao.propor_lance(self.lance_gabriel)
            self.leilao.propor_lance(novo_lance_gabriel)
