import sqlite3


# This is to take the user's name to the programme
def get_user_name():
    username = str(input("Enter your name : "))  # "Sithija Nimsara"
    sqlite3.connect(f"{username}.db")


print(get_user_name())
