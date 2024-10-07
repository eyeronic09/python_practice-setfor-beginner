def palindrome (inputStr):
    reversedStr = inputStr[::-1]
    if (inputStr == reversedStr):
        print("palindrome")
    else:
        print("its not an paildrome")
    

inputStr = input("enter the word to check wethere its a palindrome")
(palindrome(inputStr))