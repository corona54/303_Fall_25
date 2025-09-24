def main():
    print("Welcome to the Ceasar Cipher")
    choice = input("Would you like to encode or decode a message? ").lower()

    if choice == "encode":
        result = encode()
        print(result)
    elif choice == "decode":
        result = decode()
        print(result)
    else:
        print("Invalid choice. Please choose 'encode' or 'decode'.")

def encode():
    message = input("Enter the message you want to encode: ").lower() # Get user input and convert to lowercase
    shift = int(input("Enter your shift number: ")) # Get the shift number from the user
    alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)] # Create a list of the alphabet
    encoded_message = "" # initialize empty variable for the encoded message

    for ch in message:
        if ch.isalpha(): # Check if character is a letter and skip if not
            shifted = chr(((ord(ch) - ord('a') + shift) % 26) + ord('a')) # Shift each character by the shift number
            encoded_message += shifted # append the shifted character to encoded message variable
    return(alphabet, encoded_message) # Return the alphabet and the encoded message

def decode():
    message = input("Enter the message you want to decode: ").lower() # Get user input and convert to lowercase
    shift = int(input("Enter your shift number: ")) # Get the shift number from the user
    alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)] # Create a list of the alphabet
    decoded_message = "" # initialize empty variable for the decoded message

    for ch in message:
        shifted = chr(((ord(ch) - ord('a') - shift) % 26) + ord('a')) # Shift each character back by the shift number
        decoded_message += shifted # append the shifted character to decoded message variable
    return(decoded_message) # Return the decoded message

class BankAccount:
    def __init__(self, name = "Rainy", id = "1234", creation_date = datetime.date.today(), balance = 0):

# Run the main function
if __name__ == "__main__":
    main()