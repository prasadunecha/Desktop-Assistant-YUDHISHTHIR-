# importing required random module
from tkinter.constants import Y 
from pyttsx3 import speak
from PBL import takeCommand


def rps():
    import random
    print("The Rules of Rock paper scissor game will be follows: \n"
        + "Rock vs paper --> paper wins \n"
        + "Rock vs scissor --> Rock wins \n"
        + "paper vs scissor --> scissor wins \n")
    while True:
        print("Now please enter your choice no. \n 1. Rock \n 2. paper \n 3. scissor \n")
        speak("Now please enter your choice no. \n 1. Rock \n 2. paper \n 3. scissor \n")
        # take the input from user
        ch = int(input("Now Your turn: "))
        while ch > 3 or ch < 1:
            ch = int(input("Enter your valid input here: "))
        if ch == 1:
            choice_name = 'Rock'
        elif ch == 2:
            choice_name = 'paper'
        else:
            choice_name = 'scissor'
        # print user given choice
            print("Your choice is: " + choice_name)
        print("\nNow its computer turn to initiate.......")
        # Computer will select randomly any number
        # among values 1, 2 and 3. Using randint method
        # of random module
        comp_choice = random.randint(1, 3)
        # loopingwill continue until comp_choice value
        # is equal to the choice value
        while comp_choice == ch:
         comp_choice = random.randint(1, 3)
        # initialize value of the variable comp_choice_name
        # variable corresponding to the choice value
        if comp_choice == 1:
            comp_choice_name = 'Rock'
        elif comp_choice == 2:
            comp_choice_name = 'paper'
        else:
            comp_choice_name = 'scissor'
            print("So computer choice is: " + comp_choice_name)
            speak("So computer choice is: " + comp_choice_name)
        print(choice_name + " V/s " + comp_choice_name)
        speak(choice_name + " Versus " + comp_choice_name)
        # condition for winning the game
        if((ch == 1 and comp_choice == 2) or (ch == 2 and comp_choice == 1)):
        
            print ("paper wins => ", end="")
            speak ("paper wins  ")
            final_result = "paper"
        elif((ch == 1 and comp_choice == 3) or
            (ch == 3 and comp_choice == 1)):
            print("Rock wins =>", end="")
            speak("Rock wins ")
            final_result = "Rock"
        else:
            print("scissor wins =>", end="")
            speak("scissor wins ")
            final_result = "scissor"
            # Printing either user or computer wins
        if final_result == choice_name:
            print("<== You are the winner ==>")
            speak(" You are the winner ")
        else:
            print("<== Computer wins ==>")
            speak(" Computer wins ")
        print("Do you want to play again? (Y/N)")
        speak("Do you want to play again? ")
        query = takeCommand()
        ans = query
            # if user input n or N then condition is True
        if ans == 'no' or ans == 'No':
            #ans = input()
            print("\nThanks for sharing time friend...")
            speak("\nThanks for sharing time friend...")
            break
            # after exiting from the while loop
    



