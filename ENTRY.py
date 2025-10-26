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

selectedSeed = input("Please enter game seed, or leave blank to gain a random seed:")
if selectedSeed == "":
    selectedSeed = random.randint(1, 4000000)
setSeed(selectedSeed)
answer = ""
mapSize = 10
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
gameMap = Map(size=mapSize)
visibleMap = gameMap.display_map(False)


logger = LOGGER()
fileHandler  = FileHandler(logger)

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





