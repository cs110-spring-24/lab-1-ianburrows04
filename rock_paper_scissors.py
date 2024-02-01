import random
cpu = random.randint(1, 3)

user = input("Enter rock, paper or scissors: ")

if user == "rock":
	if cpu == 1: #cpu chose rock
		print("They chose rock. Tie game.")
	elif cpu == 2: #cpu chose paper
		print("They chose paper. You lost.")
	else: #cpu chose scissors
		print("They chose scissors. You Win!")

if user == "paper":
	if cpu == 1: #cpu chose rock
		print("They chose rock, you won!")
	elif cpu == 2: #cpu chose paper
		print("They chose paper. Tie game.")
	else: #cpu chose scissors
		print("They chose scissors. You lost.")

if user == "scissors":
	if cpu == 1: #cpu chose rock
		print("They chose rock. You lost.")
	elif cpu == 2: #cpu chose paper
		print("They chose paper. You won!")
	else: #cpu chose scissors
		print("They chose scissors. Tie game.")