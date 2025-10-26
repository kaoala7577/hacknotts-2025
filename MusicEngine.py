##MUSIC PLAYER
import multiprocessing
import time
import winsound
import threading

SCAMPS_BALLAD = 0
PROPHECY_KHENEIA = 1
TORINN_DANCE = 2
THE_PROTECTOR = 3

class MusicPlayer():
    def __init__(self):
        self.MUSIC = ["DB.wav", "PoK.wav", "TDance.wav", "TP.wav"]
        self.DURATION = [93, 55, 76, 68]
        self.forceSilent = False
        self.stop = False
        self.circular = 0
        self.QUIT = False      

    def sleeper(self):
        time.sleep(self.DURATION[self.circular])
        self.silent = True
        print("OH NO")

    def musicPlayer(self):
        play=True
        while play:
            if self.forceSilent:
                time.sleep(0)
                if self.QUIT:
                    winsound.PlaySound(None, winsound.SND_ASYNC)
                    t1.terminate()
                    return
                continue
            winsound.PlaySound(self.MUSIC[self.circular], winsound.SND_ASYNC | winsound.SND_FILENAME)
            self.circular = (self.circular+1)%4
            t1 = multiprocessing.Process(target=self.sleeper)
            t1.start()
            self.silent = False
            while not self.silent:
                if self.stop:
                    winsound.PlaySound(None, winsound.SND_ASYNC)
                    t1.terminate()
                    self.stop = False
                    break
                if self.QUIT:
                    winsound.PlaySound(None, winsound.SND_ASYNC)
                    t1.terminate()
                    return
                time.sleep(0)
        print("Goodbye")
        t1.terminate()
        return 0

    def musicSilence(self):
        self.forceSilent = True
        self.musicStop()

    def musicUnsilence(self):
        self.forceSilent = False
        print("Unsilenced")
        
    def musicStop(self):
        self.stop = True

    def complete(self):
        self.QUIT = True

if __name__ == "__main__":
    mp = MusicPlayer()
    thread1 = threading.Thread(target = mp.musicPlayer)
    thread1.start()
    time.sleep(10)
    mp.musicStop()
    time.sleep(15)
    mp.musicSilence()
    time.sleep(15)
    mp.musicUnsilence()
    time.sleep(20)
    print("Done")
    mp.musicSilence()
    mp.complete()
