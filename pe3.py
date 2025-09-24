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
    message = input("Enter the message you want to encode: ").lower()
    shift = int(input("Enter your shift number: "))
    alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
    encoded_message = ""

    for ch in message:
        if ch.isalpha():
            shifted = chr(((ord(ch) - ord('a') + shift) % 26) + ord('a'))
            encoded_message += shifted
    return(alphabet, encoded_message)

def decode():
    message = input("Enter the message you want to decode: ").lower()
    shift = int(input("Enter your shift number: "))
    alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
    decoded_message = ""

    for ch in message:
        shifted = chr(((ord(ch) - ord('a') - shift) % 26) + ord('a'))
        decoded_message += shifted
    return(decoded_message)

if __name__ == "__main__":
    main()