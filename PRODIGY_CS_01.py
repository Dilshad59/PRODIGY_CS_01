'''
Task-01
Implement Caesar Cipher
Create a Python program that can encrypt and decrypt text using the Caesar Cipher algorithm. 
Allow users to input a message and a shift value to perform encryption and decryption.

'''
def caesar_cipher(text, shift, encrypt=True):
    """
    Encrypt or decrypt a message using the Caesar cipher.
    :text: The input message to encrypt or decrypt
    :shift: The number of positions to shift each letter
    :encrypt: Boolean indicating whether to encrypt or decrypt
    :return: The encrypted or decrypted message
    """
    if not encrypt:
        shift = -shift
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def main():
    """
    Main function to handle user input for encryption and decryption.
    """
    while True:
        choice = input("Do you want to encrypt or decrypt a message (Enter 'encrypt' or 'decrypt', or 'exit' to quit): ").strip().lower()
        
        if choice == 'exit':
            print("Bye...")
            break
        elif choice not in ['encrypt', 'decrypt']:
            print("Invalid choice! Please enter 'encrypt' or 'decrypt'.")
            continue

        message = input("Enter your message: ").strip()
        
        while True:
            try:
                shift = int(input("Enter the shift value (a number): ").strip())
                break
            except ValueError:
                print("Invalid number! Please enter a valid number.")

        result_message = caesar_cipher(message, shift, encrypt=(choice == 'encrypt'))
        action = "Encrypted" if choice == 'encrypt' else "Decrypted"
        print(f"{action} message: {result_message}")

if __name__ == "__main__":
    main()
