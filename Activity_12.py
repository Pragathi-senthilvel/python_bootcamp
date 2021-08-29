def input_num():
    a,b,c=input("Enter three numbers: ").split()
    a,b,c=[int(a),int(b),int(c)]
    return a,b,c
def big(a,b,c):
    greatest=a
    if (a>b) and (a>c):
        greatest=a
    elif (b > a) and (b>c):
        greatest=b
    else:
        greatest=c
    return greatest

def main():
    x,y,z=input_num()
    greatest=big(x,y,z)
    print("{0} is the greatest number among {1} , {2} and {3}".format(greatest,x,y,z))
main()

