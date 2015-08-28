# coding: utf-8
import unittest
from cifra import Cifra


class TestCifra(unittest.TestCase):

    def test_alfabeto_A(self):
        """
            Testa alfabeto A
        """
        c = Cifra()
        self.assertEquals(str(c.grid['a']), 'abcdefghijklmnopqrstuvwxyz')

    def test_alfabeto_B(self):
        """
            Testa alfabeto B
        """
        c = Cifra()
        self.assertEquals(str(c.grid['b']), 'bcdefghijklmnopqrstuvwxyza')

    def test_alfabeto_C(self):
        """
            Testa alfabeto C
        """
        c = Cifra()
        self.assertEquals(str(c.grid['c']), 'cdefghijklmnopqrstuvwxyzab')

    def test_letra_A_no_alfabeto_A_deve_retorno_A(self):
        """
            A letra A na grelha de vigenére deve retornar A no alfabeto A
        """
        c = Cifra()
        self.assertEquals(c.translater('A', 'A'), 'a')

    def test_letra_A_no_alfabeto_B_deve_retorno_B(self):
        """
            A letra A na grelha de vigenére deve retornar B no alfabeto B
        """
        c = Cifra()
        self.assertEquals(c.translater('A', 'B'), 'b')

    def test_letra_A_no_alfabeto_C_deve_retorno_C(self):
        """
            A letra A na grelha de vigenére deve retornar C no alfabeto C
        """
        c = Cifra()
        self.assertEquals(c.translater('A', 'C'), 'c')

    def test_letra_Z_no_alfabeto_I_deve_retorno_H(self):
        """
            A letra Z na grelha de vigenére deve retornar H no alfabeto I
        """
        c = Cifra()
        self.assertEquals(c.translater('Z', 'I'), 'h')

    def test_retornar_None_para_o_que_nao_estiver_traduzido(self):
        """
            Para o que não estiver no grelha de Vigenère retorna None.
        """
        c = Cifra()
        self.assertEquals(c.translater(1, 'I'), "")

    def test_chave_maior_que_o_texto_base_retornar_exception(self):
        """
            Para chaves maiores que o texto sistema levanta uma exception.
        """
        c = Cifra()
        self.assertRaises(ValueError, c.crypt, 'a', 'bb')

    def test_normaliza_tamanho_LIMAO(self):
        """
            Caso key seja maior que o texto função normaliza tamanho.
        """
        c = Cifra()
        self.assertEquals(
            c.match_size('ATACARBASESUL', 'LIMAO'), 'LIMAOLIMAOLIM')

    def test_normaliza_tamanho_LIMA(self):
        """
            A chave LIMA com um texto de 13 caracteres o retorno deve
            ser LIMALIMALIMAL
        """
        c = Cifra()
        self.assertEquals(
            c.match_size('ATACARBASESUL', 'LIMA'), 'LIMALIMALIMAL')

    def test_ATACARBASESUL_chave_LIMAO_retorno_LBMCOCJMSSDCX(self):
        """
            A criptografia de ATACARBASESUL com a chave LIMAO deve
            ser LBMCOCJMSSDCX
        """
        c = Cifra()
        self.assertEquals(
            c.crypt('ATACARBASESUL', 'LIMAO').upper(), 'LBMCOCJMSSDCX')

    def test_MORREU_chave_UVA_retorno_GJRLZU(self):
        """
            A criptografia de MORREU com a chave UVA deve ser GJRLZU
        """
        c = Cifra()
        self.assertEquals(c.crypt('MORREU', 'UVA').upper(), 'GJRLZU')

    def test_GJRLZU_chave_UVA_MORREU(self):
        """
            O texto criptografado GJRLZU com chave UVA retorna MORREU
        """
        c = Cifra()
        self.assertEquals(c.crypt('GJRLZU', 'UVA', True).upper(), 'MORREU')
