# coding: utf-8
import argparse
from cifra import Cifra

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cifra Vigenére")
    parser.add_argument(
        "-k", "--key", help="Chave para criptografia.", required=True, type=str,
        nargs=1
    )
    parser.add_argument(
        "-c", "--crypt", help="Criptografar frase.", type=str,
        nargs=1
    )
    parser.add_argument(
        "-d", "--decrypt", help="Descriptografar frase.", type=str,
        nargs=1
    )

    args = parser.parse_args()
    key = args.key
    action = "crypt" if args.crypt is not None else "decrypt"
    text = getattr(args, action)[0]

    c = Cifra()
    print getattr(c, action)(text, key).upper()
