"Write a program to print all even num from given range start=10,end=20"

num1=int(input("enter start: "))
num2=int(input("enter end: "))
for i in range(num1,num2):
    if(i%2==0):
        print(i)
