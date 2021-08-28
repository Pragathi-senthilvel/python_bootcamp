input_int = input("Enter five numbers : ")
numbers  = input_int.split()
sum = 0
for num in numbers:
    sum += int (num)
print("Sum of input list = ", sum)
