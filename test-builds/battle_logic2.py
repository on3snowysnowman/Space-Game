import os
from time import sleep
import random

# Editor: Owen Cochell
# Added random ship ammount, and(hopefully) support for all ship types

shipwin = 100
enemyFighter = random.randrange(0, 100)
enemyBomber = random.randrange(0, 100)
enemyInterceptor = random.randrange(0, 100)

# Forgot other ship type here, lol
# Will change variable name appropriately once I remember the name/type
enemyWhatWasThisShipTypeAgain = random.randrange(0, 100)

enemyshipamount = enemyFighter + enemyBomber + enemyInterceptor + enemyWhatWasThisShipTypeAgain
shipamount = 209999999
def clearScreen():

    os.system('cls' if os.name == 'nt' else 'clear')



def battle():
    # !VERY BAD PRACTICE!
    # using global variables is a SIN
    # Very good reason why global variables are evil here:
    # https://softwareengineering.stackexchange.com/questions/148108/why-is-global-state-so-evil
    # generaly frowned upon in practice, but will be used here for the sake of example:
    
    global shipwin, enemyFighter, enemyBomber, enemyInterceptor, enemyWhatWasThisShipTypeAgain, enemyshipamount, shipamount

    print(">> LOG: Enemy ships detected! ")
    a = input("Press enter to continue... ")
    clearScreen()
    sleep(.5)
    print(">> LOG: Attempting to scan enemy fleet...")
    sleep(1.5)
    clearScreen()
    sleep(.5)
    # Giving player fighters only, for sake of simplicity
    playerFighter = 20
    print(">> LOG: Scan shows fleet contains: \n{} fighters\n{} Bombers\n{} Interceptors\n{} I forgot".format(enemyFighter, enemyBomber, enemyInterceptor, enemyWhatWasThisShipTypeAgain))
    a = input("Press enter to continue... ")
    clearScreen()
    sleep(.5)

    while True:

        print("{} fighters\n{} Bombers\n{} Interceptors\n{} I forgot".format(enemyFighter, enemyBomber, enemyInterceptor, enemyWhatWasThisShipTypeAgain))
        attack = str.lower(input(">> LOG: Displaying enemy fleet, engage which ships? "))
        aids = True
        
        if aids == True:
            clearScreen()
            sleep(.5)

            print("{} fighters".format(shipamount))
            shipchoice = str.lower(input(">> LOG: Deploy which units? "))
            bigboi = True
            
            if bigboi == True:
                
                advantage = enemyshipamount - shipamount
                shipwin -= advantage
                # Calculating damage bonus here:
                damageBost = 1
                if attack == 'fighters':
                    if shipchoice == 'bombers':
                        damageBost = 2
                if attack == 'interceptors':
                    if shipchoice == 'fighters':
                        damageBost = 2
                if attack == 'bombers':
                    if shipchoice == 'forgot':
                        damageBost = 2

                if shipwin in range(95, 106):

                    win = random.randrange(0, 11)

                    if win in [0, 1, 2]:
                         #implementing damage bonus by mutiplying dmage bonus by normal total
                        print("Deploying...")
                        sleep(1)
                        clearScreen()
                        lostmax = int((shipamount / 1.1 + 1))
                        lostmax2 = int((shipamount / 1.1 + 1)*damageBost)
                        lost = random.randrange(0, lostmax)
                        lost2 = random.randrange(0, lostmax2)
                        shipamount -= lost
                        if damageBost != 1:
                            shipamount += lost
                            shipamount -= lost2
                        print("You lost {} ships".format(lost))
                        if damageBost != 1:
                            print("DAMAGE BONUS: {}".format(lost2))
                        print(">> LOG: Your fighters destroyed the enemy fleet, you have {} fighters".format(shipamount))
                        a = input("Press enter to continue... ")
                        clearScreen()
                        sleep(.5)

                    elif win in [3, 4, 5]:
                        print("Deploying...")
                        sleep(1)
                        clearScreen()
                        lostmax = int((shipamount / 1.6) + 1)
                        lostmax2 = int((shipamount / 1.6 + 1)*damageBost)
                        lost = random.randrange(0, lostmax)
                        lost2 = random.randrange(0, lostmax2)
                        shipamount -= lost
                        if damageBost != 1:
                            shipamount += lost
                            shipamount -= lost2
                        print("You lost {} ships".format(lost))
                        if damageBost != 1:
                            print("DAMAGE BONUS: {}".format(lost2))
                        print(">> LOG: Your fighters destroyed the enemy fleet, you have {} fighters".format(shipamount))
                        a = input("Press enter to continue... ")
                        clearScreen()
                        sleep(.5)
                        lost = random.randrange(0, lostmax)
                        shipamount -= lost
                        print(">> LOG: Your fighters destroyed the enemy fleet, you lost {} fighters".format(lost))
                        a = input("Press enter to continue... ")
                        clearScreen()
                        sleep(.5)


                    elif win in [6, 7, 8]:
                        print("Deploying...")
                        sleep(1)
                        clearScreen()
                        lostmax = int((shipamount / 3) + 1)
                        lostmax2 = int((shipamount / 30 + 1) * damageBost)
                        lost = random.randrange(0, lostmax)
                        lost2 = random.randrange(0, lostmax2)
                        shipamount -= lost
                        if damageBost != 1:
                            shipamount += lost
                            shipamount -= lost2
                        print("You lost {} ships".format(lost))
                        if damageBost != 1:
                            print("DAMAGE BONUS: {}".format(lost2))
                        print(">> LOG: Your fighters destroyed the enemy fleet, you have {} fighters".format(shipamount))
                        a = input("Press enter to continue... ")
                        clearScreen()
                        sleep(.5)
                        lost = random.randrange(0, lostmax)
                        shipamount -= lost
                        print(">> LOG: Your fighters destroyed the enemy fleet, you lost {} fighters".format(lost))
                        a = input("Press enter to continue... ")
                        clearScreen()
                        sleep(.5)


                    else:
                        print("Deploying...")
                        sleep(1)
                        clearScreen()
                        print(">> LOG: Your fighters have been destroyed! ")
                        enemylostmin = int(enemyshipamount / 2.5)
                        enemylostmin2 = int((enemyshipamount / 2.5) * damageBost)
                        enemylost = random.randrange(enemylostmin, 11)
                        enemyshipamount -= enemylost
                        print(">> LOG: The enemy fleet lost {} fighters".format(enemylost))

                        a = input("Press enter to continue... ")
                        clearScreen()
                        sleep(.5)
                        # You get the idea.

                if shipwin in range(105, 126):

                    win = random.randrange(0, 11)

                    if win in [0, 1, 2]:
                        print("Deploying...")
                        sleep(1)
                        clearScreen()
                        lostmax = int(shipamount / 1.2 + 1)
                        lost = random.randrange(0, lostmax)
                        shipamount -= lost
                        print(">> LOG: Your fighters destroyed the enemy fleet, you lost {} fighters".format(lost))
                        a = input("Press enter to continue... ")
                        clearScreen()
                        sleep(.5)

                    elif win in [3, 4, 5]:
                        print("Deploying...")
                        sleep(1)
                        clearScreen()
                        lostmax = int((shipamount / 1.6) + 1)
                        lost = random.randrange(0, lostmax)
                        shipamount -= lost
                        print(">> LOG: Your fighters destroyed the enemy fleet, you lost {} fighters".format(lost))
                        a = input("Press enter to continue... ")
                        clearScreen()
                        sleep(.5)


                    elif win in [6, 7, 8]:
                        print("Deploying...")
                        sleep(1)
                        clearScreen()
                        lostmax = int((shipamount / 3) + 1)
                        lost = random.randrange(0, lostmax)
                        shipamount -= lost
                        print(">> LOG: Your fighters destroyed the enemy fleet, you lost {} fighters".format(lost))
                        a = input("Press enter to continue... ")
                        clearScreen()
                        sleep(.5)


                    else:
                        print("Deploying...")
                        sleep(1)
                        clearScreen()
                        print(">> LOG: Your fighters have been destroyed! ")
                        enemylostmin = int(enemyshipamount / 2)
                        enemylost = random.randrange(enemylostmin, 11)
                        print(">> LOG: The enemy fleet lost {} fighters".format(enemylost))

                        a = input("Press enter to continue... ")
                        clearScreen()
                        sleep(.5)


                if shipwin in range(125, 151):

                    win = random.randrange(0, 11)

                    if win in [0, 1, 2]:
                        print("Deploying...")
                        sleep(1)
                        clearScreen()
                        lostmax = int(shipamount / 1.5 + 1)
                        lost = random.randrange(0, lostmax)
                        shipamount -= lost
                        print(">> LOG: Your fighters destroyed the enemy fleet, you lost {} fighters".format(lost))
                        a = input("Press enter to continue... ")
                        clearScreen()
                        sleep(.5)

                    elif win in [3, 4, 5]:
                        print("Deploying...")
                        sleep(1)
                        clearScreen()
                        lostmax = int((shipamount / 2) + 1)
                        lost = random.randrange(0, lostmax)
                        shipamount -= lost
                        print(">> LOG: Your fighters destroyed the enemy fleet, you lost {} fighters".format(lost))
                        a = input("Press enter to continue... ")
                        clearScreen()
                        sleep(.5)


                    elif win in [6, 7, 8]:
                        print("Deploying...")
                        sleep(1)
                        clearScreen()
                        lostmax = int((shipamount / 3) + 1)
                        lost = random.randrange(0, lostmax)
                        shipamount -= lost
                        print(">> LOG: Your fighters destroyed the enemy fleet, you lost {} fighters".format(lost))
                        a = input("Press enter to continue... ")
                        clearScreen()
                        sleep(.5)


                    else:
                        print("Deploying...")
                        sleep(1)
                        clearScreen()
                        print(">> LOG: Your fighters have been destroyed! ")
                        enemylostmin = int(enemyshipamount / 1.4)
                        enemylost = random.randrange(enemylostmin, 11)
                        print(">> LOG: The enemy fleet lost {} fighters".format(enemylost))

                        a = input("Press enter to continue... ")
                        clearScreen()
                        sleep(.5)


                if shipwin in range(150, 171):

                    win = random.randrange(0, 11)

                    if win in [0, 1, 2]:
                        print("Deploying...")
                        sleep(1)
                        clearScreen()
                        lostmax = int(shipamount / 2 + 1)
                        lost = random.randrange(0, lostmax)
                        shipamount -= lost
                        print(">> LOG: Your fighters destroyed the enemy fleet, you lost {} fighters".format(lost))
                        a = input("Press enter to continue... ")
                        clearScreen()
                        sleep(.5)

                    elif win in [3, 4, 5]:
                        print("Deploying...")
                        sleep(1)
                        clearScreen()
                        lostmax = int((shipamount / 2.5) + 1)
                        lost = random.randrange(0, lostmax)
                        shipamount -= lost
                        print(">> LOG: Your fighters destroyed the enemy fleet, you lost {} fighters".format(lost))
                        a = input("Press enter to continue... ")
                        clearScreen()
                        sleep(.5)


                    elif win in [6, 7, 8]:
                        print("Deploying...")
                        sleep(1)
                        clearScreen()
                        lostmax = int((shipamount / 2.7) + 1)
                        lost = random.randrange(0, lostmax)
                        shipamount -= lost
                        print(">> LOG: Your fighters destroyed the enemy fleet, you lost {} fighters".format(lost))
                        a = input("Press enter to continue... ")
                        clearScreen()
                        sleep(.5)


                    else:
                        print("Deploying...")
                        sleep(1)
                        clearScreen()
                        print(">> LOG: Your fighters have been destroyed! ")
                        enemylostmin = int(enemyshipamount / 1.2)
                        enemylost = random.randrange(enemylostmin, enemyshipamount + 1)
                        print(">> LOG: The enemy fleet lost {} fighters".format(enemylost))

                        a = input("Press enter to continue... ")
                        clearScreen()
                        sleep(.5)


                if shipwin in range(170, 201):

                    win = random.randrange(0, 11)

                    if win in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                        print("Deploying...")
                        sleep(1)
                        clearScreen()
                        lostmax = int((shipamount / 1.1) + 1)
                        lost = random.randrange(0, lostmax)
                        shipamount -= lost
                        print(">> LOG: Your fighters destroyed the enemy fleet, you lost {} fighters".format(lost))
                        a = input("Press enter to continue... ")
                        clearScreen()
                        sleep(.5)


                    else:
                        print(">> LOG: Your fighters have been destroyed! ")
                        enemylostmin = int(shipamount / 1.1)
                        enemylost = random.randrange(enemylostmin, enemyshipamount + 1)
                        print(">> LOG: The enemy fleet lost {} fighters".format(enemylost))

                        a = input("Press enter to continue... ")
                        clearScreen()
                        sleep(.5)


                if shipwin > 200:

                    win = random.randrange(0, 11)
                    lostmax = int((shipamount / 9.6) + 1)
                    lost = random.randrange(0, lostmax)
                    shipamount -= lost
                    print(">> LOG: Your fighters destroyed the enemy fleet, you lost {} fighters".format(lost))
                    a = input("Press enter to continue... ")
                    clearScreen()
                    sleep(.5)

            








battle()


