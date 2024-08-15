print("****************")
print("Basic Calculator")
print("****************")


first_number = int(input("Enter First number: "))
second_number = int(input("Enter Second number: "))

print('Choose the operation to perform')
print('Addition +')
print('Subtraction -')
print('Multiplication *')
print('Division /')
print('Power **')
print('Floor Division //')
print('Modulus %')

operation =  str(input("Enter Operation Symbol: "))

if operation == '+':
    print("Sum of two numbers : ")
    result = float (first_number + second_number)
    print(result)
elif operation == '-':
    print("Subtraction of two numbers : ")
    result = first_number - second_number
    print(result)
elif operation == '*':
    print("Multiplication of two numbers : ")
    result = first_number * second_number
    print(result)
elif operation == '**':
    print("Power of a number : ")
    result = first_number ** second_number
    print(result)
elif operation == '/':
    print("Division of two numbers : ")
    result = first_number / second_number
    print(result)
elif operation == '//':
    print("Floor Division of two numbers : ")
    result = first_number // second_number
    print(result)
elif operation == '%':
    print("Modulus of two numbers : ")
    result = first_number % second_number
    print(result)
else: 
    "Wrong Choice!"




