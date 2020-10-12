#First User input
print("Please enter the first whole number")
num1 = int(input())

#Second User input
print("Please enter the second whole number")
num2 = int(input())

#Third User input
print("Please enter the third whole number")
num3 = int(input())

even_num = 0
odd_num = 0

#Working out what numbers are odd or even 
if (num1 % 2 == 0):
  even_num = even_num + 1
else:
  odd_num = odd_num + 1

if (num2 % 2 == 0):
  even_num = even_num + 1
else:
  odd_num = odd_num + 1

if (num3 % 2 == 0):
  even_num = even_num + 1
else:
  odd_num = odd_num + 1

#count how many of each type to come to result
print("There were {} even and {} odd numbers" .format(even_num, odd_num))
