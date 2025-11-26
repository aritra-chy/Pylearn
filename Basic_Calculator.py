# def addition(x, y):
#     return x + y
# def subtraction(x, y):
#     return x - y
# def multiplication(x, y):
#     return x * y
# def division(x, y):
#     return x // y



print("1 : Add")
print("2 : Subtract")
print("3 : Multiply")
print("4 : Divide")

option = int(input("Select operation: "))
result = 0

if(option in [1,2,3,4]):
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if(option == 1):
        result = num1+num2
    elif(option == 2):
        result = num1-num2
    elif(option == 3):
        result = num1*num2
    elif(option == 4):
        if((num2) == 0):
            print("Division by zero is not allowed")
        else:
            result = num1/num2
else:
    print("Invalid option selected")
    
print("The result is: {} ".format(result))

