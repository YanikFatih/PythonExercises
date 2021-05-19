from random import randint #to roll the dices randomly, we should import randint from random

first_roll = int(input("Welcome to Craps Game! Enter 1 to roll the dices."))
#prompts the user to enter 1 to roll the dices
if first_roll == 1:
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    # to roll the dices as they have 6 faces, we use randint from 1 to 6
else:
    print("The game did not start. Enter 1 to start.")

sum = dice1 + dice2 # add the dices values to each other and keeps them in sum variable

if sum == 7 or sum == 11:
    print(f"Sum of the dices is {sum}. You won on the first throw, congratulations!")
elif sum == 2 or sum == 3 or sum == 12:
    print(f"Sum of the dices is {sum}. You lost!")
    #firstly, program checks the first throw for conditions that makes the user win or lose
    #if user makes a point (dices sum is 4,5,6,8,9 or 10), else statement starts to work
else:
    point = sum
    print(f"Sum of the dices is {sum}. {point} is your point. Roll the dices to make your point.")
    #if user did not win or lose on the first throw, informs the user about the point value

    while sum != 7:
        roll = int(input("Press 1 to roll the dices again..."))
        if roll == 1:
            dice1 = randint(1,6)
            dice2 = randint(1,6)
            sum = dice1 + dice2
            #throwing dices and keep sum of them as we've done before
            print(f"Dice 1 = {dice1} , Dice 2 = {dice2} , sum of the dices = {sum}")
            #informs the user about dices values and their sum    
            if sum == point:
                print(f"Sum of the dices is  {sum}, you made your point. You won!")
                #if user makes the point again, wins 
            else:
                print("-----------------------")
        else:
            print("Invalid value! Enter 1 to roll the dices...")
    
    print(f"The sum of the dices is {sum}. You lost!") #when sum of dices is 7, while loop ends and user loses
