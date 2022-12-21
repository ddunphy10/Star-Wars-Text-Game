#Dayton Dunphy


#the dictionary links a room to other rooms.
rooms = {
    "Cell Block 1": {"South": "Cell Block 2", "item":""},
    "Cell Block 2": {"West": "Control Room", "North": "Cell Block 1", "item": "Leia"},
    "Control Room": {"North": "Flight Deck", "East": "Cell Block 2", "South": "Cell Block 4",
                     "West": "Darth Vader's Private Chambers", "item": "Saber"},
    "Cell Block 4": {"North": "Control Room", "East": "Cell Block 3", "item": "Chewbacca"},
    "Cell Block 3": {"West": "Cell Block 4", "item": "Solo"},
    "Darth Vader's Private Chambers": {"East": "Control Room", "item":""},
    "Flight Deck": {"East": "Cell Block 5", "South": "Control Room", "item": "Falcon"},
    "Cell Block 5": {"West": "Flight Deck", "item": "Yoda"},
    "Exit": {"Exit": "exit"}
}


#print a main menu and the commands
def show_instructions():
    print()
    print("Star Wars Adventure Game")
    print("-" * 25)
    print("Collect 6 items to win the game, or be defeated by Darth Vader.")
    print()
    print("Game controls:")
    print("-Move commands: go South, go North, go East, go West")
    print("-Add to Inventory: get 'item name'")
    print("-To exit game type 'exit'")
    print()


#Show the player’s status by identifying the room they are currently in, showing a list of their inventory of items,
# and displaying the item in their current room if there is one.
def show_player_status(cur_room, inventory):
    room_dict = rooms[cur_room]
    room_item = room_dict['item']
    print("Current Status:")
    if cur_room == "Control Room":
        print("You are now in the", cur_room + ".")
    elif cur_room == "Flight Deck":
        print("You are now on the", cur_room + ".")
    else:
        print("Your are now in", cur_room + ".")
    if len(room_item) != 0:
        print("You see ", room_item)

    print("Inventory: ", inventory)

def main():
    # initialization of vairables
    move = ""
    cur_room = "Cell Block 1"
    valid_moves = ["North", "South", "East", "West", "Exit", "item"]
    valid_descriptions = ["Leia", "Chewbacca", "Saber", "Solo", "Yoda", "Falcon"]
    inventory = []
    room_item = []

    show_instructions()



    #While loop to move between rooms and exit game
    while move != 'exit':
        move = input("Enter 'go' and the direction of your move, or 'get' and the name of the person or item you want "
                     "to add to your inventory. (ex: go north): ")
        move = move.lower()      #treats upper case and lower case commands the same.
        print()
        if move == "exit":
            cur_room = "Exit"
            break
        move_lst = move.split()
        if len(move_lst) >= 2:
            command, description = move_lst[0], move_lst[1]
        else:
            command = move_lst[0]
            description = ""
        description = description.title()

        if description in valid_moves:
            if description in rooms[cur_room]:
                cur_room = rooms[cur_room][description]
                show_player_status(cur_room, inventory) #shows updated player status after move complete
                print()
            else:
                print("You can't go that direction from this room")
        elif command == "get" and description in valid_descriptions:  #updates inventory
            inventory.append(description)
            print("Updated inventory:", inventory)
            rooms[cur_room]['item'] = ""     #removes item from room when added to inventory
        #elif command == ""
            #print("You did not enter anything.")
        else:
            print("That is not a valid command")
        if cur_room == "Darth Vader's Private Chambers":   #if you run into Darth Vader you  loose.
            print("Darth Vader has struck you down with his light saber!")
            break
        if len(inventory) == 6:  #once all items have been gathered you win the game
            print("Congratulations!! You have escaped the mighty wrath of Darth Vader!")
            break



    #Statement prints after exit command.
    print()
    print("Thank you for playing.")


main()
