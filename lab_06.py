# this is the lab_06 file
def encode(string):

    encoded_password = ""

    for i in range(0, len(string)):
        encoded_password += str(int(string[i]) + 3)

    return encoded_password


def main():

    continue_ = True

    while continue_:

        print("\nMenu")
        print("----")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")

        option = int(input("Please enter an option: "))

        if option == 1:

            password = input("Please enter your password to encode: ")
            new_pass = encode(password)
            print("Your password has been encoded and stored!")

        elif option == 2:

            print(f"The encoded password is {new_pass}, and the original password is {decode(new_pass)}.")

        elif option == 3:

            break


if __name__ == "__main__":
    main()
