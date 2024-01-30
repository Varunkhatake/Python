"WAP to print numbers which divisible by both 3 and 5"

x=int(input("start:"))
y=-int(input("end:"))

for i in range(x,y):
    if(i%3==0 and i%5==0):
        print(i)
