class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"存入 {amount} 元，当前余额为 {self.__balance} 元。")
        else:
            print("存入金额必须大于 0。")
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"取出 {amount} 元，当前余额为 {self.__balance} 元。")
        else:
            print("取出金额无效或余额不足。")

# 创建银行账户对象
account = BankAccount("123456789", 1000)
account.deposit(500)
account.withdraw(200)