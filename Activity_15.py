import math
def takeinput():                                               
    l = float(input("Enter the length of tromboloid: "))
    b = float(input("Enter the breadth of tromboloid: "))
    h = float(input("Enter the height of tromboloid: "))
    return l, b, h

def calculate(l,b,h): 
    k=(l**2)+(b**2)+(h**2)
    vol=((b**2)*(h**2))/(math.sqrt(k))
    rad=((3*(b**2)*(h**2))/((4*math.pi)*(math.sqrt(k))))**1/3
    return vol,rad

def display(vol,rad):
    print("Volume of the tromboloid is = %.3f " %vol)
    print("Radius of sphere having volume same as that of tromboloid is = %.3f " %rad)
    
def main():
    l,b,h=takeinput()
    vol,rad=calculate(l,b,h)
    display(vol,rad)
main()
