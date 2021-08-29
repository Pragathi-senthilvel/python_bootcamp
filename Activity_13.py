def input_num():
    start=int(input("Enter the start number:"))
    stop=int(input("Enter the stop number:"))
    return start,stop
def odd(start,stop):
    for num in range(start,stop):
        if num % 2 !=0:
            print(num,end = ", ")
def main():
    a,b=input_num()
    odd(a,b)
main()
