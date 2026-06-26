# If statements - is used to compare things
# x= "hi"
# print(x)
#Going to ride the coney island roller coaster
#height >= 48
# height = int(input("How tall are you? "))  # Example height
# if height >= 48:
#     print("You can ride the roller coaster!")
# else:
#     print("Sorry, you are not tall enough to ride the roller coaster.")

# create a password checker
# username = HotDogWater123
# password = bluepen

# password = "bluepen"

# userLoginInput = input("Enter your password: ")
# if userLoginInput == password:
#     print("Open Sesame")
# else:
#     print("Access denied")

#check a number is even or odd

# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print("The number is even.")    
# else:
#     print("The number is odd.")

# # Write a for loop for the value 1-152
# for number in range(1,153):
#     print(number)

# for number in range(10,0, -1):
#     print(number)

# print("Blast off!")

# # who likes root beer?
# numberofRootBeers = 31

# for i in range(numberofRootBeers, 1, -4):
#     print(f" {i} bottles of root beer on the wall!")

# # what is the sum of 1-427
# total = int(input("Enter a number: "))

# for number in range(1,total+1):
#     total +=number
# print(f"The sum of 1-{total} is: {total}!")

# # while loop example
# password = "bluepen"
# userLoginInput = input("Enter your password: ")
# while userLoginInput != password:
#     print("Wrong password, try again.")
#     userLoginInput = input("Enter your password: ")
# print("Access granted!")

numberList = [7, 42, 8, 946, -1, 4235, 6,730]

largestNumber = numberList  # Assume the first number is the largest
print(largestNumber) 
for number in numberList:
    if number > largestNumber:
        largestNumber = number

print(largestNumber) 

# who wants to play.. Guess that number
secretNumber = 7

while guess != secretNumber:
    guess = int(input("Guess a number between 1 and 10: "))

print("you got it! The secret number is: " + str(secretNumber))