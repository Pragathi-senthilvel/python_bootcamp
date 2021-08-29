def input_num():
    start=int(input("Enter the start number: "))
    stop=int(input("Enter the stop number: "))
    return start,stop

def displayodd(start,stop):
    odd=[*range(start,stop+1,2)]
    print(*odd,sep="\n")
   
def main():
    start,stop=input_num()
    if start % 2 ==0:
            start=start+1
            
    displayodd(start,stop)
    
main()
