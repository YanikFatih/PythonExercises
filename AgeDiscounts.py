age = int(input("Enter your age to check whether you are qualified for any discount or not? : "))
#taking the user's age as an input
if age <= 19:
    print("You are qualified for student discounts.")
    #if the user is younger than 20, informs the user about qualified for student discounts
elif age >= 65:
    print("You can recieve senior discounts.")
    #if the user is older than 64, informs the user about qualified for senior discounts
else:
    print("You qualify for no age discounts.")
    #if the user is between 19 and 65, else block works and informs the user for no age discount
