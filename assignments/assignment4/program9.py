"WAP to print count of all negative number from a given range(-15,50)"
x=int(input("start:"))
y=int(input("end:"))

count=0
for i in range(x,y):
    if(i<0):
        count=count+1
print(count)
