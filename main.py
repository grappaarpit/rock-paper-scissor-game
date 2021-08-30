rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
def ask_user():
  user_choice = int(input("Choose 1 for rock,2 for paper, 3 for scissors"))

  return(user_choice)

def ask_computer():
  computer_choice = random.randint(0,2)
  return(computer_choice)

def decide_game(user_choice, computer_choice):

  if user_choice==options[0]:
    if computer_choice==options[0]:
      winner = 0
    if computer_choice==options[1]:
      winner = 1
    if computer_choice==options[2]:
      winner = 2

  elif user_choice==options[1]:
    if computer_choice==options[0]:
      winner = 2
    if computer_choice==options[1]:
      winner = 0
    if computer_choice==options[2]:
      winner = 1


  elif user_choice==options[2]:
    if computer_choice==options[0]:
      winner = 1
    if computer_choice==options[1]:
      winner = 2
    if computer_choice==options[2]:
      winner = 0

  return(winner)



options = [rock,paper,scissors]
winner = 0
while (winner==0):
  user_choice = options[ask_user()-1]
  computer_choice = options[ask_computer()]

  winner = decide_game(user_choice,computer_choice)

  print(f"the computer chose \n {computer_choice}")


  print(f"the user chose \n {user_choice}")

  if winner == 2:
    print("Congratulations, You win")
  elif winner == 1:
    print("Better Luck next time, Computer won")
  elif winner == 0:
    print("its a tie, lets play again")
