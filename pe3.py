import datetime
import string

def encode():
    input_text = input("Enter the message you want to encode: ").lower() # Get user input and convert to lowercase
    shift = int(input("Enter your shift number: ")) # Get the shift number from the user
    alphabet = list(string.ascii_lowercase) # Create a list of the alphabet
    encoded_message = "" # initialize empty variable for the encoded message

    for ch in input_text.lower():
        if ch.isalpha(): # Check if character is a letter and skip if not
            shifted = chr(((ord(ch) - ord('a') + shift) % 26) + ord('a')) # Shift each character by the shift number
            encoded_message += shifted # append the shifted character to encoded message variable
        else:
             encoded_message += ch #keeps spaces/punctuation
    return(alphabet, encoded_message) # Return the alphabet and the encoded message

def decode():
    input_text = input("Enter the message you want to decode: ").lower() # Get user input and convert to lowercase
    shift = int(input("Enter your shift number: ")) # Get the shift number from the user
    decoded_message = "" # initialize empty variable for the decoded message

    for ch in input_text.lower():
        if ch.isalpha():
            shifted = chr(((ord(ch) - ord('a') - shift) % 26) + ord('a')) # Shift each character back by the shift number
            decoded_message += shifted # append the shifted character to decoded message variable
        else:
            decoded_message += ch #keeps spaces/punctuation
    return(decoded_message) # Return the decoded message

class BankAccount:
    def __init__(self, name = "Rainy", id = "1234", creation_date = datetime.date.today(), balance = 0):
        if creation_date > datetime.date.today():
            raise Exception("Creation date cannot be in the future.")
        self.name = name
        self.id = id
        self.creation_date = creation_date
        self.balance = balance
        
    def deposit(self, amount):
        if amount < 0:
            #raise Exception("Negative deposit amounts are not allowed.")
            return self.balance
        self.balance += amount #adding money
        print(f"Deposit was successful. New Balance: {self.balance}")
        return self.balance
    
    def withdraw(self, amount):
        if amount <= 0:
            raise Exception("Withdraw amount must be positive")
        if amount > self.balance:
            raise Exception("Withdraw denied. Insufficient funds.")
        self.balance -= amount
        print(f"New Balance:{self.balance}")
        return self.balance
    
    def view_balance(self):
        print(f"Balance: {self.balance}")
        return self.balance
        
class SavingsAccount(BankAccount):
    def __init__(self, name = "Rainy", id = "1234", creation_date = datetime.date.today(), balance = 0):
        super().__init__(name, id, creation_date, balance)
        
    def withdraw(self, amount):
        age = (datetime.date.today() - self.creation_date).days
        if age < 180:
            return self.balance
            #raise Exception("Withdrawals not permitted if account has NOT existed for more than 180 days")
        if amount <= 0 :
            return self.balance
            #raise Exception("Withdrawal was negative")
        if amount > self.balance:
            return self.balance
            #raise Exception("Insufficient funds. No overdrafts!")
        self.balance -= amount
        print(f"New Balance: {self.balance}")
        return self.balance

class CheckingAccount(BankAccount):
    def __init__(self, name = "Rainy", id = "1234", creation_date = datetime.date.today(), balance = 0):
            super().__init__(name, id, creation_date, balance)
            
    def withdraw(self, amount):
        if amount <= 0:
            raise Exception("Withdrawal amount must be positive")
            
        self.balance -= amount
        
        if self.balance < 0:
            self.balance -= 30
            print("Overdraft! a $30 fee has been applied")
            
        print(f"New Balance: {self.balance}")