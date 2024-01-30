" Take two numbers from user checks if both are odd and then print the sum of them"

num1 = int(input("enter num: "))
num2 = int(input("enter num2: "))

if(num1%2==1 and num2%2==1):
    sum= num1 + num2
    print(sum)
else:
    print('No Output')
