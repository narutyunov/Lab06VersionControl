# Nicholas Arutyunov

# Takes in an 8-digit password in string format containing only integers.
# Stores the encoded password to a new variable, with each digit being shifted up by 3 numbers.
def encode(password_to_encode):
    encoded_password = ""
    for digit in password_to_encode:
        shifted_digit = (int(digit) + 3) % 10
        encoded_password += str(shifted_digit)

    return encoded_password

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
            encode(password)
            print("Your password has been encoded and stored!")
        elif option == 3:
            exit()

