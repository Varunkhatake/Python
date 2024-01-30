"WAP    to print all the character value of givenn Ascii value from the user"

x = int(input("start : "))
y = int(input("end: "))

if (x>64 and y<91 or x>96 and y<124):
    for i in range(x,y):
        print("character of ascii",i,"is",chr(i))
else:
    print("wrong input")

