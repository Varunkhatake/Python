"Write a program to print sum of all num given range (start=1,end=10)"

num1 = int(input("enter start: "))
num2 = int(input("enter end: "))
sum=0
for i in range(num1,num2):
    sum=sum+i
print(sum)

