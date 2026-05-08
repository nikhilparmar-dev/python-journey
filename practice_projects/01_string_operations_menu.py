# Mini Project #1 - STRING OPERATIONS MENU
# Date: 09/02/2026
# Author: Nikhil


print("===== STRING OPERATIONS MENU =====")
print("1. Convert to uppercase")
print("2. Convert to lowercase")
print("3. Find Length of String")
print("4. Reverse String")
print("5. Check Palindrome")
print("6. Exit")

choice = int(input("\nEnter Your choice (1-6): "))

if choice == 1 :
    text = input("Enter a String: ")
    print("\nUppercase : ", text.upper())

elif choice == 2 :
    text = input("Enter a String: ")
    print("\nLowercase : ", text.lower())

elif choice == 3 :
    text = input("Enter a String: ")
    print("\nString Length : ", len(text), " Characters")

elif choice == 4 :
    text = input("Enter a String: ")
    print("\nReversed String : ", text[::-1])

elif choice == 5 :
    text = input("Enter a String: ")
    if text == text[::-1] :
        print("String is Palindrome.")
    else :
        print("String is not Palindrome.")

elif choice == 6 :
    print("\nProgram Exited")

else :
    print("Invalid Choice!")    
