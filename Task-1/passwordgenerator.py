import random
import string

def generate_password(length, num_upper, num_lower, num_digits, num_symbols):
    if length < (num_upper + num_lower + num_digits + num_symbols):
        raise ValueError("Password length is too short for the specified requirements.")

    uppercase_chars = string.ascii_uppercase
    lowercase_chars = string.ascii_lowercase
    digit_chars = string.digits
    symbol_chars = string.punctuation

    password_chars = (
        random.choices(uppercase_chars, k=num_upper) +
        random.choices(lowercase_chars, k=num_lower) +
        random.choices(digit_chars, k=num_digits) +
        random.choices(symbol_chars, k=num_symbols)
    )

    remaining_length = length - (num_upper + num_lower + num_digits + num_symbols)
    all_chars = uppercase_chars + lowercase_chars + digit_chars + symbol_chars

    if remaining_length > 0:
        password_chars.extend(random.choices(all_chars, k=remaining_length))

    random.shuffle(password_chars)
    password = ''.join(password_chars)

    return password

if __name__ == "__main__":
    password_length = int(input("Enter the desired password length: "))
    num_upper = int(input("Enter the number of uppercase letters: "))
    num_lower = int(input("Enter the number of lowercase letters: "))
    num_digits = int(input("Enter the number of digits: "))
    num_symbols = int(input("Enter the number of symbols: "))

    try:
        password = generate_password(password_length, num_upper, num_lower, num_digits, num_symbols)
        print("Generated Password:", password)
    except ValueError as e:
        print(e)
