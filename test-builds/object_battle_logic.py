import random
import os
from time import sleep
from multiprocessing import Queue, Process

# This version of battle_logic has some major changes:
# 1. Utilises object lists. No more pesky health lists and out of bound errors!
# 2. Disables obsolete content. Will be kept in this file for legacy support,
# But will probably be removed in the full release.
# 3. Includes some super special, super cool functions made by me!
# These include: Ship making front-end, Health display(For the new object lists), and Object Cleaner(For destroyed ships)
# This is probably the best way to go about this.
# I would like to re-work the archetecture of the battle() function,
# Like making it more "callable freindly"

#Classes

class ship:

    def __init__(self, health, name, fighterDmg, bomberDmg, interceptorDmg, freighterDmg):


        self.health = health
        self.name = name
        self.fighterDmg = fighterDmg
        self.bomberDmg = bomberDmg
        self.interceptorDmg = interceptorDmg
        self.freighterDmg = freighterDmg
#Ships

# Had a startling discovery.
# Truns out, appending the object 'fighter' to the object lists means they share attributes.
# This is a big no-no, so i've resorted to creating a new object for each object list

#fighter = ship(10, "Fighter", 10, 10, 10, 10)
#
#bomber = ship(30, "Bombers", 0, 0, 0, 50)
#
#interceptor = ship(30, "Interceptor", 20, 40, 10, 10)
#
#freighter = ship(500, "Freighter", 50, 20, 40, 50)

#Enemy Ship Lists

enemyFighters = []

enemyBombers = []

enemyInterceptors = []

enemyFreighters = []

#Enemy Ship Health Lists
# Health lists are to be kept here for legacy support
enemyFightersHealth = []

enemyBombersHealth = []

enemyInterceptorsHealth = []

enemyFreightersHealth = []

#Player Ship Lists

playerFighters = []

playerBombers = []

playerInterceptors = []

playerFreighters = []

#Player Ship Health Lists
# Health lists are to be kept here for legacy support
playerFightersHealth = []

playerBombersHealth = []

playerInterceptorsHealth = []

playerFreightersHealth = []

# Simple front-end for deciding amount of ships

ships = ['Fighters', 'Bombers', 'Interceptors', 'Freighters']

print("+=====================================================+")
print("Ship Amount Config:\n")

for i in range(len(ships)):
    
    inpP = int(input("How many freindly {} do you want?:".format(ships[i])))
    inpE = int(input("How many enemy {} do you want?:".format(ships[i])))
    
    for j in range(inpP):
        if i == 0:
            playerFighters.append(ship(10, "Fighter", 10, 10, 10, 10))
        if i == 1:
            playerBombers.append(ship(30, "Bombers", 0, 0, 0, 50))
        if i == 2:
            playerInterceptors.append(ship(30, "Interceptor", 20, 40, 10, 10))
        if i == 3:
            playerFreighters.append(ship(500, "Freighter", 50, 20, 40, 50))
            
    for j in range(inpE):
        if i == 0:
            enemyFighters.append(ship(10, "Fighter", 10, 10, 10, 10))
        if i == 1:
            enemyBombers.append(ship(30, "Bombers", 0, 0, 0, 50))
        if i == 2:
            enemyInterceptors.append(ship(30, "Interceptor", 20, 40, 10, 10))
        if i == 3:
            enemyFreighters.append(ship(500, "Freighter", 50, 20, 40, 50))


def clearScreen():

    os.system('cls' if os.name == 'nt' else 'clear')
    return


def pause():

    os.system('pause')
    return

# V Funtions below this line are OBSOLETE V
#+=========================================================================+

#def healthCount():
#
#    for i in range(0, len(playerFighters)):
#
#        playerFightersHealth.append(fighter.health)
#
#    for i in range(0, len(playerBombers)):
#
#        playerBombersHealth.append(bomber.health)
#
#    for i in range(0, len(playerInterceptors)):
#
#        playerInterceptorsHealth.append(interceptor.health)
#
#    for i in range(0, len(playerFreighters)):
#
#        playerFreightersHealth.append(freighter.health)
#
#    for i in range(0, len(enemyFighters)):
#
#        enemyFightersHealth.append(fighter.health)
#
#    for i in range(0, len(enemyBombers)):
#
#        enemyBombersHealth.append(bomber.health)
#
#    for i in range(0, len(enemyInterceptors)):
#
#        enemyInterceptorsHealth.append(interceptor.health)
#
#    for i in range(0, len(enemyFreighters)):
#
#        enenmyFreightersHealth.append(freighter.health)



#def healthClear():
#
#    global enemyFightersHealth, playerFightersHealth
#
#    print(enemyFightersHealth)
#    enemyFightersHealth = [x for x in enemyFightersHealth if x > 0]
#    print(enemyFightersHealth)
#    print(playerFightersHealth)
#    playerFightersHealth = [x for x in playerFightersHealth if x > 0]
#    print(playerFightersHealth)

#+=========================================================================+
# ^ Functions above this line are OBSOLETE! ^

# This is a new method(Written by yours truely) for removing ships with no health
# This is a proff of concept idea, so it is configured for fighters only

def objectClean():
    
    # VERY BAD PRACTICE, but will be used here for proff of concept
    global playerFighters, enemyFighters, ship
    player = False
    enemy = False
    # Initial loop for deleteing
    while True:
        # Loop for player list
        
        for i in range(len(playerFighters)):
            
            if playerFighters[i].health <= 0:
                
                del playerFighters[i]
                player = False
                # THIS IS IMPORTANT!
                # This is to prevent out of bound errors.
                # The idea is that the looping of the list restarts,
                # Every time a destroyed ship is found.
                break
            
            else:

                player = True
                continue
                
        # Loop for enemy list
        
        for j in range(len(enemyFighters)):
            
            if enemyFighters[j].health <= 0:
                
                del enemyFighters[j]
                enemy = False
                # See above for more info
                break
            
            else:
                
                enemy = True
                continue
        
        # Exit condition when clean
        
        if player and enemy:
            
            # Cleaned the list, exiting
            break
        
        # Exit condition when one list empty
        
        if len(enemyFighters) == 0:
            
            #Enemy list empty, exiting
            break
        
        if len(playerFighters) == 0:
            
            #Player list empty, exiting
            break
        
        # Re-looping
        continue
    
    print("Object list cleaned!")
    return

# A simple function for displaying health
# For debuging purposes only.
    
def healthDisplay():
    
    global playerFighters, enemyFighters, ship
    
    # Displaying health for freindly ships
    
    for i in range(len(playerFighters)):
        
        print("Health for ship {}(Freindly): {}".format(i, playerFighters[i].health))
        
    # Displaying health for hostile ships
    
    for j in range(len(enemyFighters)):
        
        print("Health for ship {}(Hostile): {}".format(j, enemyFighters[j].health))
        
    return

def battle():

    global playerFighters, enemyFighters, ship
    healthDisplay()
    #healthCount()
    #print(enemyFightersHealth)
    clearScreen()
    # Display health of every fighter
    print("+=========================================================+")
    print("Ship Attack Menu\n")

    while True:
        #Cleanup stuff:
        
        objectClean()
        print("Fleet \n\nFighters: {}\nBombers: {}\nInterceptors: {}\nFreighters: {}".format(len(playerFighters), len(playerBombers), len(playerInterceptors), len(playerFreighters)))
        print("\n" * 1)
        print("Enemy Fleet \n\nFighters: {}\nBombers: {}\nInterceptors: {}\nFreighters: {}".format(len(enemyFighters), len(enemyBombers), len(enemyInterceptors), len(enemyFreighters)))
        print("\n" * 1)


        #Player chooses a ship to attack
        playerAttack = str.lower(input("Choose a ship to attack: "))
                            
        if playerAttack in ["fighter", "fighters"]:

            shipChoice = str.lower(input("What ships will you deploy?: "))

            #Player chooses ships to deploy

            #Fighter against Fighter
            if shipChoice in ["fighter", "fighters"]:

                # V OBSOLETE code below: V
#                try:
#                      
#                    for i in range(0, len(enemyFightersHealth)):
#
#                        ranNum = random.uniform(0.5, 1.6)
#                        enemyFightersHealth[i] -= int(playerFighters[i].fighterDmg * ranNum)
#
#                        ranNum = random.uniform(0.5, 1.6)
#                        playerFightersHealth[i] -= int(enemyFighters[i].fighterDmg * ranNum)
#                      
#
#                except Exception:
#
#                    for i in range(0, len(enemyFightersHealth) - len(playerFightersHealth)):
#
#                        ranNum = random.uniform(0.5, 1.6)
#                        enemyFightersHealth[i + len(enemyFightersHealth) - 1] -= int(playerFighters[i].fighterDmg * ranNum)
#
#                        ranNum = random.uniform(0.5, 1.6)
#                        playerFightersHealth[i + len(playerFightersHealth) - 1] -= int(enemyFightersp[i].fighterDmg * ranNum) 
#
#                        break
                # ^OBSOLETE code above^

                #healthClear()
                
                # NEW code below:
                
                print("Output is below is normal.\nDisplaying heath of ships after each battle iteration:")
                for i in range(len(enemyFighters)):

                    ranNum = random.uniform(0.5, 1.6)
                    enemyFighters[i].health -= int(playerFighters[i].fighterDmg * ranNum)
 
                    ranNum = random.uniform(0.5, 1.6)
                    playerFighters[i].health -= int(enemyFighters[i].fighterDmg * ranNum)
                    
                    healthDisplay()

                continue
            
            #Bomber against Fighter
            elif shipChoice in ["bomber", "bombers"]:

                print("You can't attack Fighters with Bombers!")
                continue

            #Interceptor against Fighter
            elif shipChoice in ["interceptor", "interceptors"]:

                pass

            #Freighter against Fighter
            elif shipChoice in ["freighter", "freighters"]:
                
                print("You can't use a Freighter on offense!")
            

        elif playerAttack in ["bomber", "bombers"]:

             shipChoice = str.lower(input("What ships will you deploy? "))

             if shipChoice in ["fighter", "fighters"]:

                 pass


        elif playerAttack in ["interceptor", "interceptors"]:

            print("There are no Interceptors in the enemy fleet!")


        elif playerAttack in ["freighter", "freighters"]:

            print("There are no Freighters in the enemy fleet!")


        else:

            clearScreen()
            sleep(.5)
            print("Please enter a valid ship name")
            pause()
            clearScreen()
            sleep(.5)
            continue

        break
        

battle()