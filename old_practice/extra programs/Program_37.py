# Write a Python program to find uncommon words from two Strings.
# Date : 24/02/2026
# Author : Nikhil

def uncommon_words (str1, str2) :

    words1 = set(str1.split()) 
    words2 = set(str2.split())

    uncommon_words_set = words1.symmetric_difference(words2) 

    uncommon_words_list = list(uncommon_words_set) 

    return uncommon_words_list


String1 = "This is the First String"
String2 = "This is the Second String"

uncommon = uncommon_words(String1, String2)

print("Uncommon Words: ", uncommon)