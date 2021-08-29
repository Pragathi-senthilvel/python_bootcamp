a,b,c=input("Enter three numbers number: ").split()
if (a > b) and (a > c):
   greatest = a
elif (b > a) and (b > c):
   greatest = b
else:
   greatest = c
 
print("{0} is the greatest number among {1}, {2} and {3}".format(greatest,a,b,c))
