class ATM:
    balance=1000
    def _init_(self):
        self.balance = 1000

    def check_balance(self):
        print(f"Your current balance is: {self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount:.2f}. New balance is {self.balance:.2f}.")
        else:
            print("Deposit balance must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount:.2f}. New balance is {self.balance:.2f}.")

def main():
    p= 1234
    pin=int(input("Enter the pin: "))
    if p==pin:
        atm = ATM()
    else:
        print("Invalid pin: ")
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4, change pin")
        print("5. Exit")
        
        choice = input("Select an option (1/2/3/4/5): ")

        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            atm.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            atm.withdraw(amount)
        elif choice == '4':
            print("change your pin:")
            change_pin = int(input("Enter the new pin:"))
            pin = change_pin
            
        elif choice == '5':
            print("Exiting. Thank you for using the ATM.")
            break
        else:
            print("Invalid option. Please select again.")

if __name__ == "__main__":
    main()