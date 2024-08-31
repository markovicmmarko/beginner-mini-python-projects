import string,random

letters = list(string.ascii_letters)
symbols = list(string.punctuation)
numbers = ["0","1","2","3","4","5","6","7","8","9"]


def pwd_gen_mix():
    slova = int(input("How many letters would you like your password to contain? "))
    simboli = int(input("How many symbols would you like your password to contain? "))
    brojevi = int(input("How many numbers would you like your password to contain? "))
    password = []
    lts = random.sample(letters, slova)
    syms = random.sample(symbols, simboli)
    nms = random.sample(numbers, brojevi)
    password.extend(lts)
    password.extend(syms)
    password.extend(nms)
    random.shuffle(password)
    mix_password = "".join(password)

    return mix_password

sifra = pwd_gen_mix()
print(sifra)    