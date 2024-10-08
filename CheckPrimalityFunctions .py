def PrimeNumber(input_int):
    if input_int <= 1:
        print("Not a prime number")
        return False
    
    for x in range(2, input_int):
        if input_int % x == 0:
            print("Not a prime number")
            return False
    
    print("Prime number")
    return True

PrimeNumber(5)
