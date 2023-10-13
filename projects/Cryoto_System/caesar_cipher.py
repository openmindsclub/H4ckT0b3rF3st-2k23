def caesar_cipher(text, shift, action):
    result = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.upper()
            offset = ord(char) - ord('A')
            if action == 'encrypt':
                new_offset = (offset + shift) % 26
            elif action == 'decrypt':
                new_offset = (offset - shift) % 26
            new_char = chr(ord('A') + new_offset)
            if not is_upper:
                new_char = new_char.lower()
            result += new_char
        else:
            result += char
    return result

plaintext = input("Enter the plaintext: ")
encryption_key = int(input("Enter the encryption key: "))
action = input("Encrypt or Decrypt? (Type 'encrypt' or 'decrypt'): ")

if action not in ['encrypt', 'decrypt']:
    print("Invalid action. Please type 'encrypt' or 'decrypt'.")
else:
    result = caesar_cipher(plaintext, encryption_key, action)
    print(f"Result: {result}")
