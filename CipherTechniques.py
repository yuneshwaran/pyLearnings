import random

def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def atbash_encrypt(text):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr(219 - ord(char))
            elif char.isupper():
                encrypted_text += chr(155 - ord(char))
        else:
            encrypted_text += char
    return encrypted_text

def atbash_decrypt(text):
    return atbash_encrypt(text)

def rail_fence_encrypt(text, rails):
    encrypted_text = ""
    for i in range(rails):
        encrypted_text += text[i::rails]
    return encrypted_text

def rail_fence_decrypt(text, rails):
    decrypted_text = [''] * len(text)
    index = 0
    for i in range(rails):
        j = i
        while j < len(text):
            decrypted_text[j] = text[index]
            index += 1
            j += rails
    return ''.join(decrypted_text)

def simple_substitution_encrypt(text, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shuffled_alphabet = list(alphabet)
    random.shuffle(shuffled_alphabet)
    encryption_table = dict(zip(alphabet, shuffled_alphabet))

    encrypted_text = ""
    for char in text.upper():
        if char.isalpha():
            encrypted_text += encryption_table[char]
        else:
            encrypted_text += char
    return encrypted_text

def simple_substitution_decrypt(text, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    decryption_table = dict((v, k) for k, v in key.items())

    decrypted_text = ""
    for char in text.upper():
        if char.isalpha():
            decrypted_text += decryption_table[char]
        else:
            decrypted_text += char
    return decrypted_text

def menu():
    print("Choose an option:")
    print("1. Encrypt with Caesar Cipher")
    print("2. Decrypt with Caesar Cipher")
    print("3. Encrypt with Atbash Cipher")
    print("4. Decrypt with Atbash Cipher")
    print("5. Encrypt with Rail Fence Cipher")
    print("6. Decrypt with Rail Fence Cipher")
    print("7. Encrypt with Simple Substitution Cipher")
    print("8. Decrypt with Simple Substitution Cipher")
    print("9. Exit")

def main():
    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            plaintext = input("Enter text to encrypt: ")
            shift = int(input("Enter the shift: "))
            encrypted_text = caesar_encrypt(plaintext, shift)
            print("Encrypted text:", encrypted_text)
            input("Press Enter to continue...")

        elif choice == '2':
            ciphertext = input("Enter text to decrypt: ")
            shift = int(input("Enter the shift: "))
            decrypted_text = caesar_decrypt(ciphertext, shift)
            print("Decrypted text:", decrypted_text)
            input("Press Enter to continue...")

        elif choice == '3':
            plaintext = input("Enter text to encrypt: ")
            encrypted_text = atbash_encrypt(plaintext)
            print("Encrypted text:", encrypted_text)
            input("Press Enter to continue...")

        elif choice == '4':
            ciphertext = input("Enter text to decrypt: ")
            decrypted_text = atbash_decrypt(ciphertext)
            print("Decrypted text:", decrypted_text)
            input("Press Enter to continue...")

        elif choice == '5':
            plaintext = input("Enter text to encrypt: ")
            rails = int(input("Enter the number of rails: "))
            encrypted_text = rail_fence_encrypt(plaintext, rails)
            print("Encrypted text:", encrypted_text)
            input("Press Enter to continue...")

        elif choice == '6':
            ciphertext = input("Enter text to decrypt: ")
            rails = int(input("Enter the number of rails: "))
            decrypted_text = rail_fence_decrypt(ciphertext, rails)
            print("Decrypted text:", decrypted_text)
            input("Press Enter to continue...")

        elif choice == '7':
            plaintext = input("Enter text to encrypt: ")
            encrypted_text = simple_substitution_encrypt(plaintext, None)
            print("Encrypted text:", encrypted_text)
            input("Press Enter to continue...")

        elif choice == '8':
            ciphertext = input("Enter text to decrypt: ")
            decrypted_text = simple_substitution_decrypt(ciphertext, None)
            print("Decrypted text:", decrypted_text)
            input("Press Enter to continue...")

        elif choice == '9':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
