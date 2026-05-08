# WAP to show the use of Loop control statements in python.
# Date: 16/02/2026
# Author: Nikhil

# 1. pass statement

for i in range(6) :
    # aaj mood nahi hai !
    pass

count = 5
while count > 0 :
    if count == 3 :
        pass
    else :
        print(count)
    count -= 1



# 2. break statement

print("-------------")

for i in range(6) :
    if i == 3 :
        break
    print(i)
print("-------------")


# while True : 
#     userInput = input("Enter exit to STOP: ")
#     if userInput == 'exit' :
#         print("exited successfully!")
#         break
#     else :
#         print("Sorry! you entered ", userInput)




# 3. continue statement

print("-------------")
for i in range(5) :
    if i == 3 :
        continue
    print(i)


print("-------------")
# count = 5
# while count > 0 :
#     if count == 3 :
#         continue
#     else :
#         print(count)
#     count -= 1



# Example – Print Characters of String and word of a list

name = "Python"
for i in name :
    print(i)

courses = ["CCC", "Tally", "Python", "Web Design"]
for c in courses :
    print(c)