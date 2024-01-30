"WAP that prints all positive number from given range (start = -7 end = 8)"

x= int(input("start:"))
y=int(input("end:"))

for i in range(x,y,+1):
    if(i>0):
        print(i)
