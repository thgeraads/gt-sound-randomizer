import os
import sys
import shutil
import random
import time
import PyQt5.QtWidgets as qtw 

isBackedUp = False

user = os.getlogin() # get username to automatically set directories
soundDir = f"C:/Users/{user}/AppData/local/Growtopia/audio"
gameDir = f"C:/Users/{user}/AppData/local/Growtopia"
nameList = [] # list of all file names

# PyQt window
class mainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Randomizer")
        self.setLayout(qtw.QVBoxLayout())
        self.setStyleSheet("background-color: #121212;")
        self.keypad()
        self.setFixedSize(400, 220)
        
    # PyQt grid layout for content
    def keypad(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())
        self.show()
            
            
        def backupcheck(): # function to check if user has backed up original sound files
            global isBackedUp
            if os.path.exists(f"{gameDir}/audioBackup"):
                self.statusText.setText("Status: Backed up.")
                self.statusText.setStyleSheet("border: 0px; color: green;")
                isBackedUp = True
                
            else:
                self.statusText.setText("Status: Not Backed up!")
                self.statusText.setStyleSheet("border: 0px; color: red;")
                isBackedUp = False
                
                
            
        def backup(): # backup function
            if isBackedUp == False:
                shutil.copytree(soundDir, f"{gameDir}/audioBackup/")
                backupcheck()
            else:
                return
            
        def restore(): # restore funciton
            if isBackedUp == False:
                print("dieke")
                self.statusText.setText = "Nothing to restore!"
            else:
                shutil.rmtree(f"{soundDir}")
                shutil.copytree(f"{gameDir}/audioBackup", soundDir)
        
        def clearCache(): # clear cache folder to prevent double game sounds
            shutil.rmtree(f"{gameDir}/cache/audio")
            
        def startRandom(): # randomization function
            self.console.setText("Starting...")
            try:
                for filename in os.listdir(soundDir):
                    time.sleep(0.1)
                    if os.path.isfile(f"{soundDir}/{filename}"):
                        if filename.endswith(".tmp"):
                            os.remove(f"{soundDir}/{filename}")
                        else:
                            nameList.append(filename)
                            self.console.setText(f"Generating {filename}...")
                time.sleep(0.5)
                self.console.setText("\n\nFile name list generated!\n\n")
            except:
                time.sleep(0.5)
                self.console.setText("\n\nSomething went wrong, please try again.\n")
                raise
            time.sleep(1.5)
            resetNumber = 0
            for file in os.listdir(soundDir):
                if os.path.isfile(f"{soundDir}/{file}"):
                    resetNumber += 1
                    os.rename(f"{soundDir}/{file}", f"{soundDir}/{resetNumber}.wav")
                    self.console.setText(f"Preparing File Name: {file}")
                time.sleep(0.5)
            self.console.setText("\Prepared file names.\n\n")
            time.sleep(1.5)
            self.console.setText("Randomizing file names...")
            for x in range(1, 222):
                newName = random.choice(nameList)
                os.rename(f"{soundDir}/{x}.wav", f"{soundDir}/{newName}")
                nameList.remove(newName)
            time.sleep(1.5)
            self.console.setText("Done!")
            time.sleep(1.5)
            self.console.setText("Ready to launch Growtopia!")
        
        # PyQt content
        textButton = qtw.QPushButton("Growtopia Sound Randomizer")
        textButton.setStyleSheet("color: white; border: 0px #1f1212; background-color: #121212")
        container.layout().addWidget(textButton, 0, 0, 1, 0)
        
        randButton = qtw.QPushButton("Randomize!", clicked=startRandom)
        randButton.setStyleSheet("color: white; background: #2d2d2d")
        container.layout().addWidget(randButton, 1, 0, 1, 0)
        
        
        backupButton = qtw.QPushButton("Backup", clicked=backup)
        backupButton.setStyleSheet("color: white; background: #2d2d2d;")
        container.layout().addWidget(backupButton, 2, 0)
        
        resetButton = qtw.QPushButton("Restore", clicked=restore)
        resetButton.setStyleSheet("color: white; background: #2d2d2d;")
        container.layout().addWidget(resetButton, 2, 1)
        
        cacheButton = qtw.QPushButton("Clear Cache Folder", clicked=clearCache)
        cacheButton.setStyleSheet("color: white; background: #2d2d2d;")
        container.layout().addWidget(cacheButton, 3, 0, 1, 0)
        
        self.statusText = qtw.QPushButton("Status: Not backed up!")
        self.statusText.setStyleSheet("border: 0px; background: #121212;")
        backupcheck()
        container.layout().addWidget(self.statusText, 4, 0, 1, 0)
        
        self.console = qtw.QTextEdit()
        self.console.setText("Waiting for start...")
        self.console.setStyleSheet("border-radius: 5px; color: #00ff00; background: #000000;")
        self.console.setMaximumHeight(60)
        self.console.setReadOnly(True)
        container.layout().addWidget(self.console, 5, 0, 1, 2)
        
        self.layout().addWidget(container) # add container to window
        
app = qtw.QApplication([])
app.setStyle('Fusion')
mw = mainWindow()
app.exec_()