import random
import string


try:
    import pyperclip
    clipboard_available = True
except ImportError:
    clipboard_available = False

def generate_password(length=12):
    if length < 4:
        print("Password length should be at  least 4.")
        return ""

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the  password length: "))
        count = int(input("Enter the number of passwords to generate: "))
    except ValueError:
        print("Please enter valid numbers .")
        return

    passwords = [generate_password(length) for _ in range(count)]

    for i, pwd in enumerate(passwords, start=1):
        print(f"Password {i}: {pwd}")

    if clipboard_available:
        copy_choice = input("Do you want to copy the first password to clipboard? (y/n): ").lower()
        if copy_choice == 'y':
            try:
                pyperclip.copy(passwords[0])
                print("The first password is copied to clipboard!")
            except Exception as e:
                print("Failed to copy to the clipboard:", e)
    else:
        print("Clipboard feature is  unavailable.Please  install pyperclip to enable it:")
        print("pip3 install pyperclip")

if __name__ == "__main__":
    main()
