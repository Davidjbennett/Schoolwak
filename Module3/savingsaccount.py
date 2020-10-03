class savingsAccount:
    '''Defines a savings account'''

    #static variables
    RATE = 0.02
    MIN_BALANCE = 25

    def __init__(self, name, pin, balance = 0.0):
        self.name = name
        self.pin = pin 
        self.balance = balance
    
    def __str__(self):
        result = "Name: " + self.name + "\n"
        result += "PIN: " + self.pin + "\n"
        result += "Balance: " + f"{self.balance:.2f}"
        return result
    
    def getBalance(self):
        return f"{self.balance:.2f}"
    
    def getName(self):
        return self.name
    
    def getPin(self):
        return self.pin

    def deposit(self, amount):
        '''deposits the amount into our balance'''
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            return "Amount must be >= 0"
        elif self.balance < amount:
            return "Insufficient Funds"
        else:
            self.balance -= amount
            return None

    def computeInterest(self):
        interest = self.balance * savingsAccount.RATE
        self.deposit(interest)
        return f"{interest:.2f}"
            

if __name__ == "__main__":
    sa1 = savingsAccount("Marc", "1234", 6.50)
    print(sa1)
    print(sa1.getBalance())
    print(sa1.getName())
    print(sa1.getPin())
    sa1.deposit(1234.76)
    sa1.deposit(1852.86)
    print(sa1.getBalance())
    print(sa1.computeInterest())