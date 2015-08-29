[![Build Status](https://snap-ci.com/riquellopes/cifra-de-vigenere/branch/master/build_image)](https://snap-ci.com/riquellopes/cifra-de-vigenere/branch/master)
[![Coverage Status](https://coveralls.io/repos/riquellopes/cifra-de-vigenere/badge.svg?branch=master&service=github)](https://coveralls.io/github/riquellopes/cifra-de-vigenere?branch=master)
Cifra Vigenére
=========
Origem: [Wikipédia, a enciclopédia livre](https://pt.wikipedia.org/wiki/Cifra_de_Vigenère).

A **cifra de Vigenère** é um método de criptografia que usa uma série de diferentes cifras de César baseadas em letras de uma senha. Trata-se de uma versão simplificada de uma mais geral cifra de substituição polialfabética, inventada por Leone Battista Alberti cerca de 1465.

Como criptografar:
---------
```shell
    ./run.py --key LIMAO -crypt HENRIQUE
    SMZRWBCQ
```

Como descriptografar:
------------------
```shell
    ./run.py --key LIMAO -decrypt SMZRWBCQ
    HENRIQUE
```
