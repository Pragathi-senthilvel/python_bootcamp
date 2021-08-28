print("Enter five numbers:")
number_string_list = map(int, input().split())
sum = 0
for i in number_string_list:
	sum = sum + int(i)
print("Sum of all the number is =",sum)
