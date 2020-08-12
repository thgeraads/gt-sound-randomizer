import time
import json
import binascii
import os
import shutil
from tkinter import *
import random
import psutil

username = os.getlogin()
gameDir = f"C:/Users/{username}/AppData/local/Growtopia"
isBackedUp = False

def startRandom():
    for proc in psutil.process_iter():
        if proc.name() == "growtopia.exe":
            proc.kill()
        else:
            print("bruh")
    backupRestore()
    exit()

window = Tk()
window.title("Randomizer v2")
window.geometry("300x90")
window.resizable(False, False)
window.configure(bg="#121212")

title = Label(text="Growtopia Sound Randomizer v2")
title.place(relx=0.5, rely=0.1, anchor=CENTER)
title.configure(bg="#121212", fg="white")

startButton = Button(text="Randomize!", width=40, command=startRandom)
startButton.place(relx=0.5, rely=0.35, anchor=CENTER)
startButton.configure(fg="white", bg='#2d2d2d', border="0px")

backupLabel = Label(text="Status: Not Backed Up!")
backupLabel.place(relx=0.5, rely=0.6, anchor=CENTER)
backupLabel.configure(bg="#121212", fg="#EA4335")

statusLabel = Label(text="Waiting for start...", width=50)
statusLabel.place(relx=0.5, rely=0.85, anchor=CENTER)
statusLabel.configure(bg="black", fg="#34A853")
    
def backupcheck(): # function to check if user has backed up original sound files
    global isBackedUp
    if os.path.exists(f"{gameDir}/audioBackup"):
        backupLabel.configure(text="Status: Backed Up!", fg="#34A853")
        isBackedUp = True
    else:
        backupLabel.configure(text="Status: Not Backed Up!", fg="#EA4335")
        isBackedUp = False

def backupRestore():
    global isBackedUp
    statusLabel.configure(text="Backing up original files...")
    if isBackedUp == False:
        shutil.copytree(f"{gameDir}/audio", f"{gameDir}/audioBackup")
        isBackedUp == True
    else:
        statusLabel.configure(text="Restoring original files...")
        shutil.rmtree(f"{gameDir}/audio")
        shutil.copytree(f"{gameDir}/audioBackup", f"{gameDir}/audio")
        shutil.rmtree(f"{gameDir}/audioBackup")
        statusLabel.configure(text="Backing up original files...")
        shutil.copytree(f"{gameDir}/audio", f"{gameDir}/audioBackup")
        isBackedUp == True
    backupcheck()
    statusLabel.configure(text="Backed up original files!")
    removeTemp()
    
    
def removeTemp():
    for filename in os.listdir(f"{gameDir}/audio"):
        if filename.endswith(".tmp"):
            os.remove(f"{gameDir}/audio/{filename}")
    statusLabel.configure(text="Removed temp files!")
    resetFileName()
            
def resetFileName():
    resetNumber = 0
    for filename in os.listdir(f"{gameDir}/audio"):
        if filename.endswith(".wav"):
            os.rename(f"{gameDir}/audio/{filename}", f"{gameDir}/audio/{resetNumber}.wav")
            resetNumber += 1
    randomizeNames()
    
def randomizeNames():
    nameList = ['achievement.wav', 'airy01.wav', 'airy02.wav', 'airy03.wav', 'already_used.wav', 'arrow_thwip.wav', 'baa.wav', 'baabaa.wav', 'babycry.wav', 'balloon.wav', 'barf.wav', 'beep.wav', 'belch1.wav', 'belch2.wav', 'belch3.wav', 'belch4.wav', 'bell.wav', 'bigboom.wav', 'bird3.wav', 'bleep_fail.wav', 'blip_lock.wav', 'bloop.wav', 'blorb.wav', 'boom.wav', 'boo_death.wav', 'boo_evil_laugh.wav', 'boo_ghost_be_gone.wav', 'boo_ghost_trap.wav', 'boo_pke_warning_light.wav', 'boo_power_node.wav', 'boo_proton_glove.wav', 'bubble_boil.wav', 'burn.wav', 'buster.wav', 'cant_place_tile.wav', 'cash_register.wav', 'change_clothes.wav', 'chicken.wav', 'chicken2.wav', 'choir.wav', 'ch_slash.wav', 'ch_start.wav', 'clatter.wav', 'clatter2.wav', 'click.wav', 'click_8bit.wav', 'coin_flip.wav', 'cracker_bang.wav', 'cracker_bang_2.wav', 'cumbia_horns.wav', 'death_metal_radio.wav', 'dialog_cancel.wav', 'dialog_close.wav', 'dialog_confirm.wav', 'dialog_open.wav', 'donthitme.wav', 'door_open.wav', 'door_shut.wav', 'double_chance.wav', 'droar.wav', 'drumloop.wav', 'dry_tick.wav', 'eat.wav', 'engine.wav', 'explode.wav', 'fart5.wav', 'fart6.wav', 'fight_loop.wav', 'fire.wav', 'fireball.wav', 'firework1.wav', 'firework2.wav', 'fire_pop.wav', 'flame_go.wav', 'forcefield.wav', 'fr1.wav', 'fr2.wav', 'fr3.wav', 'fr4.wav', 'fr5.wav', 'fr6.wav', 'freeze.wav', 'friend_beep.wav', 'friend_logoff.wav', 'friend_logon.wav', 'galac_mini.wav', 'gate_close.wav', 'gate_open.wav', 'gauntlet_death.wav', 'gauntlet_spawn.wav', 'gem_pickup.wav', 'getpoint.wav', 'glass_hit.wav', 'gobble.wav', 'gong.wav', 'gulp.wav', 'gunshot.wav', 'hammer_rumble.wav', 'harp.wav', 'heart.wav', 'hiss2.wav', 'hiss3.wav', 'hiss4.wav', 'hit.wav', 'hub_open.wav', 'ionic_pulse.wav', 'jack_in_the_box.wav', 'jelly_squelch.wav', 'jet_engine01.wav', 'jet_engine02.wav', 'jump.wav', 'keypad_hit.wav', 'knock.wav', 'laser.wav', 'launch.wav', 'lb_sfx1.wav', 'lb_sfx2.wav', 'levelup.wav', 'levelup2.wav', 'lightning.wav', 'lil_hiss.wav', 'loser.wav', 'love_in.wav', 'machinegun.wav', 'magic.wav', 'male_scream.wav', 'metalwingz.wav', 'metal_destroy.wav', 'metal_hit.wav', 'mlaunch.wav', 'moo.wav', 'morty_ears.wav', 'msg.wav', 'obelisk.wav', 'object_collect.wav', 'object_spawn.wav', 'object_spawn2.wav', 'oracle.wav', 'ouch.wav', 'owooooo.wav', 'page_turn.wav', 'pay_time.wav', 'peep.wav', 'piano_nice.wav', 'pinata_lasso.wav', 'pinball.wav', 'plastic_ghost.wav', 'pop.wav', 'prayer_wheel.wav', 'punch.wav', 'punch_glass.wav', 'punch_locked.wav', 'punch_miss.wav', 'punch_organic.wav', 'quack.wav', 'race_end.wav', 'race_start.wav', 'rain_loop.wav', 'ratatat.wav', 'realitytear.wav', 'reality_tear.wav', 'repair.wav', 'rock_destroy.wav', 'rock_hit.wav', 'scream.wav', 'secret.wav', 'shotgun.wav', 'shower.wav', 'siren.wav', 'sizzle.wav', 'skel.wav', 'slap.wav', 'slash.wav', 'slashquick.wav', 'slot_lose.wav', 'slot_start.wav', 'slot_win.wav', 'snd037.wav', 'spark.wav', 'spell1.wav', 'splash.wav', 'splat.wav', 'spray.wav', 'squirt.wav', 'squish.wav', 'squish_undo.wav', 'startopia_jump_thruster.wav', 'startopia_jump_thruster_hover.wav', 'startopia_tool_droid.wav', 'success.wav', 'sungate.wav', 'switch.wav', 'switch2.wav', 'swoosh.wav', 'teleport.wav', 'terraform.wav', 'thanksgiving.wav', 'thousandSlash.wav', 'thunderclap.wav', 'thwoop.wav', 'tile_created.wav', 'tile_removed.wav', 'tip_start.wav', 'toilet_flush.wav', 'trampoline.wav', 'transform.wav', 'trash.wav', 'tree_harvest.wav', 'tree_plant.wav', 'tsktsk.wav', 'twinkling_lights.wav', 'use_lock.wav', 'use_lock2.wav', 'weird_hit.wav', 'wheel.wav', 'whistle.wav', 'wind_loop.wav', 'wing_flap.wav', 'wood_break.wav', 'wood_damage.wav', 'wscream.wav']
    for filename in os.listdir(f"{gameDir}/audio"):
        if filename.endswith(".wav"):
            newName = random.choice(nameList)
            os.rename(f"{gameDir}/audio/{filename}", f"{gameDir}/audio/{newName}")
            nameList.remove(newName)
    statusLabel.configure(text="Ready to launch Growtopia!")
backupcheck()      
window.mainloop()
