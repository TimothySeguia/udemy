correct_password = "Python123"
name_input = input("Please input a name: ")
user_input = input("Please input a password: ")

while(user_input != correct_password):
    print("Incorrect!")
    user_input = input("Please input a password: ")
print("%s Logged in!" % name_input)