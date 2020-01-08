#This is a comment
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')
result = int(num1) + int(num2)
#print('Addition is ',result) this is trivial way of printing statements
print("Addition of {0} and {1} is {2}".format(num1,num2,result))

result = int(num1) - int(num2)
print("Subtraction of {0} and {1} is {2}".format(num1,num2,result))

result = int(num1) * int(num2)
print("Multiplication of {0} and {1} is {2}".format(num1,num2,result))

result = int(num1) / int(num2)
print("Division of {0} and {1} is {2}".format(num1,num2,result))