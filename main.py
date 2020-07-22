# def numbers(num1,num2):
#   print(num1+num2)

# number1 = input("Say one whole number:")
# number2 = input("Say a second whole number:")
# number1 = int(number1)
# number2 = int(number2)

# numbers(number1,number2)



###DOES NOT WORK

# def calculator(num1, math, num2):
#   print(num1, math, num2 )

# number1 = int(input("Say one whole number:"))
# number2 = int(input("Say another whole number:"))
# mathematics = input("Do you want to multiply '*', add '+', subtract '-', or divide '/'? Please print the character, not the word: ")

# calculator(number1, mathematics, number2)

def addNumbers(num1, num2):
  print(num1 + num2)

def subNumbers(num1, num2):
  print(num1 - num2)
# Ask user to enter two numbers. Plug these two numbers into the addNumbers function

num1 = int(input("enter number 1: "))
num2 = int(input("enter number 2: "))
operator = input("add or subtract: ")

if operator.lower() == "add":
  addNumbers(num1, num2)
elif operator.lower() == "subtract":
  subNumbers(num1, num2)
else:
  print("that's not an operator")
