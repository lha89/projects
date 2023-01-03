# The purpose of this code is to produce a password generator

# Import modules
import secrets, string

# Define the data
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

final_pwd = letters + numbers + symbols

# Define password length
pwd_length = 10

# Generate a password
pwd = ''
for i in range(pwd_length):
    pwd += ''.join(secrets.choice(final_pwd))

print(pwd)

# Ensure that restrictions apply
while True:
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(final_pwd))
        
    if (any(char in symbols for char in pwd) and
        sum(char in numbers for char in pwd) >=6):
        break

print(pwd)