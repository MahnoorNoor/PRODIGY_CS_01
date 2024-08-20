
# Caesar Cipher with GUI

This project is an implementation of the Caesar Cipher, a simple encryption technique where each letter in a text is shifted by a certain number of positions in the alphabet. The project includes both a command-line interface and a graphical user interface (GUI) built with Tkinter.



## Features

- **Encrypt Messages:** Shift letters in a message to create an encrypted text.
- **Decrypt Messages:** Reverse the process to reveal the original message.
- **User-Friendly GUI:** Easily encrypt and decrypt messages with a simple button click.


## Project details


### 1. **caesar_cipher.py**
   This script provides a command-line interface for the Caesar Cipher.

   **Key Functions:**
   - `caesar_cipher(message, shift, mode)`: Handles the encryption and decryption logic.
   - `main()`: The entry point for running the script in the terminal.

   **How to Run:**
   - To encrypt or decrypt a message, run the script, select the mode, enter the message, and provide the shift value.
   
   

  ### 2. **caesar_cipher_GUI.py**
This script provides a graphical user interface for the Caesar Cipher using Tkinter.

**Key Functions:**

- caesar_cipher(message, shift, mode): Same encryption and decryption logic as the command-line version.
- on_encrypt(): Triggered when the "Encrypt" button is clicked.
- on_decrypt(): Triggered when the "Decrypt" button is clicked.

**How to Run:**

Run the script to open a window where you can enter your message, select the shift value, and click "Encrypt" or "Decrypt" to see the result.
 
 **Example:**

- python caesar_cipher_GUI.py

### **What I Learned:**

Through this project, I deepened my understanding of:

- Python Functions: Writing and organizing code into reusable blocks.

- String Manipulation: Handling and transforming text data.

- Error Handling: Using try and except to make the program user-friendly by catching and handling errors.

- Conditional Logic: Ensuring the program runs only when intended, using if __name__ == "__main__":.

- GUI Development: Creating a graphical interface that allows users to interact with the program visually, using Tkinter.

### **How to Use**

### Clone the Repository:

 git clone https://github.com/MahnoorNoor/PRODIGY_CS_01.git

### Navigate to the Project Directory:

cd PRODIGY_CS_01

### Run the Command Line Version:

python caesar_cipher.py

### Run the GUI Version:

python caesar_cipher_GUI.py



## challenges

One of the challenges I faced was understanding how to properly handle user input and ensure the program only runs in certain contexts. After exploring if __name__ == "__main__":, it all made sense!
