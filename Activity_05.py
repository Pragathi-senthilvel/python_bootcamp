print("Enter five numbers a,b,c,d,e:")
a,b,c,d,e = map(int, input().split())
sum = 0
for i in a,b,c,d,e:
	sum = sum + int(i)
print("Sum of all the number is =",sum)
