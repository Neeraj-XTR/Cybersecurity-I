import hashlib
import getpass

password_list = {}
def create_password():
    username = input("Username: ")
    password = getpass.getpass('Enter your password: ')
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    password_list[username] = hashed_password
    print("Your account is created")

def login():
    username = input("Username: ")
    password = getpass.getpass('Enter your password: ')
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in password_list.keys() and password_list[username] == hashed_password:
        print("Login successful")
    else:
        print("Kal ana mittr")

def main():
    while True:
        choice = input("Would you like to create a new password? (y/n): ")
        if choice == "y":
            create_password()
        elif choice == "n":
            login()
        elif choice == "q":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
