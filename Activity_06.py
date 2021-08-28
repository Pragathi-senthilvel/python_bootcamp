input_int = input("Enter five numbers : ")
a_list = input_int.split()
first_three = a_list[0:3]
print("Sliced list is : ", first_three)
a_list[0]=0
a_list[4]=0
print("Replaced list-1 : ",a_list)
first_three[0]=0
first_three[2]=0
print("Replaced list-2 : ",first_three)
