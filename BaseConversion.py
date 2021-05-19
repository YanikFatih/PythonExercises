number = int(input("Please enter a number : "))
base = int(input("Which base you want to convert the number? : "))

if base == 2:
    converted_number = bin(number)
elif base == 8:
    converted_number = oct(number)
elif base == 16:
    converted_number = hex(number)
else:
    print("Invalid base!")
#checking the base entered by user and converts the number to the entered base
#if any undefined base entered by user, else block works and informs the user

print(f"The decimal value of {number} is {converted_number} in {base}.")
#prints the decimal number and its value in entered base
