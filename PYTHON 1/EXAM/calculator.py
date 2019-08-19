class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return(self.num1+self.num2)
    def sub(self):
        return(self.num1-self.num2)
    def mul(self):
        return(self.num1*self.num2)
    def div(self):
        if(self.num2==0):
            print("Division not possible")
        else:
            return(self.num1/self.num2)
print("1.ADDITION 2.SUBSTRACTION 3.MULTIPLICATION 4.DIVISION")
num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
cal=Calculator(num1,num2)
ch=int(input("enter your choice"))
if(ch==1):
    print(cal.add())
elif(ch==2):
    print(cal.sub())
elif(ch==3):
    print(cal.mul())
elif(ch==4):
    print(cal.div())
else:
    pass
