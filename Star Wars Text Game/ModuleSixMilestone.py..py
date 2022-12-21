#Dayton Dunphy

#The dictionary links a room to other rooms.
rooms = {
        "Cell Block 1": {"South": "Cell Block 2", "Exit": "exit"},
        "Cell Block 2": {"West": "Control Room", "North": "Cell Block 1", "Exit": "exit"},
        "Control Room": {"North": "Flight Deck", "East": "Cell Block 2", "South": "Cell Block 4",
        "West": "Darth Vader's Private Chambers", "Exit": "exit"},
        "Cell Block 4": {"North": "Control Room", "East": "Cell Block 3", "Exit": "exit"},
        "Cell Block 3": {"West": "Cell Block 4", "Exit": "exit"},
        "Darth Vader's Private Chambers": {"East": "Control Room", "Exit": "exit"},
        "Flight Deck": {"East": "Cell Block 5", "South": "Control Room", "Exit": "exit"},
        "Cell Block 5": {"West": "Flight Deck", "Exit": "exit"},
        "Exit": {"Exit": "exit"}
    }

#Opening statements and header
print()
print("Star Wars Adventure Game")
print("-" * 25)
print()
print("You are currently in Cell Block 1.")

#Initialization of vairables
move = ""
cur_room = "Cell Block 1"
valid_moves = ["North", "South", "East", "West", "Exit"]

#While loop to move between rooms and exit game
while move != 'Exit':
    move = input("Enter 'go' and the direction of your move. (ex: go north): ")
    move = move.lower()      #treats upper case and lower case commands the same.
    if move == "exit":
        cur_room = "Exit"
        break
    move_lst = move.split()
    command, direction = move_lst[0], move_lst[1]
    direction = direction.title()

    if direction in valid_moves:
        if direction in rooms[cur_room]:
            cur_room = rooms[cur_room][direction]
            if cur_room == "Control Room":
                print("You are now in the", cur_room + ".")
            elif cur_room == "Flight Deck":
                print("You are now on the", cur_room + ".")
            else:
                print("Your are now in", cur_room + ".")
        else:
            print("You can't go that direction from this room")
    else:
        print("That is not a valid command")

#Statement prints after exit command.
print()
print("Thank you for playing.")
