# WAP to show the use of File Handling in python.
# Date: 12/03/2026
# Author: Nikhil    



# open file

file = open("example.txt", 'r')


# read file
contant = file.readline()   # reads only one line
print(contant)
print("---")
print(file.read())  # read entire data

# print(file.read())   # reads entire data in list form
file.close()



# write to a file
file = open('example2.txt', 'w')
file.write("Namaste guys,")
file.close()



# apped an file
file = open("example2.txt", 'a')
file.write("\nadded an message")
file.write("\nGood morning...")
file.close()


# closing file using with statement
with open("example2.txt", 'r') as file :
    data = file.read()
    print(data)



# exaption handling when creating a file
try :
    file = open("example2.txt", 'r')
    content = file.readline()
    print(content)
finally :
    file.close()