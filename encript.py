def OctEncrypt(data):
    """Encrypts a string using the Oct algorithm.

    Args:
        data: The string to encrypt.

    Returns:
        The encrypted string.
    """

    key = generateOctKey(data)
    encrypted_data = []
    for i in range(len(data)):
        val = ord(data[i]) + (key[i])
        encrypted_data.append(chr(val))
    return "".join(encrypted_data)

def decryptOctData(encrypted_data):
    """Decrypts a string using the Oct algorithm.

    Args:
        encrypted_data: The encrypted string.

    Returns:
        The decrypted string.
    """

    key = generateOctKey(encrypted_data)
    decrypted_data = []
    for i in range(len(encrypted_data)):
        val = ord(encrypted_data[i]) - (key[i])
        decrypted_data.append(chr(val))
    return "".join(decrypted_data)

def generateOctKey(text):
    """Generates a key for the Oct algorithm.

    Args:
        text: The string to use for generating the key.

    Returns:
        A list of integers representing the key.
    """

    key = []
    num = 0
    for c in text:
        key.append((11 - num))
        num += 2
    return key

# Example usage
decrypted_data = "Tug32218"  # Start with a decrypted string
encrypted_data = OctEncrypt(decrypted_data)
re_decrypted_data = decryptOctData(encrypted_data)

print("Encrypted data:", encrypted_data)
print("Re-decrypted data:", re_decrypted_data)