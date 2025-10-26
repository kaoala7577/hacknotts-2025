##PLAYER CLASS
from FileHandler import *
from LOGGER import *
from Misc import *
from inventory import *

class Player():
    
    def gainItem(self, item, itemRarity=None):
        self.inventory.addItem(item, itemRarity)

    def loseItem(self, item):
        self.inventory.removeItem(item, itemRarity)

    def __init__(self, fileHandler, logger):
        self.fileHandler = fileHandler
        self.logger = logger
        self.gold = 0
        self.health = 10
        self.name = ""
        self.locX = 0
        self.locY = 0

        self.inventory = inventory()

    def __repr__(self):
        return self.name

    def setLocationX(self, locX):
        self.locX = locX

    def getLocationX(self):
        return self.locX
    
    def setLocationY(self, locY):
        self.locY = locY

    def getLocationY(self):
        return self.locY

    def setName(self, name):
        self.name = name

    def setGold(self, gold):
        self.gold = gold

    def addGold(self, goldAdd):
        self.gold += goldAdd

    def setHealth(self, health):
        self.health = health
        
    def getHealth(self):
        return self.health

    def getGold(self):
        return self.gold

    def setSeed(self, seed):
        self.seed = seed

    def getSeed(self):
        return self.seed


    ##Data generating stuff

    def genFromFile(self, mFileName):
        handle = self.fileHandler.openFile(mFileName, FILE_READ_BYTES)
        mData = self.fileHandler.readData(handle)
        hexData = []
        for x in mData:
            hexData.append(pad0s(hex(int(x)).upper()[2:], 2))

        if hexData[:4] != ["72", "79", "20", "25"]:
            self.logger.log(f"Could not import data from file {mFileName}.", "ERROR")
            return
        hexData = hexData[4:]
        nameLength = int(hexData[0], base=16)
        name = ""
        for x in range(nameLength):
            name += chr(int(hexData[x+1], base=16))
        self.setName(name)
        hexData = hexData[nameLength+1:]
        self.setHealth(int(bitJoin32(hexData[:4]), base=16))
        hexData = hexData[4:]
        self.setGold(int(bitJoin32(hexData[:4]), base=16))
        hexData = hexData[4:]
        self.setLocationX(int(bitJoin32(hexData[:4]), base=16))
        hexData = hexData[4:]
        self.setLocationY(int(bitJoin32(hexData[:4]), base=16))
        hexData = hexData[4:]
        self.setSeed(int(bitJoin32(hexData[:4]), base=16))
        hexData = hexData[4:]

    def expToFile(self, mFileName):
        handle = self.fileHandler.openFile(mFileName, FILE_WRITE_BYTES)
        hexArray = ["72", "79", "20", "25"]
        mNameSize = pad0s(hex(len(self.name)).upper()[2:], 2)
        hexArray.append(mNameSize)
        for x in self.name:
            hexArray.append(hex(ord(x)).upper()[2:])
        hexArray += bitSplit32(pad0s(hex(self.getHealth()).upper()[2:], 8))
        hexArray += bitSplit32(pad0s(hex(self.getGold()).upper()[2:], 8))
        hexArray += bitSplit32(pad0s(hex(self.getLocationX()).upper()[2:], 8))
        hexArray += bitSplit32(pad0s(hex(self.getLocationY()).upper()[2:], 8))
        hexArray += bitSplit32(pad0s(hex(self.getSeed()).upper()[2:], 8))

        for x in hexArray:
            hexArray[hexArray.index(x)] = int(x, base=16)
        self.fileHandler.writeData(handle, bytearray(hexArray))
        self.fileHandler.closeFile(handle)

    def printPlayerInfo(self):
        formString = self.name.upper() + "\n\n================\n\n"
        formString += "HEALTH: " + str(self.getHealth())+"\n"
        formString += "GOLD: " + str(self.getGold())+"\n\n================\n\nINVENTORY\n\n"
        formString += self.inventory.viewInventory()

        print(formString)
        


if __name__ == "__main__":
    dummyLogger = LOGGER()
    dummyFileHandler = FileHandler(dummyLogger)
    stevie = Player(dummyFileHandler, dummyLogger)
    stevie.setName("Stevie Wonder")
    stevie.printPlayerInfo()
