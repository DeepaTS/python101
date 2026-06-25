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

#create a receipt
customerName = input("Enter customer name: ")
itemPrice = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
totalCost = itemPrice * quantity
roundedCost = round(totalCost, 2)

print("Receipt")
print(f"Customer Name: {customerName}")
print(f"Item Price: ${itemPrice}")
print(f"Quantity: {quantity}")
print(f"Total Cost: {roundedCost}")

#additional code
print(f"Tax Amount: ${roundedCost * 0.08}")