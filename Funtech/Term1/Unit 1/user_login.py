class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        print("User registered!")


user_list = []
for i in range(1,4):
    user_list.append(User("User_{}".format(i), "Password_{}".format(i)))

for user in user_list:
    print("Username: {}\tPassword: {}".format(user.username, user.password))

while True:
    opt = input("Would you like to:\n1. Login\n2. Register\nPlease enter a number: ")
    if opt == "1":
        print("Please enter your username and password to login!")
        u_name = input("Username: ")
        u_pass = input("Password: ")

        found = False
        for user in user_list:
            if (user.username == u_name) and (user.password == u_pass):
                print("Welcome, {}".format(u_name))
                found = True
                break
        if not found:
            print("The username / password could not be found. Please try again!")
    elif opt == "2":
        print("Please enter your username / password to Register!")
        u_name = input("Username: ")
        u_pass = input("Password: ")
        user_list.append(User(u_name, u_pass))
