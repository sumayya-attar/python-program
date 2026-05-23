#python program to create a simple calculator

#3 steps to build calculator program
# 1. functions for basic operations
# 2.user input
# 3.print results

# step 1: createfunctions
#function for addition
def add(num1, num2):
    return num1 + num2

#function for subtraction
def sub(num1, num2):
    return num1 - num2

#function for multiplication
def mul(num1, num2):
    return num1 * num2

#function for division
def div(num1, num2):
    return num1 / num2

#function for average
def avg(num1, num2):
    return (num1 + num2) / 2

#step 2: user input
print("Please select a operation:\n "\
      "1. Add\n" \
      "2. Subtract\n" \
      "3. Multiply\n" \
      "4. Divide\n" \
      "5. Average\n")
 
select = int(input("select a operation from 1,2,3,4,5: "))

number1 = int(input("Enter first number:"))
number2 = int(input("Enter second number:"))

#step 3: print results
if select == 1:
    print(number1, "+", number2, "=", add(number1, number2))
elif select == 2:
    print(number1, "-", number2, "=", sub(number1, number2))
elif select == 3:
    print(number1, "*", number2, "=", mul(number1, number2))
elif select == 4:
    print(number1, "/", number2, "=", div(number1, number2))
elif select == 5:
    print("Average of", number1, "and", number2, "is", avg(number1, number2))
else:
    print("Invalid input!")