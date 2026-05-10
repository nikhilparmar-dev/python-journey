# Final Project - Password Strength Checker
# Date: 12/03/2026
# Author: Nikhil

import re


# function to check strength of an password
def check_pass_strength(password) :

    if len(password) < 8 :
        print("Weak: Your password length must be minimum 8 digits.")

    
    if not any (char.isdigit() for char in password) :
        return "Weak: Password must include at least one digit."
    

    if not any (char.isupper() for char in password) :
        return "Weak: Password must include at least one uppercase letter."
    
    if not any (char.islower() for char in password) :
        return "Weak: Password must include at least one lowercase letter."
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password) :
        return "Medium : Add special character to make password stronger"
    
    return "Strong: Your password is secure!"


def pass_checker () :

    print("Welcome to password strength checker")

    while (True) :
        password = input("\nEnter your pass or type 'exit' to quite: ")

        if password.lower() == "exit" :
            print("Thank you for using the password strength checker! good bye.")

        result = check_pass_strength(password) 
        print(result)

if __name__ == "__main__" :
    pass_checker()