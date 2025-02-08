import random         
import string

chars=" " + string.punctuation + string.digits+ string.ascii_letters
# list use for personal double comaa "" every value and all value in a index
chars=list(chars)
# copy use for  other variable copy 
key=chars.copy()
# isme key ke value unsequenc ho guy ge
random.shuffle(key)
print(chars)
print(key)

# ENCRYPT
plain_text=input("Enter a  message to encrypt:")
cipher_text=""

for letter in plain_text:
    index=chars.index(letter) 
    cipher_text+=key[index]

print(f"original message:{plain_text}")
print(f"encrypted message:{cipher_text}")

# DECRYPT
# enter output of the ENCRYPT in a dectypt input then answer return of the input ENCRYPT 
cipher_text=input("Enter a message to decrypt:")
plain_text=""

for letter in cipher_text:
    index=key.index(letter)
    plain_text+=chars[index]

print(f"encrypted message:{cipher_text}")
print(f"original message:{plain_text}")