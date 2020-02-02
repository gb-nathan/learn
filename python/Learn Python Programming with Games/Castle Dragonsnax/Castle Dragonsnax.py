print("You are in a dark room in a mysterious castle")
print("In front of you are four doors. You must choose one.")
playerChoice = input("Choose 1, 2, 3 or 4...")
if playerChoice == "1":
    print("You find a room full of treasure. You're rich!")
    print("GAME OVER. YOU WIN!")
elif playerChoice == "2":
    print("The door opens and an angry ogre hits you with his club.")
    print("GAME OVER. YOU LOSE!")
elif playerChoice == "3":
    print("You go into the room and find a sleeping dragon.")
    print("You can either:")
    print("1) Try to steal the dragon's gold.")
    print("2) Try to sneak around the dragon to the exit.")
    dragonChoice =
else:
    print("Sorry, you didn't enter 1, 2 or 3!")
print("Run the game again to have another go!")