import os
from time import sleep
import random


shipwin = 100


def clearScreen():

    os.system('cls' if os.name == 'nt' else 'clear')



def battle():

    global shipwin

    print(">> LOG: Enemy ships detected! ")
    a = input("Press enter to continue... ")
    clearScreen()
    sleep(.5)
    print(">> LOG: Attempting to scan enemy fleet...")
    sleep(1.5)
    clearScreen()
    sleep(.5)
    enemyshipamount = 10
    shipamount = 20
    print(">> LOG: Scan shows fleet contains {} fighters".format(enemyshipamount))
    a = input("Press enter to continue... ")
    clearScreen()
    sleep(.5)

    while True:

        print("{} fighers".format(enemyshipamount))
        attack = str.lower(input(">> LOG: Displaying enemy fleet, engage which ships? ".format(shipamount)))

        if attack == 'fighters':
            clearScreen()
            sleep(.5)

            print("{} fighters".format(shipamount))
            shipchoice = str.lower(input(">> LOG: Deploy which units? "))

            if shipchoice == 'fighters':

                advantage = enemyshipamount - shipamount
                shipwin -= advantage


                if shipwin in range(95, 106):

                    win = random.randrange(0, 11)

                    if win in [0, 1, 2]:
                        print("Deploying...")
                        sleep(1)
                        clearScreen()
                        lostmax = int(shipamount / 1.1 + 1)
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
                        enemylostmin = int(enemyshipamount / 2.5)
                        enemylost = random.randrange(enemylostmin, 11)
                        enemyshipamount -= enemylost
                        print(">> LOG: The enemy fleet lost {} fighters".format(enemylost))

                        a = input("Press enter to continue... ")
                        clearScreen()
                        sleep(.5)


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


