def OddOrEven(number):
    if (number%2==0):
        print(f"{number} is the even")
        
    else:
        print(f"{number} is the odd")


number = int(input("enter the find a number is even or odd"))
OddOrEven(number)