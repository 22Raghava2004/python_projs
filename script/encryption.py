#substitution encryption# this is a simple substitution cipher where each character is replaced by a randomly shuffled character from the same set of characters.
#This code allows the user to encrypt and decrypt messages using a randomly shuffled key

import random
import string
chars=" "+string.punctuation+string.digits+string.ascii_letters
chars=list(chars)
key=chars.copy()
random.shuffle(key)
#print(f"chars{chars}")
#print(f"key{key}")  

#encrypt

while True:
    access=input("what to do encrytp or decrypt? (e/d/q): ").upper()
    if access =="E":
        plain_text=input("enter your letter to encrypt")
        cipher_text=""
        for letter in plain_text:
            index = chars.index(letter)
            cipher_text+=key[index]
        print(f"original message :{plain_text}")
        print(f"encrytped message :{cipher_text}")
        continue

    if access=="D":
        cipher_text=input("enter the letter to decrypt")
        plain_text=""
        for letter in cipher_text:
            index = key.index(letter)
            plain_text+=chars[index]
        print(f"encrytped message :{cipher_text}")          
        print(f"original message :{plain_text}")
        continue
    if access=="Q":
        print("quitting")
        break

    if access !="E" or access!="D":
        print("what to do not given properly")
        continue
    
