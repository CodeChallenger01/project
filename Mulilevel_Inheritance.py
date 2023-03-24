#Multilevel Programming in Python
class Sum:
    def sum(self,a,b):
        z=a+b
        print("Sum :",z)

class Multi(Sum):
    def multi(self,a,b):
        z=a*b
        print("Multi :",z)

class Divide(Multi):
    def divide(self,a,b):
        z=a/b
        print("Divide :",z)
        # ob=multi(a,b)


obj=Divide()
while True:
    a = int(input("Enter the First number :"))
    b = int(input("Enter the Second number :"))
    print("\nEnter :")
    print("1.Addition\n2.Multipliction\n3.Division\n4.Exit from Program")
    ch=int(input("Enter Your Choice :"))
    if ch==1:
        obj.sum(a,b)
    elif ch==2:
        obj.multi(a,b)
    elif ch==3:
        obj.divide(a,b)
    elif ch==4:
        exit(0)
    else:
        print("Wrong Input")
        exit(0)
