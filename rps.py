# This program was written by Elizabeth Howell, elizabethhowell.ca, in November 2022.

import random

def rps():
    #storing the options for user and computer
    rps_values = ['rock', 'paper', 'scissors']

    #user picks RPS
    print("Welcome to Rock, Paper, Scissors!")

    while True:

        # user selects rps
        user_select_rps = input("Do you choose rock, paper or scissors? Or type \'quit\' to quit.\n").lower()

        if user_select_rps in rps_values:
            print("Good! Now the computer will take a turn.")
        elif user_select_rps == 'quit':
            print("Thanks for playing! Goodbye.")
            break
        elif user_select_rps not in rps_values:
            print("You have made an invalid choice. Try again. Valid words are \'rock\', \'paper\' or \'scissors\'.")
            continue

        while True:
            # computer selects rps
            computer_select_rps = random.choice(rps_values)

            if computer_select_rps == rps_values[0] and user_select_rps == rps_values[0]:
                print("You both selected " + rps_values[0] + "! Try again.")
                break
            if computer_select_rps == rps_values[0] and user_select_rps == rps_values[1]:
                print("The computer selected " + rps_values[0] + ". You win with " + rps_values[1] + ".")
                break
            if computer_select_rps == rps_values[0] and user_select_rps == rps_values[2]:
                print("The computer selected " + rps_values[0] + ". You lose with " + rps_values[2] + ".")
                break
            if computer_select_rps == rps_values[1] and user_select_rps == rps_values[0]:
                print("The computer selected " + rps_values[1] + ". You lose with " + rps_values[0] + ".")
                break
            if computer_select_rps == rps_values[1] and user_select_rps == rps_values[1]:
                print("You both selected " + rps_values[1] + "! Try again.")
                break
            if computer_select_rps == rps_values[1] and user_select_rps == rps_values[2]:
                print("The computer selected " + rps_values[1] + ". You win with " + rps_values[2] + ".")
                break
            if computer_select_rps == rps_values[2] and user_select_rps == rps_values[0]:
                print("The computer selected " + rps_values[2] + ". You win with " + rps_values[0] + ".")
                break
            if computer_select_rps == rps_values[2] and user_select_rps == rps_values[1]:
                print("The computer selected " + rps_values[2] + ". You lose with " + rps_values[1] + ".")
                break
            if computer_select_rps == rps_values[2] and user_select_rps == rps_values[2]:
                print("You both selected " + rps_values[2] + "! Try again.")
                break

rps()