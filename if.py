num1 = float(input('please insert the first number : '))
num2 = float(input('please insert the second number : '))
operation = input('please insert your desired operation among : +,-,*,/')

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result == num1 * num2
elif operation == '/':
    result = num1 / num2
else:
    print('the operation is not defined')
print(result)
