#1st National Bank of Browntown Online Banking Application

#This code allows a user to make a bank account. They can set a name, 
#make withdrawals, make deposits, and check their balance
class Customer(): #This creates an object known as a customer.
    #This is an OBJECT. It has properties of Withdraw, Deposit, BalanceCheck
    def __init__ (self, name, balance = 100.00): #The customer needs a name, and are given a $100 sign-up bonus.
        self.name = name
        self.balance = balance
        print("Account made for", name, " Current Balance: $", balance) #Prints the name of the customer, and their balance.

    def withdraw(self,amount): #Creates the ability to withdraw, which removes a defined amount from your balance
        self.balance = self.balance - amount
        return self.balance
    
    def deposit(self,amount): #Creates the ability to deposit, which adds a defined amount to your balance
        self.balance = self.balance + amount
        return self.balance
    #Add the ability to deposit
    def BalanceCheck(self): #Creates the ability to check your balance, which prints the amount of money in your balance.
        return self.balance

    #Add the ability to check balance

print("Welcome to the 1st National Bank of Browntown App")
print("All new customers get $100 deposited into their account for signing up!")
print()
name = input("Let's Get Started! What is your name: ") #Sets the name from the input of the customer
customer = Customer(name)
while True: #Keeps the below code running until something stops it
    print("What would you like to do: (1) Withdraw   (2) Deposit   (3) Check Balance    (4) Log Out") #Gives the options of what to do with the bank account
    choice = input("->") #Determines what action is done

    #Withdraw
    if choice == "1":
        print("How much would you like to withdraw?")
        amount = float(input("->")) #Gives the amount to remove from the balance
        customer.withdraw(amount)
        print("You have withdrawn ", amount) #Tells the user how much they have withdrawn
        #Add a line that tells them their balance...after you have implemented balance check above
        #Add the ability to deposit
    elif choice == "2":
        print("How much would you like to deposit?")
        amount = float(input("_>")) #Gives the amount to add to the balance
        customer.deposit(amount)
        print("You have deposited ", amount) #Tells the user how much they have deposited
        pass #Delete this and replace with your code! 
        #Add the ability to check balance
    elif choice == "3":
        balance = customer.balance #Gives the balance something to be equal to
        print("Your balance is $ ",balance) #Tells the user the balance of the account
    elif choice == "4": #Additional choice added to break the above loop
        print("You have successfully logged out.") #Informs the user the code has ended
        break #Ends the code listed above
    else:
        print("You have entered an illegal value, please try again.") #An error prevention created to be used in case a value was inserted, not matching one of the four choices.
