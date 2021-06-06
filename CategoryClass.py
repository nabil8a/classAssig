class Category:

    def __init__(self, deposit, withdraw, transfer, checkBalance):
        self.deposit = deposit
        self.withdraw = withdraw
        self.transfer = transfer
        self.checkBalance = checkBalance

Food = Category(200,100,100,100)
Clothing = Category(150,50,50,150)
car = Category(10000,350,350,9650)
Classes = Category(5000,5000,5000,0)

for i in ['deposit', 'withdraw', 'transfer', 'checkBalance']:
    a = ('print(Food.%s)' %i)
    print(a)
    eval(a)