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
		print("Account_balance: ", self.balance)
		return self
		
	def yield_interest(self):
		if self.balance > 0:
			self.balance = self.balance + (self.balance * self.int_rate)
		return self
			
account1 = BankAccount()
account2 = BankAccount()

account1.deposit(100).deposit(50).deposit(200).withdraw(100).yield_interest().display_account_info()

account2.deposit(300).deposit(500).withdraw(100).withdraw(200).withdraw(300).withdraw(400).yield_interest().display_account_info()

