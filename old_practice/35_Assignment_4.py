# Solve the assignment 4 of python.
# Date: 06/02/2026
# Author: Nikhil

# 1. Limit the decimal places to 2 digits using .format method and print result, for the variable pi = 3.14159265359 
pi = 3.14159265359

print(round(pi, 2))

print("Value of pi is {:.2f}".format(pi))

print(f"{pi:.2f}")


# 2. Extract characters from index 2 to 8 with a step of 2: Given my_string = "Python Course",
#  slice characters from index 2 to 8, skipping every other char.
my_string = "Python Course"

print(my_string[2:8:2])


# 3.  Slice to get only the middle character(s): For my_string = "Madhav", use slicing to extract the middle character(s).
name = "Nikhil"
Name = "NikhilP"

def mid(word) :
    middle = int(len(word)/2)
    if len(word) % 2 == 0 :
        return word[middle-1 : middle+1]
    else :
        return word[middle]
    
print(mid(Name))


# 4. Remove the first 3 and last 3 characters: Given my_string = "Regression Analysis", remove the first 3 and last 3 characters.

my_string = "Regression Analysis"

print(my_string[3:-3])



# 5. Get the substring that starts 4 characters from the end to the last character: For my_string = "Classification",
#  slice the string starting from the 4th character from the end to the last character.

my_string = "Classification"

print(my_string[-4:])


# 6. How to Reverse a String Using Python String Methods? 
word = "Python"
print(word[::-1])


# 7. Write a Python function to check if a string is a palindrome using string methods.
word = "madam"
word2 = "madam"

if word == word[::-1] :
    print("Palindrome string")
else :
    print("not a Palindrome string")


# 8. Difference Between find() and index() in Python? 
print(Name.find('k'))   # findes index value by character, but return -1 if not found
print(Name.index('k'))   # findes index value by character, but returns error if not found


#9. Efficient String Concatenation method: Why is using join() often more efficient than using + for string concatenation in a loop?

languages = ["Python", "Java", "C++", "Javascript"]
print("_".join(languages))