input_int = input("Enter five numbers : ")
list  = input_int.split()
sum = 0
for num in list:
    sum += int (num)
print("Sum of input list = ", sum)
