import string

def func(dc, st):
    new_st = ""
    for i in st:
        if i not in string.ascii_letters:
            new_st += i
            continue
        if i.isupper():
            new_st += dc[i]
        else:
            i = i.upper()
            new_st += dc[i].lower()
    return new_st

class Cipher:

    def __init__(self, word):
        self.dc_for_enc = {}
        self.dc_for_dec = {}
        wd = ""
        word = word.upper()
        s = string.ascii_uppercase
        for i in word:
            s = s.replace(i.upper(), "")
            if i not in wd:
                wd += i
            else:
                continue
        wd += s
        j = 0
        for i in string.ascii_uppercase:
            self.dc_for_enc[i] = wd[j]
            self.dc_for_dec[wd[j]] = i
            j += 1


    def encode(self, st):
        print(func(self.dc_for_enc, st))

    def decode(self, st):
        print(func(self.dc_for_dec, st))


cipher = Cipher("crypto")
cipher.encode("Hello world")
cipher.decode("Fjedhc dn atidsn")

