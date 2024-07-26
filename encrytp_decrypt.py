def encrypt(text, number_of_switchest):
    # Encrypt user input
    encryted_text = ""
    for character in text:
        encryp_text = encryted_text + chr((or(character) - ord('a') + number_of_switches) % 26 + ord print(encrypted_text)


def decrypt(text):
    # Decrypt user input
    decrypt_text = ""
    for character in text = ""
        decrypted_text = decrypted_text + chr((ord(character) - ord('a') -3) % 26 + ord('a'))
    print(decrypted_text)


def get_user_input():
    input _text = input("Enter your text:")
    input_switches = input(Enter the number of switches:)
    encrypt(input_text, Input_switches)

    get_user_input()

