import math
def userinput():
    num = int(input("Enter a number to check weather it is a prime number or composite number: "))
    return num

def prime(num):
    isprime = True
    for x in range(2, int(math.sqrt(num))+1):
        if(num%x==0):
            isprime = False
            break
    return(isprime)

def display(isprime, num):
    if(isprime==True):
        print("%d is a prime number"%(num))
    else:
        print("%d is a composite number"%(num))

def main():
    num = userinput()
    isprime = prime(num)
    display(isprime, num)
main()
