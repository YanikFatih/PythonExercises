from random import randint #importing randint from random to make a choice for computer randomly 
 
 
rps = ["rock", "paper", "scissors"] #keeping the options in a list 
check_finish = 1 #define a variable to check whether user wants to play again or not 
 
 
while check_finish == 1: 
    computer_choice = rps[randint(0,2)] #to have a choie from computer randomly(rps[0] = rock, rps[1] = paper, rps[2] = scissors) 
    player_choice = input("Select -> Rock | Paper | Scissors : ") #promts the user to make a choice 
 
 
    print(f"You: {player_choice} - Computer: {computer_choice}") #prints the computer's and user's choices 
 
    if player_choice == computer_choice: 
        print("Tie") #if choices are equal, its tie. 
    elif player_choice == "rock": 
        if computer_choice == "paper": 
            print("Paper covers rock, you lose!") 
            #if user chooses rock and computers chooses paper, computer wins 
        else: 
            print("Rock crushes scissors, you win!") 
            #otherwise, computer chooses scissors and player wins 
    elif player_choice == "paper": 
        if computer_choice == "rock": 
            print("Paper covers rock, you win!") 
            #if player chooses paper and computer chooses rock, player wins 
        else: 
            print("Scissors cut paper, you lose!") 
            #otherwise, computer chooses scissors and player loses 
    elif player_choice == "scissors": 
        if computer_choice == "rock": 
            print("Rock crushes scissors, you lose!") 
            #if player chooses scissors and computer chooses rock, computer wins 
        else: 
            print("Scissors cut paper, you win!") 
            #otherwise, computer chooses paper and player wins 
     
    check_finish = int(input("Play Again(Press 1) or exit(-1) : ")) 
