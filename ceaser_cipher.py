
def caesar_cipher(message, shift, mode):
    # Initialize an empty string to store the resulting text
    result = ""

    # Loop through each character in the input message
    for char in message:
        # Check if the character is a letter (either uppercase or lowercase)
        if char.isalpha():
            # Determine the shift direction based on the mode (encrypt or decrypt)
            shift_amount = shift if mode == "encrypt" else -shift
            
            # Find the starting ASCII value ('A' for uppercase, 'a' for lowercase)
            start = ord('A') if char.isupper() else ord('a')
            
            # Calculate the new character using the shift and wrap around using modulo 26
            new_char = chr((ord(char) - start + shift_amount) % 26 + start)
            
            # Add the new character to the result
            result += new_char
        else:
            # If the character is not a letter, add it to the result unchanged
            result += char

    # Return the final encrypted or decrypted message
    return result

def main():
    # Print a title for the program
    print("Caesar Cipher Implementation")
    
    # Ask the user if they want to encrypt or decrypt
    mode = input("Do you want to encrypt or decrypt? (enter 'encrypt' or 'decrypt'): ").strip().lower()
    
    # Check if the user input is valid (either 'encrypt' or 'decrypt')
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode selected!")
        return
    
    # Get the message to be encrypted or decrypted from the user
    message = input("Enter the message: ").strip()
    
    try:
        # Try to convert the user's input to an integer for the shift value
        shift = int(input("Enter the shift value (integer): ").strip())
    except ValueError:
        # If the conversion fails, inform the user that the shift value must be an integer
        print("Shift value must be an integer!")
        return

    # Call the caesar_cipher function with the message, shift, and mode
    result = caesar_cipher(message, shift, mode)
    
    # Print the resulting text (either encrypted or decrypted)
    print(f"The resulting text is: {result}")

# Check if this script is being run directly (as opposed to being imported as a module)
if __name__ == "__main__":
    # Call the main function to start the program
    main()
