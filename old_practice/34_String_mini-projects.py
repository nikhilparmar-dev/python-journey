# WAP to show the use mini projects in string.
# Date: 06/02/2026
# Author: Nikhil

name = "Nikhil"

# 1. Reverse string
print(name[::-1])

# 2. count characters
print(len(name))

# 3. check palindrome
if name == name[::-1] :
    print("Palindrome")
else :
    print("Not palindrome")

# 4. Wovel counter
# string = input("Enter a string: ")
# count = 0

# for ch in string :
#     if ch in ('aeiouAEIOU') :
#         count += 1
    
# print("Wowels : ", count)


# 5. Auto Email Masking (Privacy)
email = "nikhil123@gmail.com"

masked = email[:2] + "****" + email[email.index("@"):]

print(masked)


# 6. Count Only Vowels (No Loop)
count = name.lower().count('a') + name.lower().count('e') + name.lower().count('i') + name.lower().count('o') + name.lower().count('u')
print(count)


# 7. Password Strength Checker (Basic)
strong = strong = any(c.isupper() for c in name) and any(c.isdigit() for c in name) and len(name) >= 8
print(strong)


# 8.  Gender Check
# GENDER = input("Enter Your Gender: ")
# if GENDER == "Male" :
#     print("Hello Sir")
# else :
#     print("Hello Ma'am")


# 9. Check Uppercase or Not
# text = input("Enter Text: ")
# if text.isupper() :
#     print("All letters are uppercase")
# else :
#     print("Not all letters are uppercase")


# 10. Mobile Number Length Check
# mobile = input("Enter Mobile Number: ")

# if len(mobile) == 10 :
#     print("Valid Mobile Number!")
# else :
#     print("InValid Mobile Number!")


# 11. Name Length Checker
# name = input("Enter name: ")

# if len(name) >= 5:
#     print("Valid Name")
# else:
#     print("Name too short")