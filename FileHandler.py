##File handler
from LOGGER import *

FILE_READ = 0
FILE_WRITE = 1
FILE_WRITE_BYTES = 2
#Handle created by the file handler

class FileHandle():
    def __init__(self, ID):
        self.ID = ID
        self.status = "CLOSED"
        self.name = ""
        self.file = None

    def openFile(self, mFileName, mode):
        if mode == 0:
            self.file = open(mFileName, "r")
            self.status = "READ"
        if mode == 1:
            self.file = open(mFileName, "w")
            self.status = "WRITE"
        if mode == 2:
            self.file = open(mDileName, "wb")
            self.status = "WRITE"

    def closeFile(self):
        if self.status != "CLOSED":
            self.file.close()
            self.status = "CLOSED"

    def writeData(self, info):
        self.file.write(info)
    
class FileHandler():

    def __init__(self, logger):
        self.logger = logger
        self.handles = []
        self.handleFormat = "File_"
        self.fileCount = 0

    def getHandleByName(self, name):
        for handle in handles:
            if handle.name == name:
                return handle
        return None

    def createFile(self, mFileName):
        mHandle = None
        for handle in self.handles:
            if handle.status != "READ" and handle.status != "WRITE":
                mHandle = handle
        if mHandle == None:
            mHandle = FileHandle(self.handleFormat+str(self.fileCount))
            self.fileCount += 1
        try:
            file = open(mFileName, "r")
            file.close()
            self.logger.log(f"Attempted to create file {mFileName}. File already exists." , "ERROR")
            return
        except OSError:
            mHandle.file = open(mFileName, "w")
            mHandle.status = "WRITE"
            self.logger.log(f"Created file '{mFileName}' successfully!", "SUCCESS")
            return mHandle
        
    def openFile(self, mFileName, mode):
        try:
            mHandle = None
            for handle in self.handles:
                if handle.status != "READ" and handle.status != "WRITE":
                    mHandle = handle
            if mHandle == None:
                mHandle = FileHandle(self.handleFormat+str(self.fileCount))
                self.fileCount += 1
                mHandle.openFile(mFileName, mode)
        except Exception as e:
            raise e
            self.logger.log(f"Failed to open file: {mFileName}", "ERROR") 
        except Exception as e:
            self.logger.log(f"Unknown error occurred when opening a file {e}", "ERROR")
        return mHandle

    def closeFile(self, pFileHandle):
        try:
            pFileHandle.closeFile()
        except OSError:
            self.logger.log(f"Failed to close file with handle {pFileHandle.name}", "ERROR")
        except Exception as e:
            self.logger.log(f"Unknown error occurred when opening a file {e}", "ERROR")


    def readData(self, handle):
        return handle.file.read()


    def writeData(self, handle, info):
        handle.writeData(info)
