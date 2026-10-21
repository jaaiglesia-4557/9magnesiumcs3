class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def set_account_number(self, account_number):
        raw_account_number = input("Enter the account number: ")
        try:
            account_number = str(raw_account_number)
            self.__account_number = account_number
        except ValueError:
            print("Please give a valid account number")

    def set_balance(self, balance):
        raw_balance = input("Enter the balance:")
        try:
            balance = float(raw_balance)
            if balance >= 0:
                self.__balance = balance
            else:
                print("Invalid balance, balance must be positive or zero")
        except ValueError:
            print("Please give a valid number for balance")

    def get_account_number(self):
        return self.__account_number
    def get_balance(self):
        return self.balance

    