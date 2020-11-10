# num = int(input("Please input a number: "))
# if (num%2) == 0:
#     print ('the number is even')
# else:
#     print ('the number is odd')

"""
Take two inputs from the command line, then convert both to an int the first number will be the starting number, 
and the second will be the ending number. Create a loop that goes from the starting number to the ending number, 
and only prints the even numbers.
"""
# num_1 = int(input("First number: "))
# num_2 = int(input("Second number: "))
# if (num_1 == num_2) and (num_1%2 == 0):
#     print(num_1)
# else:
#     while (num_1 != num_2):
#         if (num_1 < num_2):
#             num_1 += 1
#             if (num_1%2 == 0):
#                 print(num_1)
#         if (num_1 >num_2):
#             num_1 -= 1
#             if (num_1%2 == 0):
#                 print(num_1)

# var_1 = []; 
# x = "text"; 
# var_1.append(x); 
# print(var_1)
"""
Create an empty list called shopping_list then using user input fill the list with 5 elements. 
Hint: You can do this with 6 variables including the list
"""
shopping_list = []
item_1 = input("First item: ")
item_2 = input("Seconde item: ")
item_3 = input("Third item: ")
item_4 = input("Fourth item: ")
item_5 = input("Fifth item: ")
shopping_list.append(item_1)

shopping_list.append(item_2)

shopping_list.append(item_3)

shopping_list.append(item_4)

shopping_list.append(item_5)
print(shopping_list)