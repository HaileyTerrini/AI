# Programmer: Hailey Terrini
# 3.12.24
# Program: Password Generator
# Resource: https://youtu.be/jRAAaDll34Q?si=SZq8WSYzjrmuAoIA

import hashlib

def hash_password(password, salt):
    """Hashes the password using the provided salt."""
    salted_password = password.encode() + salt.encode()
    hashed_password = hashlib.sha256(salted_password).hexdigest()
    return hashed_password

def main():
    # Accept password input from the user
    password = input("Enter your password: ")

    # Salt for hashing
    salt = "sUp3rS3cR3tS@lt"  # You can change this salt to your preference

    # Hash the password with the salt
    hashed_password = hash_password(password, salt)

    # Print the hashed password
    print("Hashed password:", hashed_password)

if __name__ == "__main__":
    main()

import hashlib
import getpass

def hash_password(password, salt):
    """Hashes the password using the provided salt."""
    salted_password = password.encode() + salt.encode()
    hashed_password = hashlib.sha256(salted_password).hexdigest()
    return hashed_password

def main():
    # Accept password input from the user without showing characters
    password = getpass.getpass("Enter your password: ")

    # Salt for hashing
    salt = "sUp3rS3cR3tS@lt"  # You can change this salt to your preference

    # Hash the password with the salt
    hashed_password = hash_password(password, salt)

    # Print the hashed password
    print("Hashed password:", hashed_password)

if __name__ == "__main__":
    main()