# print("Hello world!")
# print("My name is Deepa.")

# # ctrl+/ is how we make a comment

# learner = "Deepa"
# print(learner)

# # This is a number/integer example
# ideal_number_of_pets = 2
# print(ideal_number_of_pets)

# # This is a float/decimal  example
# how_much_is_a_banana = 9.99
# print(how_much_is_a_banana)

# # This is a example of a boolean TRUE/FALSE
# is_our_pet_vaccinated = True
# print(is_our_pet_vaccinated)

# print(type(learner))
# print(type(ideal_number_of_pets))
# print(type(how_much_is_a_banana))
# print(type(is_our_pet_vaccinated))

# is_it_a_number = 333
# is_this_a_number = "333"

# print(type(is_it_a_number))
# print(type(is_this_a_number))

# statement = "The number of pets I want 2 dogs"

# print(statement)
'''
print(5+3)
print(5-3)
print(5*3)
print(5/3)

#Example of a modulo
print(10%3)
print(10/3)
print(10%5)

# show an example of an exponent
print(2**5)
print(2**2)
print(32**73)
print(2^2) # this is not an exponent, this is a bitwise operator '''
'''
# find the area of a rectangle
length = int(input("Enter the length: "))
width = 4
area = length * width
print(area)

# Find the tax amount 
price = 10
tax = price * 0.08
print(f"The tax on the item given is: {tax}")

#find the average
avg = (10+10+10)/3
print(avg) '''

# print("Per Scholas is Unlocking Potential and Changing the Face of Tech")
# print(10+90)
# print(300.5+0.5)
# print(12, 24, -2, sep=':')
# print('but', 'not', 'including', sep='**')
# print('but', 'not', 'including', sep='')

# #create a receipt
# customerName = input("Enter customer name: ")
# itemPrice = float(input("Enter item price: "))
# quantity = int(input("Enter quantity: "))
# totalCost = itemPrice * quantity
# roundedCost = round(totalCost, 2)

# print("Receipt")
# print(f"Customer Name: {customerName}")
# print(f"Item Price: ${itemPrice}")
# print(f"Quantity: {quantity}")
# print(f"Total Cost: {roundedCost}")

# #additional code
# print(f"Tax Amount: ${roundedCost * 0.08}")

# random_string = "We Don't live in a perfect world"

# #If you need to use single quotes in your string, then wrap it in double quotes. See the following example.
# my_string = "I'm a Python programmer!"
# print(my_string)

# otherString = 'The word "python" usually refers to a snake'
# print(otherString)

# tripleString = """Here's another way to embed "quotes" in a string"""
# print(tripleString)

# string = 'Hello World!'
# print(string)
# print(string[0])
# print(string[2:5])
# print(string[3:])
# print(string*2)
# print(string+'Everyone!')
# print(string.lower())
# print(string.replace('l','s'))
# print(len(string))
# print(string.strip())
# print(string.split(' '))

# string2 = 40000
# print(type(string2))
# print(type(str(string2)))

# MyInteger= 10
# print(type(MyInteger))
# # Converting integer to String
# integerToStr = str(MyInteger)
# print("Integer into String: ", integerToStr)
# print(type(integerToStr))

# mylist=[] # create a empty list
# print(mylist)
# # Create a list of strings.
# string_list = ["Hello", "Python", "World"]
# print(string_list)
# # Create a list of numbers.
# number_list = [3, 4, 5, 6, 8, 10]
# print(number_list)
# # Create a list of boolean values.
# boolean_list = [True, False, False, True]
# print(boolean_list)
# # Create a mixed list or list with heterogeneous data
# mixed_list = [3, 4, "Python", True]
# print(mixed_list)

# mylist = []
# print(mylist)
# string_list = ["Hello", "Python", "World"]
# print(string_list)

# # Create a string.
# my_string = "Hello World"
# # Create a list of characters from my_string.
# character_list = list(my_string)
# # Create a list of substrings from my_string.
# substring_list = my_string.split()
# # Print the results.
# print(my_string)        # Output: "Hello World"
# print(character_list)   # Output: ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
# print(substring_list)   # Output: ['Hello', 'World']
# substring_list[1] = 'Everyone'
# print(substring_list)   # Output: ['Hello', 'Everyone']

my_list = []
my_list.append("Hello")

# # Create a list.
# my_list = [1, 2, 3, 4, 5]
# # Traverse the list with a for loop.
# for element in my_list:
#     print(element)

# for i in my_list:
#     print(i)
# # Traverse the list by accessing the
# # indexes with the range() and len() functions.
# for i in range(len(my_list)):
#     print(f“Index {i} contains: {my_list[i]}”)

my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(my_list[0][0])  # Output: 1

# Iterate through each sublist.
for sublist in my_list:
    # Iterate through each sublist element.
    for element in sublist:
        print(element)
# output (each on a new line): 1 2 3 4 5 6 7 8 9

nums = [1, 2, 3, [4, 5, 6, [7, 8, [9]]], 10]
print(nums[3][3][2][0])  # Output: 9
