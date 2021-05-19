def compare_strings(str1, str2):
    if len(str1) > len(str2):
        print(str1)
    elif len(str2) > len(str1):
        print(str2) # if and elif statements check the lentgh of string and prints the longest one
    else:
        print(str1)
        print(str2) 
        #else block works when strings have equal lentgh

string1 = input("Enter 1.string: ") #taking first string input
string2 = input("Enter 2.string: ") #taking second string input

compare_strings(string1, string2) #calling the function with strings
