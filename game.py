# All LIbraries Installed :- 
import os 
import random

# For Continuation :- 
while True:
 choices = ["rock" , "paper" , "scissor"]
 comp_decision = random.choice(choices)

# Display The Virtual Interface :- 
 print("Welcome To The 'Rock , Paper and Scissors Game' " )
 print("1. Play The Game")
 print("2. Exit The Game")
 choice = int(input("What would you like to do ? (1/2) :- "))

# If User Wants To Play The Game :- 

 if choice == 1:
    print("What You Want To Choose ( Rock / Paper / Scissors ) :- ")
    choose = input("Enter Your Decision :- ").lower()
    if choose not in choices :
        print("Input Is Invalid .. Please Try Again ..")
    elif choose in choices :
        if comp_decision == choose :
            print("Since you both have choosen ",comp_decision,"... Its a Tie !!!")
        elif choose == "rock" and comp_decision == "scissor":
            print("Since Computer Chooses",comp_decision,"Congratulations .. You win!")
        elif choose == "paper" and comp_decision == "Rock":
            print("Since Computer Chooses",comp_decision,"Congratulations .. You Win! ")
        elif choose == "scissor" and comp_decision == "paper":
            print("Since Computer Chooses",comp_decision,"Congratulations .. You Win! ")
        else:
            print("Sorry . You Lost The Game . Try Again Later ")
    else:
       print("Sorry , It is not defined in our program . ")
    
# If User Wants To Exit The Game :- 
 elif choice == 2:
    print('Thank You for Playing .')
    print("Have a Good Day . ")
    os._exit(1)

# For An Invalid Input :- 
 else:
    print("Sorry we are not able to help you . ")
    print("Please write your query on raunakjain1002@gmail.com")
    print("Thank You .")
