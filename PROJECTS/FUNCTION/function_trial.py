def caesar_encrypt(text, shift):
    result = []
    for char in text:
        if char.isupper():
            result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
        elif char.islower():
            result.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
        else:
            result.append(char)
    return "".join(result)
 
 
def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)
 
 
if __name__ == "__main__":
    message = "Hello, World! This is Python."
    shift_amount = 3
 
    encrypted = caesar_encrypt(message, shift_amount)
    decrypted = caesar_decrypt(encrypted, shift_amount)
 
    print(f"Original:  {message}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")