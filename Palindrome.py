text = input("Enter a text: ")
reverse_of_text = text[::-1]
#defining a varieable which is equal to reverse of the text entered by user
print("Your text = " + text)
print("Reverse of text = " + reverse_of_text)
#printing text and reverse of it to the screen

if text == reverse_of_text:
    print("This is a palindrome.") 
else:
    print("This is not a palindrome.")
    # if statement checks whether text and reverse of it are equal
    #if they are not, else block works
