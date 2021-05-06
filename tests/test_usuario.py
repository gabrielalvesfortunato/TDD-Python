from src.leilao.dominio import Usuario, Leilao, Lance
from src.leilao.excecoes import *
import pytest

class TestUsuario:

    # Inicializa as  fixtures
    @pytest.fixture
    def zoe(self):
        zoe = Usuario("Zoe")
        zoe.depositar_valor_carteira(1000.00)  # Valor em carteira 1000.00
        return zoe

    @pytest.fixture
    def leilao(self):
        leilao = Leilao("Casaco")
        return leilao

    def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance(self, zoe, leilao):
        lance_zoe = Lance(zoe, 500.00) # Lance 500.00
        zoe.retirar_valor_carteira(lance_zoe.valor)
        leilao.propor_lance(lance_zoe)
        assert zoe.carteira == 500.0 # Valor esperado na carteira 500.00

    def test_deve_permitir_propor_lance_quando_o_valor_for_menor_que_o_valor_da_carteira(self, zoe, leilao):
        lance_zoe = Lance(zoe, 900.00) # Lance 900.00
        zoe.retirar_valor_carteira(lance_zoe.valor)
        leilao.propor_lance(lance_zoe)
        assert zoe.carteira == 100.00 # Valor esperado na carteira 100.00

    def test_deve_permitir_propor_lance_quando_o_valor_for_igual_ao_valor_da_carteira(self, zoe, leilao):
        lance_zoe = Lance(zoe, 1000.00) # Lance 1000.00
        zoe.retirar_valor_carteira(lance_zoe.valor)
        leilao.propor_lance(lance_zoe)
        assert zoe.carteira == 0.0 # Valor esperado na carteira 0.0

    def test_nao_deve_permitir_propor_um_lance_quando_o_valor_for_maior_que_o_valor_carteira(self, zoe, leilao):
        with pytest.raises(LanceInvalido) and pytest.raises(ValorInsuficiente):
            lance_zoe = Lance(zoe, 1100.00)
            zoe.retirar_valor_carteira(lance_zoe.valor)
            leilao.propor_lance(lance_zoe)
