def check_password(value):
    if len(value.strip()) > 8:
        return "The password is safe"
    else:
        return "The password is not safe"

user_input = input("Enter your password:")
print(check_password((user_input)))
