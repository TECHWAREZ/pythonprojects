import random
import string

def generate_password(length=12, uppercase=True, lowercase=True, digits=True, symbols=True):
    """Generates a random password with customizable options"""
    # Define the character sets to include in the password
    letters_upper = string.ascii_uppercase if uppercase else ''
    letters_lower = string.ascii_lowercase if lowercase else ''
    numbers = string.digits if digits else ''
    symbols = string.punctuation if symbols else ''

    # Combine the selected character sets
    characters = letters_upper + letters_lower + numbers + symbols

    # Check that at least one character set is included in the password
    if not characters:
        raise ValueError("At least one character set must be included in the password")

    # Generate the password by randomly selecting characters from the combined character set
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Example usage
password = generate_password(length=16, uppercase=True, lowercase=True, digits=True, symbols=False)
print("your new generated password is:",password)