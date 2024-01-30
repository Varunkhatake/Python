"WAP to print the ascii value of from given character range"

x=int(input("start:"))
y=int(input("end:"))

for i in range(x,y):
    print("ascii value of ",chr(i),"is",ord(i))

