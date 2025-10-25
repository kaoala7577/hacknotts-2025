##File handler


FILE_READ = 0
FILE_WRITE = 1

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

    def closeFile(self):
        if self.status != "CLOSED"
            self.file.close()
            self.status = "CLOSED"
    
class FileHandler():

    def __init__(self, logger):
        self.logger = logger
        self.handles = []
        self.handleFormat = "File_"
        self.fileCount = 0

    def openFile(self, mFileName, mode):
        try:
            mHandle = None
            for handle in handles:
                if handle.status != "READ" and handle.status != "WRITE":
                    mHandle = handle
            if mHandle == None:
                mHandle = FileHandle(self.handleFormat+str(self.fileCount))
                self.fileCount += 1
                mHandle.openFile(mFileName)
        except OSError:
            self.logger.log(f"Failed to open file: {mFileName}", "ERROR") 
        except Exception as e:
            self.logger.log(f"Unknown error occurred when opening a file {e}", "ERROR")
        return mHandle

    def closeFile(self, pFileHandle):
        pFileHandle.closeFile()
