def main():
    a,b=input_numbers()
    summation=add(a,b)
    display(a,b,summation)
    
def input_numbers():
    a,b=input("Enter two numbers : ").split()
    a,b=[int(a),int(b)]
    return a,b

def add(x,y):
    return x+y

def display(x,y,sum):
   print("The sum of {0} + {1} = {2}".format(x,y,sum))

main()
