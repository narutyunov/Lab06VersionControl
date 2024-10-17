# Nicholas Arutyunov

# Takes in an 8-digit password in string format containing only integers.
# Stores the encoded password to a new variable, with each digit being shifted up by 3 numbers.
def encode(password_to_encode):
    encoded_password = ""
    for digit in password_to_encode:
        shifted_digit = (int(digit) + 3) % 10
        encoded_password += str(shifted_digit)

    return encoded_password

def decode(string):
    strlist = [int(i) for i in string]
    for i, a in enumerate(strlist):
        strlist[i] = str(strlist[i] - 3)
    delimiter = ""
    decoded_password = delimiter.join(strlist)
    return decoded_password

# Main function.
if __name__ == "__main__":
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = int(input("Please enter an option: "))

        if option == 1:
            password = input("Please enter your password to encode: ")
            stored_password = encode(password)
            print("Your password has been encoded and stored!")
        elif option == 2:
            print(f"The encoded password is {stored_password}, and the original password is {decode(stored_password)}")
        elif option == 3:
            exit()

