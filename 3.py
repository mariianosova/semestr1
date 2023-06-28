class ATM:
    def __init__(self):
        self.banknotesCount = [0, 0, 0, 0, 0] 

    def deposit(self, banknotesCount):
        for i in range(5):
            self.banknotesCount[i] += banknotesCount[i]

    def withdraw(self, amount):
        withdraw_count = [0, 0, 0, 0, 0]
        remaining = amount

        for i in reversed(range(5)):
            num = min(remaining // [20, 50, 100, 200, 500][i], self.banknotesCount[i])
            withdraw_count[i] = num
            remaining -= num * [20, 50, 100, 200, 500][i]

        if remaining == 0:
            for i in range(5):
                self.banknotesCount[i] -= withdraw_count[i]
            return withdraw_count
        else:
            return [-1]

atm = ATM()

atm.deposit([0, 0, 1, 2, 1])
result = atm.withdraw(600)
print(result)  

atm.deposit([0, 1, 0, 1, 1])
result = atm.withdraw(600)
print(result)  

result = atm.withdraw(550)
print(result)
