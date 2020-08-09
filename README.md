# gt-sound-randomizer
A PyQt5-based GUI Program made to randomize Growtopia game sounds.

_Note: Modifying the Growtopia game files is technically illegal and might get you punished. Although its hard for the game to see that you've modified anything, I'm not responsible for anything that happens to your account/game._

# Installation

### Windows
1. Download the .exe file from the [releases tab](https://github.com/thgeraads/gt-sound-randomizer/releases).
2. Run the `randomizer.exe`file.

_If your browser/Windows SmartScreen says that this app is not safe to run, don't worry. This is because the app doesn't have a valid certificate. Click more info > run anyway. If you don't feel comfortable running the EXE, you can look into the source code yourself. Or follow the "Other OS" instructions below._


### Other OS
1. Download and install Python 3.8 (obviously).
2. Download the .py file from the [releases tab](https://github.com/thgeraads/gt-sound-randomizer/releases).
3. Run `pip3 install -r requirements.txt`.
4. Run the `randomizer.py` file.


# Usage
### Before running, **make sure that the game is closed.**
1. Before randomizing, click `Backup` to ensure that you can go back to the original sounds and wait until it says `Status: backed up.`
2. When backed up, click `Randomize!` **and wait** until the green text says `Ready to launch Growtopia`. **(this may take a few minutes!)** Then launch the game manually
3. When the game is launched, login. It will update ~90 items total. These are the modified sound files moving to the cache (You don't want these.)
4. When that's done, hit the `Clear cache folder` button. Do this every time you launch Growtopia if needed.
5. You're done! If you ever want to go back to the original sounds just click `Restore` and wait a few seconds.

This program is a bit unstable. Only click a button **once** and then just wait until you get a response.
If at any time the program stops responding, **just wait** until the window becomes responsive again. It just does that sometimes.
