"WAP to determine whether entered angles are difine a right-angle-trangle "

angle1 = int(input("enter angle1: "))
angle2 = int(input("enter angle2: "))
angle3 = int(input("enter angle3: "))

if(angle1+angle2+angle3==180):
    if(angle1==90 or angle2==90 or angle3==90):
        print("angles defines right-angle-trangle")
    else:
        print("angles not defines right-angle-trangle")

else:
    print(" angles not defines trangle")
