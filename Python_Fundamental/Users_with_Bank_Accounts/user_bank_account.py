class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account1 = BankAccount()
        self.account2 = BankAccount()
        self.account3 = BankAccount()

    def make_deposit(self, amount, account):
        account.deposit(amount)
        return self

    def make_withdrawal(self, amount, account):
        account.withdraw(amount)
        return self

    def display_user_balance(self, account):
        if account == self.account1:
            print("Name of user: " + self.name + " -- " + "Account_1_balance: " + str(account.display_account_info()))
        elif account == self.account2:
            print("Name of user: " + self.name + " -- " + "Account_2_balance: " + str(account.display_account_info()))
        elif account == self.account3:
            print("Name of user: " + self.name + " -- " + "Account_3_balance: " + str(account.display_account_info()))
        return self
    
    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self
		
    def make_yield_interest(self, account):
        account.yield_interest()
        return self



class BankAccount:
	def __init__(self, int_rate= 0.02, balance = 0): # don't forget to add some default values for these parameters!
		self.int_rate = int_rate
		self.balance = balance
	
	def deposit(self, amount):
		self.balance += amount
		return self
		
	def withdraw(self, amount):
		if self.balance > amount: 
			self.balance -= amount
		else:
			print("Insufficient funds: Charging a ${} fee and deduct ${}".format(amount,self.balance))
		return self			
		
	def display_account_info(self):
		return self.balance
		
	def yield_interest(self):
		if self.balance > 0:
			self.balance = self.balance + (self.balance * self.int_rate)
		return self
	
user = User('Shahrazad_Masalmah', 'shahrazad@gmail.com')
user.make_deposit(500, user.account1).make_deposit(50,user.account1).make_withdrawal(150,user.account1).display_user_balance(user.account1)
user.make_deposit(500, user.account1).make_deposit(50,user.account2).make_withdrawal(150,user.account1).display_user_balance(user.account1)
user.make_deposit(500, user.account1).make_deposit(50,user.account2).make_withdrawal(150,user.account2).display_user_balance(user.account2)
user.make_deposit(200, user.account3).make_deposit(150,user.account3).make_withdrawal(120,user.account3).display_user_balance(user.account3) 
