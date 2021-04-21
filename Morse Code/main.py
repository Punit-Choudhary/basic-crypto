# Morse code Encryter - Decrypter

# Morse code chart

morse_code_dict = {
                    'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'
}

# Encrypt
def encrypt(text):
    cipher = ''

    for letter in text:
        
        if letter != ' ':
            cipher += morse_code_dict[letter] + ' '
        
        else:
            cipher += ' '
    
    return cipher


# Decrypt
def decrypt(text):
    
    text += ' '
    decrypt_cipher = ''
    citext = ''

    for letter in text:
        if letter != ' ':
            counter = 0
            citext += letter

        else:
            # if counter = 1
            counter += 1

            # if counter = 2
            if counter == 2:
                decrypt_cipher += ' '
            else:
                # reversing the encryption
                decrypt_cipher += list(morse_code_dict.keys())[list(morse_code_dict.values()).index(citext)]
                citext = ''

    return decrypt_cipher


def main():
    print("""
        * ******************************** *
        #  Morse Code Encrypter - Decrypter #
        # ********************************* #  
        #                                   #
        #  * Type 'E' for Encryption        #
        #  * Type 'D' for Decryption        #
        #  * And nothing to exit            #
        #                                   #
        #  Developed by Punit-Choudhary     #
        * ********************************* *
         """)
    
    while True:
        choice = input("\nEnter command: ")

        if choice.lower() == 'e':
            text = input("Enter text to Encrypt:\n")

            result = encrypt(text.upper())
            print(f"Encrypted text:\n{result}")
        elif choice.lower() == 'd':
            text = input("Enter text to Decrypt:\n")

            result = decrypt(text)
            print(f"Decrypted text:\n{result}")
        else:
            print("Bye!")
            break



if __name__ == '__main__':
    main()
