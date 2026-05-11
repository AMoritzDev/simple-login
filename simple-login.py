correct_username = "Username"
correct_password = "Password"

username = input("Username: ")
password = input("Password: ")

while correct_username != username or correct_password != password:
    print("Username or password is incorrect")
    username = input("Username: ")
    password = input("Password: ")
print(f"Welcome {username} you successfully logged in")