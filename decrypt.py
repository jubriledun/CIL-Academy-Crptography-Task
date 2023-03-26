
import random, time

def decrypt(ciphertext, key):
    decrypted_text = ""
    for i in range(0, len(ciphertext), key+1):
        decrypted_text += ciphertext[i]
    return decrypted_text

ciphertext = input("Enter the ciphertext")
key = int(input("Input a key as a number between 1 and 10"))
while not (key>=1 and key<=10):
    print("Invalid key, try again!")
    key = int(input("Input a key as a number between 1 and 10"))
#Process...
print("...")
time.sleep(1)
print("Decrypting plaintext...")
time.sleep(1)
print("...")
time.sleep(1)
decrypted_text = decrypt(ciphertext, key)
#Output...
print("Decrypted text:")
print(decrypted_text)

