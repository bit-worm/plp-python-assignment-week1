# A funtion to perform the arithmetic operation
def performOperation(operator):
    if(operator == '+'):
        return num1 + num2 # addition
    elif(operator == '-'):
        return num1 - num2 # subtraction
    elif(operator == '/'):
        try:
            return num1 / num2 # division
        except ZeroDivisionError:
            print("\nCan't divide by zero!")
            return None
    elif(operator == 'x'): 
        return num1 * num2 # multiplication

num1 = float(input("Enter 1st number: ")) # user input for first number
num2 = float(input("Enter 2nd number: ")) # user input for second number
operator = input("Select operator\n(+, -, /, x): ") # user input for operator

# call the funtion to perform arithmetic operation
result = performOperation(operator)

if(result != None):
    print("\n-------------------")
    print(f"{num1} {operator} {num2} = {result:.2f}") # the output
