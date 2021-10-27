from random import *
import time
caractère = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&'()*+,-./:;<=>?@[\]^_`{|}~").lower()
a = int(input("The number of characters in the password: "))
print("The password is: ")
for i in range(a):
    password = ""
    cara = choice(caractère)
    print(cara, end='')