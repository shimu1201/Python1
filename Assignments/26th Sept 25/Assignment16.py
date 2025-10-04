right_username = "Shipatel"
right_password = "12345"

username = input("Enter your username : ")
password = input("Enter your password : ")

if username == right_username:
    if password == right_password:
        print("Login Successful")
    else:
        print("Invalid Password")
else:
    print("Invalid Username")