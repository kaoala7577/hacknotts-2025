##WORKING TITLE : COURIER
from generator import *
from Player import *
import random
from Misc import *
from MusicEngine import *
from GenericInput import *

import time
import threading
import multiprocessing
import winsound

if __name__ != "__main__":
    quit()
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

time.sleep(4)
print("\nWelcome, Adventurer! Please select one of the following options to begin:\n")

mResponse = callInputNumeric(("Select an existing player file", "Create a new game"))

if mResponse == 1:
    print("Not yet implemented, defaulting to option 2. sorry!")
    
# elif mResponse == 2:

# set the seed
def set_seed(seed=0):
    selectedSeed = input("\nPlease enter game seed, or leave blank to gain a random seed: ")
    if selectedSeed == "":
        selectedSeed = seed if seed>0 else random.randint(1, 4000000)
    random.seed(selectedSeed)
    print(f"Selected seed: {selectedSeed}")

#==============================================================================
##generate the game map

def generate_map(player) -> Map:
    map_size = 10
    while True:
        print(f"\nMAP SIZE: {map_size}\n")

        answer = input("change map size? (Y/N)").upper()
        if answer != "Y" and answer != "N":
            print("That is not a valid option!")
            continue
        if answer == "Y":
            try:
                map_size = int(input("Please enter a numerical value greater than 10: "))
                if map_size < 10:
                    print("That map size is too small! Setting to 10.")
                    map_size = 10
            except:
                print("That is not a number!")
            answer = ""
        elif answer == "N":
            break

    print(f"Map size: {map_size}.\n\n")
    time.sleep(3)
    clearScreen()
    print("Generating Map...")
    return Map(player, map_size)

#==============================================================================
##Create the player character

def create_player() -> Player:
    character_name = None
    while True:
        character_name = input("Please choose a name for your character: ")
        resolve = False
        while not resolve:
            valid = input(f"\n{character_name}... Is this okay? (Y/N) ").upper()
            if valid == "Y":
                resolve = True
            elif valid == "N":
                break
            else:
                print("That is not a valid answer.")
        if resolve:
            break

    logger = LOGGER()
    file_handler = FileHandler(logger)
    player = Player(character_name, file_handler, logger)

    print(f"Welcome, {player}! Your adventure begins now...\n")
    time.sleep(3)
    clearScreen()
    return player
    
#==============================================================================
#movement
def move_player(map, player) -> Cell:
    current_cell = map.get_cell(player.row, player.col)

    valid_directions = current_cell.get_valid_directions()

    map.display_map()
    print("   ".join(valid_directions).title())

    direction = input("Where to next? ").lower()
    while direction not in valid_directions:
        print("You can't go that way!")
        direction = input("Where to next? ").lower()
        
    next_cells = map.get_pointing_cells(player.row, player.col) + map.get_pointer_cells(player.row, player.col)
    next_cells = list(dict.fromkeys(next_cells)) # remove duplicates
    new_cell = None

    if direction == 'right':
        new_cell = next(cell for cell in next_cells if cell[1] > player.col)
    elif direction == 'left':
        new_cell = next(cell for cell in next_cells if cell[1] < player.col)
    elif direction == 'up':
        new_cell = next(cell for cell in next_cells if cell[0] > player.row)
    elif direction == 'down':
        player.setRow(player.getRow()-1)
        new_cell = next(cell for cell in next_cells if cell[0] < player.row)

    player.setRow(new_cell[0])
    player.setCol(new_cell[1])
    map.visit_cell(new_cell[0], new_cell[1])
    return map.get_cell(new_cell[0], new_cell[1])

#==============================================================================
#encounters
def encounter(map, player):
    cell = map.get_cell(player.row, player.col)
    encounter = cell.encounter.encounter if cell.encounter else None
    if not encounter:
        print('\nYou reach a peaceful clearing.\n')
        return
    
    print(encounter.opening_text)
    print("I haven't implemented actual functionality yet sorry")
    try:
        
        print(encounter.closing_text)
    except:
        print("...which means this can't finish properly either")

    if cell.encounter.encounterType == "Ally":
        pass##DO ALLY STUFF
    else:
        pass##DO ENEMY STUFF


#=============================================================================
##Game Reset
def reset(map, player):
    player.setHealth(10)
    player.setGold(10)
    player.setRow(0)
    for x in map.map_grid[0]:
        if x != None:
            player.setCol(map.map_grid[0].index(x))

#=============================================================================
##Game Reset
def game_loop(map, player):
    gameLoopRuns = True
    cell = map.get_cell(player.row, player.col)
    while gameLoopRuns:
        # run cell encounter
        if cell.encounter is not None:
            encounter(map, player)
        
        # move to next cell
        cell = move_player(map, player)


def main():
    set_seed()
    player = create_player()
    map = generate_map(player)
    player.setCol(map.size // 2)

    musicEngine = MusicPlayer()
    musicPlayer = threading.Thread(target=musicEngine.musicPlayer, daemon=True)
    musicPlayer.start()

    game_loop(map, player)

    musicEngine.musicSilence()
    musicEngine.complete()
    player.logger.log(None, "CLOSE")
    musicPlayer.join()

if __name__ == "__main__":
    main()
