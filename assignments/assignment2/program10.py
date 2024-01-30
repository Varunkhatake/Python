"Take two character from user check if the ascii  value both of chracter are odd then print the sum of ascii value of character"

char1 =input("enter chatracter: ")
char2 =input("enter character: ")

if(ord(char1)%2==1 and ord(char2)%2==1):
    sum = ord(char1)+ord(char2)
    print(sum)
else:
    print("No Output")

