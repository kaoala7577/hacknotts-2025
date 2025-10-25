##PLAYER CLASS
from FileHandler import *
from LOGGER import *


class Player():
    def __init__(self, health, gold, name, fileHandler):
        self.gold = gold
        self.health = health
        self.name = name
        self.fileHandler = fileHandler

    def __init__(self, fileHandler):
        self.fileHandler = fileHandler

    def __repr__(self):
        return self.name

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
        return gold


    def genFromFile(self, mFileName):
        handle = self.fileHandler.openFile(mFileName, FILE_READ)
        mData = bytes(self.fileHandler.readData(handle), encoding="UTF-8")

    def expToFile(self, mFileName):
        handle = self.fileHandler.openFile(mFileName, FILE_WRITE_BYTES)
        

#stevie = Player(FileHandler(LOGGER()))
#stevie.genFromFile("stevie.txt")
