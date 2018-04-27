import random
import time


#CLASSES
class ship:

    def __init__(self, name, hp, attack, attackamount
        ,alloy, fuel, fleet, efleet):

        self.name = name
        self.hp = hp
        self.attack = attack
        self.attackamount = attackamount
        self.alloy = alloy
        self.fuel = fuel
        self.fleet = fleet
        self.efleet = efleet


class cv:

    def __init__(self, name, alloy, maxalloy, fuel, maxfuel, hp, attack, attackamount):

        self.name = name
        self.alloy = alloy
        self.maxalloy = maxalloy
        self.fuel = fuel
        self.maxfuel = maxfuel
        self.hp = hp
        self.attack = attack
        self.attackamount = attackamount


class planet:

    def __init__(self, name, alloy, fuel, defcon, control):

        self.name = name
        self.alloy = alloy
        self.fuel = fuel
        self.defcon = defcon
        self.control = control


class pplanet:

    def __init__(self, hp, alloy, maxalloy, fuel, maxfuel, name):

        self.hp = hp
        self.alloy = alloy
        self.maxalloy = maxalloy
        self.fuel = fuel
        self.maxfuel = maxfuel
        self.name = name

#SHIPDEFINE
fighterfleet = 30
frigatefleet = 0
bomberfleet = 0
interceptorfleet = 0
corvettefleet = 0
destroyerfleet = 0
cruiserfleet = 0
battlecruiserfleet = 0
battlerigfleet = 0
freighterfleet = 0
cargovesselfleet = 0
superfreighterfleet = 0


#SHIPS
capitalvessel = cv('Capital Vessel', 0, 500, 0, 300, 1000, 1500, 15)
fighter = ship('Fighter', 30, 2, 1, 10, 5, fighterfleet, 100)
freighter = ship('Freighter', 200, 10, 3, 300, 200, freighterfleet, 0)
bomber = ship('Bomber', 50, 30, 1, 50, 40, bomberfleet, 0)
interceptor = ship("Interceptor", 50, 30, 1, 60, 20, interceptorfleet, 0)



while True:
    name = input("What will you name your planet? ")
    if name == '':
        print("Please enter a name ")
        continue
    planetname = name
    break


#PLAYER
playerplanet = pplanet(2000, 50, 1000, 0, 1000, planetname)

#DEFCON 1
zechion = planet('Zechion', 400, 200, 1, False)

#DEFCON 2
asmora = planet('Asmora', 650, 300, 2, False)

#DEFCON 3
huaclite = planet('Huaclite', 7000, 4500, 3, False)


'''fighter, frigate, bomber, interceptor, corvette, destroyer, cruiser,
battlecruier, battlerig, freighter, cargovessel, superfreighter'''


#DEFINITONS
check = [fighter, freighter]
seecheck = ["Fighter", "Freighter"]

shiplist = ["Fighter: {} Alloy".format(fighter.alloy), "Freighter: {} Alloy".format(freighter.alloy)]

fleet = [fighter, fighter, fighter, fighter, fighter, fighter, fighter, fighter, fighter, fighter,
         fighter, fighter, fighter, fighter, fighter, fighter, fighter, fighter, fighter, fighter,
         fighter, fighter, fighter, fighter, fighter, fighter, fighter, fighter, fighter, fighter,
         freighter]
seefleet = ["{} Fighter(s)".format(fighterfleet), "{} Frigate(s)".format(frigatefleet), "{} Bomber(s)",
            '{} Interceptor(s)']
attackfleet = [fighter]
seeattackfleet = []

build = fighter
shipbuild = fighter

planets1 = [zechion]
planets2 = []
planets3 = [huaclite]

system = [zechion, asmora, playerplanet, huaclite]
seesystem = [zechion.name, asmora.name, playerplanet.name, huaclite.name]

defcon1fighter = [100, 100, 50, 60, 45, 20, 60]
defcon1freighter = [1, 0, 0, 2, 1, 0]
defcon1frigate = [0, 0, 0, 0, 0, 0, 0, 0, 1]
defcon1bomber = [20, 10, 10, 5, 30, 10, 10]



enemyfleet = []
seeenemyfleet = ["{} Fighter(s)".format(fighter.efleet), '{} Frigate(s)'.format(None), '{} Bomber(s)'.format(None),
                 '{} Intercptor(s)'.format(None)]


#FUNCTIONS

def battle():
    while True:
        deploy = str.lower(input('Deploy which units? '))
        if deploy == 'fighter':
            print("You have deployed a Fighter")
            time.sleep(1.5)
            print("The enemy has deployed a Fighter! ")
            time.sleep(1.5)
            attack = random.randrange(1, 6)
            if attack == 1 or 2 or 4 or 5 or 6:
                print("Your Fighter has destroyed the enemy Fighter ")
                time.sleep(1)
                print("You have gained 50 Alloy and 30 Fuel")

                capitalvessel.alloy += 50
                if capitalvessel.alloy > capitalvessel.maxalloy:
                    print("Your Capital Vessel Alloy storage is full!")

                capitalvessel.fuel += 30
                if capitalvessel.fuel > capitalvessel.maxfuel:
                    print("Your Capital Vessel Fuel storage is full! ")

                print("Your Capital Vessel Alloy storage is at {}, and fuel at {} ".format(capitalvessel.alloy,
                                                                                           capitalvessel.fuel))
                leave = str.lower(input("Return to {}? ".format(planetname)))
                if leave == 'yes':
                    time.sleep(2)
                    print("Your fleet has returned to {}! ".format(planetname))
                    mainplanet()

                if leave == 'no':
                    pass


            if attack == 3:
                print("Your Fighter was destroyed by the enemy Fighter!")

        else:
            print("You don't have this vessel!")


def mainplanet():
    while True:
        choose = str.lower(input("Build Ships, Resources, Research, Planets, See Fleet or Attack?"))

        if choose == 'build ships':

                while True:
                    print(shiplist)
                    build = int(input("Which ships will you build? 0,1,2..."))
                    while True:
                        amount = int(input("Choose amount"))
                        shipbuild = check[build]
                        if playerplanet.alloy - (shipbuild.alloy*amount) < 0:
                            print("You don't have enough Alloy! ")
                            continue

                        if playerplanet.alloy - (shipbuild.alloy*amount) >= 0:
                            playerplanet.alloy -= shipbuild.alloy
                            print("You have built {} {}(s)".format(amount, shipbuild.name))
                            while True:
                                i = amount
                                fleet.append(shipbuild)
                                seefleet.append(shipbuild.name)
                                amount -= 1
                                if i == 0:
                                    break
                            print(seefleet)
                            time.sleep(1)


        if choose == 'resources':
            print("Your Alloy is at {} and Fuel at {}".format(playerplanet.alloy, playerplanet.fuel))

        if choose == 'research':
            print("Not implemented yet")

        if choose == 'planets':
            print("The planets in your system: ")
            time.sleep(1)
            print(system)


        if choose == 'see fleet':
            print(seefleet)

        if choose == 'attack':
            pass


def attack():
    effighter = int
    effreighter = int
    effbomber = int
    efinterceptor = int
    print(seesystem)
    attack = int(input("Which planet will you attack? 0,1,2.."))
    planetattack = system[attack]

    while True:
        print(seefleet)
        print(seecheck)
        choose = int(input("Which ship will you take or attack? 0,1,2..."))
        cship = check[choose]
        break

    while True:
        print(seefleet)
        number = int(input("How many will you take? "))
        d = number
        while True:
            if cship not in fleet:
                break
            attackfleet.append(cship)
            seeattackfleet.append(cship.name)
            d -= 1
            if d == 0:
                break
        break
    print("You have added {} {}(s) to your fleet ".format(number, cship.name))
    at = str.lower(input("Attack {} now? ".format(planetattack.name)))

    if at == 'yes':
        print("Your fleet is advancing on {}! ".format(planetattack.name))
        if planetattack.defcon == 1:
            f1 = int(random.choice(defcon1fighter))
            fighter.efleet += f1
            print(seeenemyfleet)
            d = f1
            while True:
                d -= 1
                enemyfleet.append(fighter)
                if d == 0:
                    break
            f2 = int(random.choice(defcon1freighter))
            freighter.efleet += f2
            number += 1
            d = f2
            while True:
                if d == 0:
                    break
                d -= 1
                enemyfleet.append(defcon1freighter)
                if d == 0:
                    break
            print("{} has launched an enemy fleet! ".format(planetattack.name))
            time.sleep(1)
            print("Their fleet consists of: {}".format(seeenemyfleet))
            r = str.lower(input("Retreat? This will still consume your fuel! "))

            if r == 'yes':
                print("Your fleet is retreating to {} ".format(playerplanet.name))
                time.sleep(2)
                print("Your fleet has returned")
                mainplanet()

            if r == 'no':
                print("Your ships are engaging the enemy fleet! ")
                time.sleep(2)
                while len(attackfleet and enemyfleet) > 0:
                    a = random.choice(attackfleet)
                    c = random.randrange(0, 1)
                    if c == 0:
                        d = random.choice(enemyfleet)
                        b = a.attackamount
                        while True:
                            d.health -= a.attack
                            if d.health < 0:
                                break
                            b -= 1
                            if b == 0:
                                break




                    if c == 1:
                        pass
                    if c == 2:
                        pass
                    if c == 3:
                        pass
                    if c == 4:
                        pass
                    if c == 5:
                        pass
                    if c == 6:
                        pass



        if at == 'no':
            mainplanet()


choice = str.lower(input("Run mainplanet, battle or attack? "))

if choice == 'mainplanet':
    mainplanet()
if choice == 'battle':
    battle()
if choice == 'attack':
    attack()
