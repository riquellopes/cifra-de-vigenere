# coding: utf-8
import string


class Cifra(object):

    @property
    def grid(self):
        """
            Cria grelha de Vigenére.
        """
        grid = {}
        alphabet = string.ascii_lowercase
        for pos in xrange(26):
            letter_now = alphabet[pos]
            try:
                letter_previous = alphabet[pos-1]
                grid[letter_now] = grid[letter_previous][1:] + letter_previous
            except:
                grid[letter_now] = alphabet
        return grid

    def crypt(self, text, key, decrypt=False):
        """
            Criptografa texto e decriptografa.
        """
        if len(text) < len(key):
            raise ValueError(
                "O tamanho da chave deve ser menor do que o do texto.")

        key = self.match_size(text, key)
        crypt = ""
        for l in range(len(text)):
            crypt += self.translater(text[l], key[l], decrypt)
        return crypt

    def translater(self, letter, alphabet, decrypt=False):
        """
            Traduz letra usando a grelha de Vigenère.
        """
        try:
            for pos in xrange(26):
                if decrypt:
                    index = 'a'
                    alpha = alphabet.lower()
                else:
                    index = alphabet.lower()
                    alpha = 'a'

                if self.grid[alpha][pos] == letter.lower():
                    translater = self.grid[index][pos]
                    break
            return translater
        except:
            return ""

    def match_size(self, text, key):
        """
            Normaliza tamanho de uma chave.
        """
        textlen = len(text)
        keylen = len(key)
        pos_now = 0
        new_key = ""
        start = True

        while start:
            for pos in xrange(keylen):
                new_key += key[pos]
                pos_now += 1
                if pos_now == textlen:
                    start = False
                    break
        return new_key
