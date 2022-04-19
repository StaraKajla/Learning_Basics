import random
import time
print("Welcome to the game of ROCK, PAPER, SCISSORS!\n---RULES---\nRock beats scissors but loses to paper.")
print("Scissors beats paper but loses to rock.\nPaper beats rock but loses to scissors.")
print("If both parties select the same weapon the game will result in a draw.\n You win if you get 3 points.")
print("[ROCK = 1]\n[PAPER = 2]\n[SCISSORS = 3]")
ROCK = 1
PAPER = 2
SCISSOR = 3
play = input("Type START (start game), press any key to exit: ").lower()
start = "start"
score = 0
while start == play:
    print("Pressing 4 will exit the game!")
    weapon = input("Lets play!\n Number: ")
    if weapon == "4":
        quit()
    print("I'm thinking...")
    time.sleep(0.5)
    random_weapon = random.randint(1, 3)
    # WEAPON = ROCK
    if weapon == "1" and random_weapon == 1:
        print("You chose rock and I chose rock. DRAW!")
    if weapon == "1" and random_weapon == 2:
        print("You chose rock and I chose paper. YOU LOSE!")
        score = score - 1
    if weapon == "1" and random_weapon == 3:
        print("You chose rock and I chose scissors. YOU WIN!")
        score = score + 1
    # WEAPON = PAPER
    if weapon == "2" and random_weapon == 1:
        print("You chose paper and I chose rock. YOU WIN!")
        score = score + 1
    if weapon == "2" and random_weapon == 2:
        print("You chose paper and I chose paper. DRAW!")
    if weapon == "2" and random_weapon == 3:
        print("You chose paper and I chose scissors. YOU LOSE!")
        score = score - 1
    # WEAPON = SCISSORS
    if weapon == "3" and random_weapon == 1:
        print("You chose scissors and I chose rock. YOU LOSE!")
        score = score - 1
    if weapon == "3" and random_weapon == 2:
        print("You chose scissors and I chose paper. YOU WIN!")
        score = score + 1
    if weapon == "3" and random_weapon == 3:
        print("You chose scissors and I chose scissors. DRAW!")
    if weapon != "1" and weapon != "2" and weapon != "3" and weapon != "4":
        print("Not a valid number. Chose 1-3. Exit game = 4")
    print("Your score:", score)
    if score == 3:
        print("Congratulations you win!\nExiting game in 5 seconds")
        time.sleep(3)
        quit()
