import string
from functools import reduce


def distinct(items):
    return [items[i] for i in range(len(items)) if items[i] not in items[:i]]


def create_table(keyword):
    alph = [*string.ascii_uppercase]

    base_letters = distinct([*keyword.upper()])
    enc_alph = base_letters + list(filter(lambda letter: letter not in base_letters, alph))

    encoding_table = {key: val for (key, val) in zip(alph, enc_alph)}
    decoding_table = {val: key for (key, val) in encoding_table.items()}

    return encoding_table, decoding_table


def encode_str(word, enc_table):
    return reduce(lambda acc, letter: acc + encode_letter(letter, enc_table), word, '')


def encode_letter(letter: str, enc_table):
    enc = enc_table.get(letter.upper()) or letter
    return enc if letter.isupper() else enc.lower()


class Cipher:
    def __init__(self, keyword):
        self.encoding_table, self.decoding_table = create_table(keyword)

    def encode(self, word):
        return encode_str(word, self.encoding_table)

    def decode(self, word):
        return encode_str(word, self.decoding_table)


if __name__ == '__main__':
    print(string.ascii_lowercase)

    cipher = Cipher("crypto")

    res = cipher.encode("Hello world")
    print(f"res={res}")
    assert res == "Btggj vjmgp"

    res = cipher.decode("Fjedhc dn atidsn")
    print(f"res={res}")
    assert res == "Kojima is genius"
