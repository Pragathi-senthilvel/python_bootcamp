import math
l =float(input("Enter length l of the tromboloid : "))
b =float(input("Enter breadth b of the tromboloid : "))
h =float(input ("Enter height h of the tromboloid : "))
k =(l**2)+(b**2)+(h**2)
volumeoftromboloid = ((b**2)*(h**2))/(math.sqrt(k))
print("Volume of the tromboloid is = %.3f " %volumeoftromboloid)
radiusofsphere = ((3*(b**2)*(h**2))/((4*math.pi)*(math.sqrt(k))))**1/3
print("Radius of sphere having volume same as that of tromboloid is = %.3f " %radiusofsphere)


