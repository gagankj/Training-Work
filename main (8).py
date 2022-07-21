num = int(input("Enter a number between 1200 and 3000 : "))
if(1200<num<3000):
    if(num%8==0):
        if(num%6==0):
            print(num," is divisible by 4 and 8 and also by 6")
        else:
            print(num," is divisible by 4 and 8 and but not by 6")
    elif(num%4==0):
        print(num," is divisible by 4 but not by 8")
    else:
        print(num," is not divisible by 4 and 8")
else:
    print("Write a number between 1800 and 3000")
        
    