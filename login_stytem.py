user_name = input("Username: ")
password = int(input("Password: "))

if user_name == "admin" and password == 1234:
    print("Login Successful!")
else:
    print("Invalid credentials!!!")