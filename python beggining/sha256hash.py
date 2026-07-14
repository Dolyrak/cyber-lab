import hashlib

def HashPassword(password):
    # Encode the password as bytes
    PasswordBytes = password.encode('utf-8')

    # Use SHA-256 hash function to create a hash object
    hashObject = hashlib.sha256(PasswordBytes)

    # Get the hexadecimal representation of the hash
    passwordHash = hashObject.hexdigest()

    return passwordHash

password = input("Input your password: ")
hashedPassword = HashPassword(password)
print(f"Your hashed passord is: {hashedPassword}")