import string
from typing import Literal


def cipher(word, shift:int, mode:Literal["encrypt","decrypt"]):
    if not 0 < shift < 26:
        raise ValueError("Shift must be between 1 and 25.")
    if mode not in ("encrypt", "decrypt"):
        raise ValueError("Invalid option. Choose 'encrypt' or 'decrypt'.")
    
    alphabet = list(string.ascii_lowercase + string.ascii_lowercase)
    final_word = ""

    if mode == "encrypt":    
        for letter in word.lower():
            new_letter = alphabet[alphabet.index(letter) + shift]
            final_word += new_letter
    else:
        for letter in word.lower():
            new_letter = alphabet[alphabet.index(letter) - shift]
            final_word += new_letter
    return final_word


print(cipher("tigarz", 20, "encrypt"))

