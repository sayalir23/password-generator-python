import random
import string

def generate_password(length):
    if length < 8:
        return "Password length should be at least 8"

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password


print("\n--- Password Generator ---")
length = int(input("Enter password length: "))
pwd = create_password(length)
print("Generated Password:", pwd)
