import math
l =float(input("Enter length l of the tromboloid : "))
b =float(input("Enter breadth b of the tromboloid : "))
h =float(input ("Enter height h of the tromboloid : "))
k =(l**2)+(b**2)+(h**2)
squareroot = k ** 0.5
volumeoftromboloid = ((b**2)*(h**2))/(squareroot)
print("Volume of the tromboloid is = %.3f " %volumeoftromboloid)
radiusofsphere = ((3*(b**2)*(h**2))/((4*math.pi)*(squareroot)))**1/3
print("Radius of sphere having volume same as that of tromboloid is = %.3f " %radiusofsphere)

