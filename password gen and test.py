import secrets
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    if length < 12:
        raise ValueError("Password length should be at least 12 characters for strong security.")

    # Character sets
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Ensure password contains at least one of each character type
    password = [
        secrets.choice(letters.upper()),  # Ensure at least one uppercase letter
        secrets.choice(letters.lower()),  # Ensure at least one lowercase letter
        secrets.choice(digits),           # Ensure at least one digit
        secrets.choice(symbols)           # Ensure at least one special character
    ]

    # Fill the rest of the password length with random characters
    password += [secrets.choice(letters + digits + symbols) for _ in range(length - 4)]
    
    # Shuffle the password list to ensure randomness
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)

def test_password(password):
    if len(password) < 12:
        return "Weak: Password should be at least 12 characters long."

    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_number = any(char.isdigit() for char in password)
    has_special_character = any(char in string.punctuation for char in password)
    common_patterns = ["1234", "password", "abcd", "qwerty", "admin"]

    if any(pattern in password.lower() for pattern in common_patterns):
        return "Weak: Password contains common sequences or words."

    if has_uppercase and has_lowercase and has_number and has_special_character:
        return "Strong: Password contains a good mix of character types."
    else:
        missing_types = []
        if not has_uppercase:
            missing_types.append("uppercase")
        if not has_lowercase:
            missing_types.append("lowercase")
        if not has_number:
            missing_types.append("digit")
        if not has_special_character:
            missing_types.append("special character")
        return f"Weak: Password is missing {', '.join(missing_types)}."

# GUI functions
def generate_password_gui():
    try:
        length = int(password_length_entry.get())
        password = generate_password(length)
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        strength_label.config(text="")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def test_password_gui():
    password = password_entry.get()
    if password:
        strength = test_password(password)
        strength_label.config(text=f"Strength: {strength}")
    else:
        messagebox.showwarning("Warning", "Please enter a password to test.")

# Setting up the GUI
root = tk.Tk()
root.title("Secure Password Generator & Tester")

# Labels and entries
tk.Label(root, text="Password Length (min 12):").grid(row=0, column=0, padx=10, pady=10)
password_length_entry = tk.Entry(root)
password_length_entry.grid(row=0, column=1, padx=10, pady=10)
password_length_entry.insert(0, "12")  # Default length

tk.Label(root, text="Generated Password:").grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, width=30)
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Buttons
generate_button = tk.Button(root, text="Generate Password", command=generate_password_gui)
generate_button.grid(row=2, column=0, columnspan=2, pady=10)

check_button = tk.Button(root, text="Test Password Strength", command=test_password_gui)
check_button.grid(row=3, column=0, columnspan=2, pady=10)

# Strength label
strength_label = tk.Label(root, text="")
strength_label.grid(row=4, column=0, columnspan=2, pady=10)

# Run the GUI event loop
root.mainloop()
