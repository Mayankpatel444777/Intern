import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 characters for a strong password.")
        return None
    
    #Define possible characters
    characters = string.ascii_letters + string.digits + string.punctuation

    #Ensure the password contains at least one lowercase letter, one uppercase letter, one digit, and one special character
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    #Fill the rest of the password length with random characters
    password += random.choices(characters, k=length-4)
    
    # Shuffle the resulting password list to avoid predictable patterns
    random.shuffle(password)
    
    # Join the list into a string
    return ''.join(password)

def main():
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 4:
                print("Password length should be at least 4 characters for a strong password.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    password = generate_password(length)
    if password:
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
