# All Libraries Installed :- 
import random
import os

# Displaying The Virtual Interface :- 
print("Welcome To The 'Rock , Paper and Scissors Game'")
print("1. Play The Game")
print("2. Exit The Game")
choice = int(input("What would you like to do ? (1/2) :- "))


while True:
# If User Don't Want To Play The Game :-
    if choice == 2:
      
      print('Thank You for Playing .')
      print("Have a Good Day . ")
      os._exit(1)

# If User Wants To Play The Game :-
    elif choice == 1:
      print("\nChoose:")
      print("1. Rock")
      print("2. Paper")
      print("3. Scissors")

      user_input = input("Enter your choice (1/2/3/): ")

      while user_input not in ['1', '2', '3']:
        user_input = input("Invalid choice. Enter 1, 2 or 3: ")

      user_choice = int(user_input)
      comp_choice = random.randint(1, 3)

      choices = {1: "Rock", 2: "Paper", 3: "Scissors"}

      user_word = choices[user_choice]
      comp_word = choices[comp_choice]

      print("You chose:", user_word)
      print("Computer chose:", comp_word)

      if user_choice == comp_choice:
        print("It's a tie!")
      elif (user_choice == 1 and comp_choice == 3) or (user_choice == 2 and comp_choice == 1) or (user_choice == 3 and comp_choice == 2):
        print("You win!")
      else:
        print("You lose!")

# For An Invalid Input :-
    else:
      print("Sorry we are not able to help you . ")
      print("Please write your query on raunakjain1002@gmail.com")
      print("Thank You .")
      os.exit(1)

# If User wants to Play Again :- 
    print("\nPlay again or exit:")
    print("1. Play Again")
    print("2. Exit")
    choice = int(input("Your choice (1/2): "))
