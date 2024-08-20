
import tkinter as tk
from tkinter import messagebox

# Function to perform Caesar Cipher
def caesar_cipher(message, shift, mode):
    result = ""
    for char in message:
        if char.isalpha():
            shift_amount = shift if mode == "encrypt" else -shift
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - start + shift_amount) % 26 + start)
            result += new_char
        else:
            result += char
    return result

# Function triggered when the Encrypt button is clicked
def on_encrypt():
    try:
        shift = int(shift_entry.get())
        message = message_entry.get()
        encrypted_message = caesar_cipher(message, shift,    "encrypt")
        result_label.config(text=f"Encrypted: {encrypted_message}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")

# Function triggered when the Decrypt button is clicked
def on_decrypt():
    try:
        shift = int(shift_entry.get())
        message = message_entry.get()
        decrypted_message = caesar_cipher(message, shift, "decrypt")
        result_label.config(text=f"Decrypted: {decrypted_message}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")

# Create the main application window
root = tk.Tk()
root.title("Caesar Cipher GUI")
root.geometry("500x400")

# Message label and entry
message_label = tk.Label(root, text="Enter your message:")
message_label.pack(pady=10)
message_entry = tk.Entry(root, width=50)
message_entry.pack(pady=10)

# Shift label and entry
shift_label = tk.Label(root, text="Enter the shift value:")
shift_label.pack(pady=10)
shift_entry = tk.Entry(root, width=10)
shift_entry.pack(pady=10)

# Encrypt and Decrypt buttons
encrypt_button = tk.Button(root, text="Encrypt", command=on_encrypt)
encrypt_button.pack(pady=10)

decrypt_button = tk.Button(root, text="Decrypt", command=on_decrypt)
decrypt_button.pack(pady=10)

# Result label to display the output
result_label = tk.Label(root, text="")
result_label.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()