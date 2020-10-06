#Prompt to add the first number
print("Please enter a number")
first = int(input())

#Prompt to add a second number
print("Please enter...another number!")
second =int(input())

if first < second:
  print(first, "is smaller than", second)

elif first >second:
  print(first, "is bigger than", second)

else:
  print("System does not compute... ERROR...")

print("Congratulations! You win...absolutely nothing")
