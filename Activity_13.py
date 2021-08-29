def input_num():
    start=int(input("enter the start number: "))
    stop=int(input("enter the stop number: "))
    return start,stop
def oddnos(start,stop):
    res=[]
    for num in range(start,stop):
        if(num%2!=0):
            res.append(num)
    return res
def display(odd_nos):
    print("Odd numbers from start number to stop number is: ",odd_nos)

def main():
    start,stop=input_num()
    odd_nos=oddnos(start,stop)
    display(odd_nos)
main()
