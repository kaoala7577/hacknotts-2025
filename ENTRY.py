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

logger = LOGGER()
fileHandler  = FileHandler(logger)

char = Player(fileHandler, logger)
time.sleep(4)
print("\nWelcome, Adventurer! Please select one of the following options to begin:\n")

mResponse = callInputNumeric(("Select an existing player file", "Create a new game"))

mapSize = 10

if mResponse == 1:
    print("Not yet implemented, defaulting to option 2. sorry!")
    
elif mResponse == 2:
    selectedSeed = input("\nPlease enter game seed, or leave blank to gain a random seed:")
    if selectedSeed == "":
        selectedSeed = random.randint(1, 4000000)
    random.seed(selectedSeed)
    answer = ""
    while True:
        print(f"\nMAP SIZE: {mapSize}\n")

        answer = input("change map size? (Y/N)").upper()
        if answer != "Y" and answer != "N":
            print("That is not a valid option!")
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


    print(f"Selected seed: {selectedSeed}.")
    print(f"Map size: {mapSize}.\n\n")
    time.sleep(3)
    clearScreen()
    print("Generating Map...")

    #==============================================================================
    ##Create the player character


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

    char.setName(valid)

gameMap = Map(size=mapSize)
gameMap.display_map(False)
clearScreen()
time.sleep(2)

musicEngine = MusicPlayer()
musicPlayer = threading.Thread(target=musicEngine.musicPlayer, daemon=True)
musicPlayer.start()


#=============================================================================
##Game Reset
if mResponse == 2:
    char.setHealth(10)
    char.setGold(10)
    char.setLocationY(0)
    for x in gameMap.map_grid[0]:
        if x != None:
            char.setLocationX(gameMap.map_grid[0].index(x))

gameLoopRuns = True
while gameLoopRuns:
    mTravelOptions = constructDirection(gameMap.getMapTypeByLocation(char))

    print(f"{char} enters the room.")

    mCell = gameMap.getCellByTileLocation(char)
    if mCell.encounter != None:
        print("I have an encounter too!")

    result = callInputNumeric(mTravelOptions)
    initialLocX = char.getLocationX()
    initialLocY = char.getLocationY()
    if result == 1:
        char.setLocationY(initialLocY+1)
    elif result == 2:
        char.setLocationX(initialLocX+1)
    elif result == 3:
        char.setLocationY(initialLocY-1)
    elif result == 4:
        char.setLocationX(initialLocX-1)
        
    #Okay this is accurate, the generation is off.
    if gameMap.getMapTypeByLocation(char) == None:
        print("\nUnfortunately that way has been blocked.\n")
        char.setLocationX(initialLocX)
        char.setLocationY(initialLocY)
        
    ##Draw location scene

    ##Present options

    ##Respond to player option

musicEngine.musicSilence()
musicEngine.complete()
logger.log(None, "CLOSE")
musicPlayer.join()
