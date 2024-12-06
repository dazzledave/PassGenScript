import random
import string

def generate_password(length, use_uppercase=True, use_numbers=True, use_special_chars=True):
    if length < 4:
        raise ValueError("Password length must be at least 4 to include all character types.")

    # Character pools
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_uppercase else ""
    numbers = string.digits if use_numbers else ""
    special = string.punctuation if use_special_chars else ""

    # Ensure at least one of each selected type is included
    all_chars = lower + upper + numbers + special
    if not all_chars:
        raise ValueError("No character types selected for the password!")

    password = [
        random.choice(lower),
        random.choice(upper) if use_uppercase else "",
        random.choice(numbers) if use_numbers else "",
        random.choice(special) if use_special_chars else ""
    ]
    
    # Fill the rest of the password length with random choices from all_chars
    password += random.choices(all_chars, k=length - len(password))
    
    # Shuffle to avoid predictable patterns
    random.shuffle(password)

    return ''.join(password)

# User interaction
if __name__ == "__main__":
    print("Welcome to DazzleDave's Password Generator!")
    
    try:
        length = int(input("Enter the desired password length (minimum 4): "))
        use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == "yes"
        use_numbers = input("Include numbers? (yes/no): ").strip().lower() == "yes"
        use_special_chars = input("Include special characters? (yes/no): ").strip().lower() == "yes"

        password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
        print(f"Generated Password: {password}")
        print("Hope you like it (●'◡'●)")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")