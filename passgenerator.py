import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("Password Generator")
desired_length = int(input("Enter the desired length of the password: "))

if desired_length <= 0:
    print("Please enter a valid password length.")
else:
    password = generate_password(desired_length)
    print("Generated Password: ", password)
 # task done
