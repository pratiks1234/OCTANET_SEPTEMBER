class ATM:
    def __init__(self):
        self.users = {
            "user1": {"pin": "1234", "balance": 1000, "transactions": []},
            "user2": {"pin": "5678", "balance": 1500, "transactions": []}
        }
        self.current_user = None

    def authenticate_user(self):
        user_id = input("Enter your user ID: ")
        pin = input("Enter your PIN: ")
        
        if user_id in self.users and self.users[user_id]["pin"] == pin:
            self.current_user = user_id
            print("Authentication successful.")
        else:
            print("Authentication failed. Please check your user ID and PIN.")

    def main_menu(self):
        while self.current_user is not None:
            print("\nMain Menu:")
            print("1. Transactions History")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Transfer")
            print("5. Quit")

            choice = input("Select an option: ")

            if choice == "1":
                self.show_transaction_history()
            elif choice == "2":
                amount = float(input("Enter the withdrawal amount: "))
                self.withdraw(amount)
            elif choice == "3":
                amount = float(input("Enter the deposit amount: "))
                self.deposit(amount)
            elif choice == "4":
                recipient_account = input("Enter the recipient's user ID: ")
                amount = float(input("Enter the transfer amount: "))
                self.transfer(recipient_account, amount)
            elif choice == "5":
                self.quit()
            else:
                print("Invalid choice. Please select a valid option.")

    def show_transaction_history(self):
        if self.current_user is not None:
            transactions = self.users[self.current_user]["transactions"]
            print("Transaction History:")
            for transaction in transactions:
                print(transaction)
        else:
            print("Authentication required.")

    def withdraw(self, amount):
        if self.current_user is not None:
            user = self.users[self.current_user]
            if amount > 0 and user["balance"] >= amount:
                user["balance"] -= amount
                user["transactions"].append(f"Withdraw: ${amount}")
                print(f"Withdrawal of ${amount} successful.")
            else:
                print("Invalid withdrawal amount or insufficient funds.")
        else:
            print("Authentication required.")

    def deposit(self, amount):
        if self.current_user is not None:
            user = self.users[self.current_user]
            if amount > 0:
                user["balance"] += amount
                user["transactions"].append(f"Deposit: ${amount}")
                print(f"Deposit of ${amount} successful.")
            else:
                print("Invalid deposit amount.")
        else:
            print("Authentication required.")

    def transfer(self, recipient_user_id, amount):
        if self.current_user is not None:
            if recipient_user_id in self.users:
                sender = self.users[self.current_user]
                recipient = self.users[recipient_user_id]
                if amount > 0 and sender["balance"] >= amount:
                    sender["balance"] -= amount
                    recipient["balance"] += amount
                    sender["transactions"].append(f"Transfer to {recipient_user_id}: ${amount}")
                    recipient["transactions"].append(f"Transfer from {self.current_user}: ${amount}")
                    print(f"Transfer of ${amount} to {recipient_user_id} successful.")
                else:
                    print("Invalid transfer amount or insufficient funds.")
            else:
                print("Recipient user ID not found.")
        else:
            print("Authentication required.")

    def quit(self):
        print("Thank you for using our ATM. Have a great day!")
        self.current_user = None

if __name__ == "__main__":
    atm = ATM()
    atm.authenticate_user()
    atm.main_menu()
