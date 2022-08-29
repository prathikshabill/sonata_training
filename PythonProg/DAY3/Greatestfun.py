def greatest(num1,num2,num3):
    if (num1 > num2) and (num1 > num3):
        a=num1
    elif (num2 > num3) and (num2>num1):
        a=num2
    else:
        a=num3
    return a

num1 = int(input('Enter 1st number: '))
num2 = int(input('Enter 2nd number: '))
num3 = int(input('Enter 3rd number: '))
print(greatest(num1, num2, num3))
