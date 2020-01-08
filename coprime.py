#Practical 1.c Date 9 January 2020
def iscoprime():
    flag = 0
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    if num1>num2:
        small = num2
    else:
        small = num1
    small = int(small/2)
    for x in range(2,small):
        if num1%x==0 and num2%x==0:
            flag = 1
    if flag==0:
        return False
    else:
        return True
print(iscoprime())