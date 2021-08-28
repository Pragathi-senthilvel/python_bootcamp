print("Enter five numbers a,b,c,d,e:")
a,b,c,d,e = map(int, input().split())
sum = 0
for i in a,b,c,d,e:
	sum = sum + int(i)
print("Sum of all the numbers is =",sum)


input_int = input("Enter five numbers a,b,c,d,e : ")
list  = input_int.split()
print("Calculating sum of input list")
sum = 0
for num in list:
    sum += int (num)
print("Sum = ",sum)
