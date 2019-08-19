
class Bank:
    def setValues(self,acno,name):
        self.bankname="SBI"
        self.minimum=3000
        self.balance=self.minimum
        self.acno=acno
        self.name=name
        print("account has been created")
    def displayValues(self):
        print("ACNO="+self.acno)
        print("Available balance=",self.balance)
    def deposit(self,amt):
        self.balance +=amt
        print("your account",self.acno,"has been credited",amt)
        print("current balance=",self.balance)
    def withdrawal(self,amt):
        # if(amt>self.balance):
        #     print("insufficient balance")
        # else:
        self.balance-=amt
        print("your account",self.acno,"has been debited with",amt,)
        print("current balance=",self.balance)
    def bal_enq(self):
        print("your balance amount is",self.balance)

obj=Bank()
obj.setValues(1001, "anu")
obj.deposit(10000)
obj.withdrawal(5000)
obj.bal_enq()
# print("1.DEPOSIT","2.WITHDRAWAL","3.BALANCE ENQUIRY",)
# ch=int(input("enter your choice"))
# if ch==1:
#
#     obj.deposit(10000)
# elif(ch==2):
#     obj.withdrawal(5000)
# elif(ch==3):
#     obj.bal_enq()
# else:
#     pass


