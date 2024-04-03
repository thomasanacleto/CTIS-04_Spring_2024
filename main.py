#Create a program that uses a list of 'N' numbers from # user input. 
# From the list, find the 2nd largest #number and 
# print the output. 
# If only 1 number is #present in the list, print 
# 'inf'

user_input = int(input('How many numbers would you like to enter? '))
list_of_numbers = []
for i in range(user_input):
  user_input2 = int(input('Enter a number : '))
  list_of_numbers.append(user_input2)

list_of_numbers.sort()
if len(list_of_numbers) > 1:
  print(list_of_numbers[-2])

# if only 1 number is present in the list print 'inf'
else:
  print('inf')
  

