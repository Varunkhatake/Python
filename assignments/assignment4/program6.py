"WAP to print number divisible by 7 but not divisible by 3 between 1-100"
x = int(input("start:"))
y = int(input("end: "))

for i in range(x,y):
    if(i%7==0 and i%3!=0):
        print(i)
