##LOGGER

##TODO: IMPLEMENT LOGGER!

class LOGGER():
    def __init__(self):
        self.file = open("logFile.txt", "a")
        self.log(0, "INTRO")

    def log(self, message, level):
        if level =="INTRO":
            self.file.write("\nStart of new session.\n----------------\n")
        elif level == "CLOSE":
            self.file.write("----------------\nEnd of current session.\n")
            self.file.close()
        else:
            self.file.write(f"[{level}]: {message}\n")
