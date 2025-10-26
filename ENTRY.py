##WORKING TITLE : COURIER
from generator import Map
from Player import *
import random
from Misc import *
from MusicEngine import *


import time
import threading
import multiprocessing
import winsound

#winsound.PlaySound("TDance.wav", winsound.SND_ASYNC | winsound.SND_FILENAME)

#if __name__ == "__main__":
#    musicThread = multiprocessing.Process(target=playsound.playsound, args=("C:\\Users\\galax\\Downloads\\TPOC.mp3"))
#    musicThread.start()


print("\n"*100 +
"""=================================================================================================================================
_ _ _ _ _ _ _   _ _ _ _ _ _ _ _    _ _ _     _ _ _     _ _ _ _ _ _ _      _ _ _ _ _ _ _ _     _ _ _ _ _ _ _ _      _ _ _ _ _ _ _
|           |   |             |    |   |     |   |     |     _ _    |     |              |    |              |     |     _ _    |
|   _ _ _ _ |   |   _ _ _ _   |    |   |     |   |     |   |     |  |     |__ _     _ _ _|    |   _ _ _ _ _ _|     |   |     |  | 
|  |            |   |     |   |    |   |     |   |     |   | _ _ |  |          |   |          |   |                |   | _ _ |  |
|  |            |   |     |   |    |   |     |   |     |     _ _ _ _|          |   |          |   | _ _ _ _        |     _ _ _ _|
|  |            |   |     |   |    |   |     |   |     |   |_ _ _ _            |   |          |   _ _ _ _ _|       |   |_ _ _ _
|  | _ _ _ _    |   _ _ _ _   |    |   | _ _ |   |     |   _ _ _ _  |     _ _ _|   |_ _ _     |   | _ _ _ _ _      |   _ _ _ _  |
|           |   |             |    |             |     |   |     |  |     |             |     |              |     |   |     |  |
| _ _ _ _ _ |   | _ _ _ _ _ _ |    | _ _ _ _ _ _ |     | _ |     | _|     | _ _ _ _ _ _ |     |_ _ _ _ _ _ _ |     | _ |     | _|

=================================================================================================================================""")

# set the seed
def set_seed(seed=0):
    selectedSeed = input("Please enter game seed, or leave blank to gain a random seed: ")
    if selectedSeed == "":
        selectedSeed = seed if seed>0 else random.randint(1, 4000000)
    #setSeed(selectedSeed)
    random.seed(selectedSeed)
    print(f"Selected seed: {selectedSeed}.")

# generate the map
def generate_map():
    mapSize = 10
    while True:
        print(f"\nMAP SIZE: {mapSize}\n")

        answer = input("Change map size? (Y/N)").upper()
        if answer != "Y" and answer != "N":
            print("That is not a valid option!")
            continue
        if answer == "Y":
            try:
                mapSize = int(input("Please enter a numerical value greater than 10: "))
                if mapSize < 10:
                    print("That map size is too small!")
                    mapSize = 10
            except:
                print("That is not a number!")
            answer = ""
        elif answer == "N":
            break
    
    print(f"Map size: {mapSize}.\n\n")
    print("Generating Map...")
    time.sleep(3)
    clearScreen()
    return Map(size=mapSize)

#==============================================================================
##Create the player character

def create_player():
    characterName = None
    while True:
        characterName = input("Please choose a name for your character: ")
        resolve = False
        while not resolve:
            valid = input(f"\n{characterName}... Is this okay? (Y/N)").upper()
            if valid == "Y":
                resolve = True
            elif valid == "N":
                break
            else:
                print("That is not a valid answer.")
        if resolve:
            break

    logger = LOGGER()
    fileHandler  = FileHandler(logger)
    player = Player(name=characterName, fileHandler=fileHandler, logger=logger)

    print(f"\nWelcome, {player}! Your adventure begins now...\n")
    time.sleep(3)
    clearScreen()
    return player

#==============================================================================
#movement

def move_player(map, player):
    current_cell = map.get_cell(player.row, player.col)
    valid_directions = current_cell.get_valid_directions()
    direction = None

    map.display_map()
    print("   ".join(valid_directions).title())

    while True:
        direction = input("Where to next? ").lower()
        if direction not in valid_directions:
            print("You can't go that way!")
            continue
        break
        
    next_cells = map.get_pointing_cells(player.row, player.col)
    new_cell = None

    if direction == 'right':
        new_cell = next(cell for cell in next_cells if cell[1] > player.col)
    elif direction == 'left':
        new_cell = next(cell for cell in next_cells if cell[1] < player.col)
    elif direction == 'up':
        new_cell = next(cell for cell in next_cells if cell[0] > player.row)
    elif direction == 'down':
        new_cell = next(cell for cell in next_cells if cell[0] < player.row)

    player.setRow = new_cell[0]
    player.setCol = new_cell[1]
    map.visit_cell(new_cell[0], new_cell[1])


if __name__ == "__main__":
    set_seed()
    map = generate_map()
    player = create_player()
    player.setCol(map.size // 2)

    move_player(map, player)
