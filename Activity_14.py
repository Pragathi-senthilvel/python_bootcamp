def CheckIfPrime ():
    num1 = input("Enter a number to check weather it is a prime number or not: ")
    a = int(num1)
    b = 2
    c = ("Yes {0} is a prime number".format(num1))
    while b < a:
        if a%b == 0:
            c = ("No {0} is not a prime number".format(num1))
        b = b+1
    print(c)
CheckIfPrime ()
