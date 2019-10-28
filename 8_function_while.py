def check_password():
    while True:
        value = input("Enter your password:")
        if len(value.strip()) > 8:
            print("The password is safe")
            continue
        else:
            print("The password is not safe")
            break


check_password()