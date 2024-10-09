import random
import string


def generatePassword(lenth):
    character = string.ascii_letters + string.punctuation
    password = "".join(random.choice(character) for i in range(lenth))
    return password

lenth = int(input("enter the lenth of pasword"))
print(generatePassword(lenth))
