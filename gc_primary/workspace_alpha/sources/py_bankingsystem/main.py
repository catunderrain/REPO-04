# Parent Class
class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Name ", self.name)
        print("Age  ", self.age)
        print("Gender ", self.gender, '\n')


# Child Class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.cat = 0

    def deposit(self, amount):
        self.amount = amount
        self.cat = self.cat + self.amount
        print("Account balance has been updated : £", self.cat)

    def withdraw(self, amount):

        self.amount = amount
        if self.amount > self.cat:
            print("Insufficient Funds | Balance Available : £", self.cat)
        else:
            self.cat = self.cat - self.amount
            print("Account balance has been updated : £", self.cat)

    def view_balance(self):
        self.show_details()
        print("Account balance: £", self.cat)


u_list = [['Thai Toan', 21, 'Male']]


def getinfo(n):
    return Bank(u_list[n][0], u_list[n][1], u_list[n][2])


TT = getinfo(0)

TT.show_details()

TT.deposit(200)
TT.withdraw(300)
TT.withdraw(100)
TT.view_balance()
