import random
import string


def password_generator():
    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    symbols = list(string.punctuation)

    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_numbers = int(input("How many numbers would you like?\n"))
    nr_symbols = int(input("How many symbols would you like?\n"))
    
    password_letters = random.sample(letters, nr_letters)
    password_numbers = random.sample(numbers, nr_numbers)
    password_symbols = random.sample(symbols, nr_symbols)
    password = password_letters + password_numbers + password_symbols
    random.shuffle(password)
    final_password = "".join(password)
    return final_password

sifra = password_generator()
print(sifra)
