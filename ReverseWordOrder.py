
def receverseWord(inputStr):
    reversedarray = inputStr.split(" ")
    reversedarray.reverse()
    return reversedarray

inputStr = input("enter the the sentence : ")
print(receverseWord(inputStr))