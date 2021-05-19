year = int(input("Enter a year to check whether it is a leap year or not: "))
#taking the year input from the user
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"Year {year} is a leap year.") #checking the conditions for leap year
else:
    print(f"Year {year} is not a leap year.")
    #else statement works if the year is not a leap year
