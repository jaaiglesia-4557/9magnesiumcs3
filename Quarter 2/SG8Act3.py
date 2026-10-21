#initialize the class and set its attributes and methods
class BankAccount:
    def __init__(self, account_number, balance):
        # Private attributes
        self.__account_number = account_number
        self.__balance = balance

    #Public Setter Methods - Sets/Assigns values for the attributes
    def set_account_number(self, account_number):
        self.__account_number = account_number

    def set_balance(self, balance):
        #Input validation; checks whether balance is zero or positive
        if balance >= 0:
            self.__balance = balance
        else:
            print("The balance must be not be a negative number.")

    #Public Getter Methods - Returns the value of the attributes
    #Using @property allows us to access these like attributes (e.g., a1.balance)
    @property
    def account_number(self):
        return self.__account_number

    @property
    def balance(self):
        return self.__balance

print("Sample Output")

# 1. The required object from the instructions
a1 = BankAccount(12345, 1000)
print(f"a1 = BankAccount({a1.account_number}, {a1.balance:.2f})\n")

# 2. Display initial info
print("Output:\n")
print("Account 1")
print(f"Account Number: {a1.account_number}")
print(f"Balance: {a1.balance:.2f}\n")

# 3. Test the negative balance validation
print("Update balance to -100")
a1.set_balance(-100) # This will trigger the warning
print(f"Account Number: {a1.account_number}")
print(f"Balance: {a1.balance:.2f}\n")


