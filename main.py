def encode(pass_word): #Constantinos Papanicolaou
    new_pass = ""
    for char in pass_word:
        new_pass += str((int(char)+3))
    return new_pass

def decode(password): #Updated push
    decoded_pass = ""
    for char in password:
        decoded_pass += str((int(char)-3))
    return decoded_pass

def main(): #main func
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()


if __name__ == "__main__":
    while True:
        main()
        option = input("Please enter an option: ")
        if option == "1":
            password = input("Please enter your password to encode: ")
            encoded_pass = encode(password)
            print("Your password has been encoded and stored!")
            print()
        if option == "2":
            decoded = decode(encoded_pass)
            print(f"The encoded password is {encoded_pass}, and the original password is {decoded}.")
            print() #added comments
        if option == "3":
            break


