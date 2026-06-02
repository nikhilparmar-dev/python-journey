taken_usernames = ["nikhil", "admin", "python", "developer"]

username = input("Enter username: ").lower()

if username in taken_usernames:
    print("Username is already taken.")
else:
    print("Username is available.")
