#!/usr/bin/python3
"""Driving a simple game framework with 
   a dictionary object | Atla3 Research"""

def showInstruction():
    """Show the game instructions when called"""

    #print a main menu and the commands
    print('''
    RPG Game
    
    How to Win:
    Get to the Garden with a key and potion to win! 
    AVOID THE MONSTERS!
    ========
    Comands:
        go [direction]
        get [item]
    ''')

def showStatus():
    """determine the current status of the player"""
    #print the player's current location
    print('-------------------------')
    print('You are in the ' + currentRoom)
    #print what the player is carrying
    print('Inventory:', inventory)
    #check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("-------------------------")


# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
rooms = {
            
            'Hall' : {
                'south' : 'Kitchen',
                'east'  : 'Dining Room',
                'north' : 'Bedroom',
                'item'  : 'key'
                },

            'Kitchen' : {
                'north' : 'Hall',
                'item'  : 'monster'
                },
            'Dining Room' : {
                'west' : 'Hall',
                'south': 'Garden',
                'item' : 'potion'
                },
            'Garden' : {
                'north' : 'Dining Room',
                },
            'Bedroom' : {
                'south' : 'Hall',
                'east'  : 'Bathroom',
                'item'  : 'spiked bat'
                },
            'Bathroom' : {
                'west' : 'Bedroom',
                'item' : 'adrenaline'
                }               

        }

# start the player in the Hall
currentRoom = 'Hall'

showInstruction()

while True:
    showStatus()

    # the player MUST type something in 
    # otherwise input will keep asking
    move = ''
    while move == '':
        move = input('>')

    # normalize input:
    # .lower() makes it lower case, .split() turns it to a list 
    # therefore, "get golden key" becomes ["get", "golden key"]
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]] 
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way:')

    #if they type 'get' first
    if move[0] == 'get' :
        #make two checks:
        #1. if the current room contains an item
        #2. if the itme in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory.append(move[1])
            #display a helpful message 
            print(move[1] + 'got!')
            #delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
        #if there is no item in the room or the item doesn't match
        else:
            #tell them they can't get it 
            print('Can\'t get ' + move[1] + '!')

    # if a player enters a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        break

    # Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN')
        break

    #Define attempts to leave without items
