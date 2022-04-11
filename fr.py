import random
import time
from time import sleep
import sys
import os
import multiprocessing
from rich.console import Console

console = Console()

level1P = False
level2P = False
level3P = False

admin = True


def clearConsole():
    for i in range(0, 150):
        console.print("\n")


class Warrior:
    identifier = "Warrior"
    hp = 15
    hpmax = 15
    battack = 1
    attack = battack
    bdefense = 0
    defense = bdefense
    agility = 10
    agilityMax = 10
    magic = 0
    consciousness = True
    level = 1
    exp = 0
    poisoned = False
    bag = ["smallPotion"]
    weapons = []
    headArmour = []
    chestArmour = []
    legArmour = []
    boots = []
    critChance = 100
    gold = 0
    wEquip = ""
    hEquip = ""
    cEquip = ""
    lEquip = ""
    bEquip = ""

    def __init__(self, name, status, magicAllowed):
        self.name = name
        self.status = status
        self.magicAllowed = magicAllowed

    def smallPotion(self):
        if player.hp + 5 < player.hpmax:
            player.hp += 5
            console.print("You healed 5 hp!")
        if player.hp + 5 >= Warrior.hpmax:
            console.print("You healed " + str(player.hpmax - player.hp) + " hp!")
            player.hp = player.hpmax

    def mediumPotion(self):
        if player.hp + 10 < player.hpmax:
            player.hp += 10
            console.print("You healed 5 hp!")
        if player.hp + 10 >= Warrior.hpmax:
            console.print("You healed " + str(player.hpmax - player.hp) + " hp!")
            player.hp = player.hpmax

    def largePotion(self):
        if player.hp + 20 < player.hpmax:
            player.hp += 20
            console.print("You healed 5 hp!")
        if player.hp + 20 >= Warrior.hpmax:
            console.print("You healed " + str(player.hpmax - player.hp) + " hp!")
            player.hp = player.hpmax

    def rockyLand(self, tf):
        if tf == True:
            player.agility = 10
        else:
            player.agility = player.agilityMax

    def AgilityBuff(self, tf):
        while tf == True:
            player.agility = player.agilityMax * 2
        else:
            player.agility = player.agilityMax


class Monk:
    identifier = "Monk"
    hp = 30
    attack = 10
    defense = 0
    agility = 20
    magic = 10
    consciousness = True
    level = 1
    exp = 0
    poisoned = False
    bag = ["potion"]
    weapons = []
    headArmour = []
    chestArmour = []
    legArmour = []
    boots = []
    critChance = 100
    gold = 0
    wEquip = ""
    hEquip = ""
    cEquip = ""
    lEquip = ""
    bEquip = ""

    def __init__(self, name):
        self.name = name

    def smallPotion(self):
        if player.hp + 5 < player.hpmax:
            player.hp += 5
            console.print("You healed 5 hp!")
        if player.hp + 5 >= Warrior.hpmax:
            console.print("You healed " + str(player.hpmax - player.hp) + " hp!")
            player.hp = player.hpmax

    def mediumPotion(self):
        if player.hp + 10 < player.hpmax:
            player.hp += 10
            console.print("You healed 5 hp!")
        if player.hp + 10 >= Warrior.hpmax:
            console.print("You healed " + str(player.hpmax - player.hp) + " hp!")
            player.hp = player.hpmax

    def largePotion(self):
        if player.hp + 20 < player.hpmax:
            player.hp += 20
            console.print("You healed 5 hp!")
        if player.hp + 20 >= Warrior.hpmax:
            console.print("You healed " + str(player.hpmax - player.hp) + " hp!")
            player.hp = player.hpmax


"""class Mage:
    hp = 10
    attack = 0
    defense = 0
    agility = 20
    magic = 50
    consciousness = True
    level = 1
    exp = 0
    poisoned = False
    bag = ["potion"]
    weapons = []
    headArmour = []
    chestArmour = []
    legArmour = []
    boots = []
    critChance = 100
    gold = 0
    wEquip = ""
    hEquip = ""
    cEquip = ""
    lEquip = ""
    bEquip = ""

    def __init__(self, name):
        self.name = name

    def smallPotion(self):
        if player.hp + 5 < player.hpmax:
            player.hp += 5
            console.print("You healed 5 hp!")
        if player.hp + 5 >= Warrior.hpmax:
            console.print("You healed " + str(player.hpmax - player.hp) + " hp!")
            player.hp = player.hpmax

    def mediumPotion(self):
        if player.hp + 10 < player.hpmax:
            player.hp += 10
            console.print("You healed 5 hp!")
        if player.hp + 10 >= Warrior.hpmax:
            console.print("You healed " + str(player.hpmax - player.hp) + " hp!")
            player.hp = player.hpmax

    def largePotion(self):
        if player.hp + 20 < player.hpmax:
            player.hp += 20
            console.print("You healed 5 hp!")
        if player.hp + 20 >= Warrior.hpmax:
            console.print("You healed " + str(player.hpmax - player.hp) + " hp!")
            player.hp = player.hpmax

"""


class Samurai:
    identifier = "Samurai"
    hp = 25
    attack = 1
    defense = 0
    agility = 25
    magic = 0
    consciousness = True
    level = 1
    exp = 0
    poisoned = False
    weapons = []
    headArmour = []
    chestArmour = []
    legArmour = []
    boots = []
    bag = ["potion"]
    critChance = 100
    gold = 0
    wEquip = ""
    hEquip = ""
    cEquip = ""
    lEquip = ""
    bEquip = ""

    def __init__(self, name):
        self.name = name

    def smallPotion(self):
        if player.hp + 5 < player.hpmax:
            player.hp += 5
            console.print("You healed 5 hp!")
        if player.hp + 5 >= Warrior.hpmax:
            console.print("You healed " + str(player.hpmax - player.hp) + " hp!")
            player.hp = player.hpmax

    def mediumPotion(self):
        if player.hp + 10 < player.hpmax:
            player.hp += 10
            console.print("You healed 5 hp!")
        if player.hp + 10 >= Warrior.hpmax:
            console.print("You healed " + str(player.hpmax - player.hp) + " hp!")
            player.hp = player.hpmax

    def largePotion(self):
        if player.hp + 20 < player.hpmax:
            player.hp += 20
            console.print("You healed 5 hp!")
        if player.hp + 20 >= Warrior.hpmax:
            console.print("You healed " + str(player.hpmax - player.hp) + " hp!")
            player.hp = player.hpmax


class Hero:
    status = None
    magicAllowed = False
    identifier = "Hero"
    hp = 1500
    hpmax = 900
    battack = 300
    attack = 300
    bdefense = 1000
    defense = bdefense
    agility = 500
    agilityMax = 500
    magic = 100
    consciousness = True
    level = 100
    exp = 0
    poisoned = False
    bag = ["largePotion", "largePotion", "largePotion", "largePotion"]
    weapons = []
    headArmour = []
    chestArmour = []
    legArmour = []
    boots = []
    critChance = 4
    gold = 0
    wEquip = ""
    hEquip = ""
    cEquip = ""
    lEquip = ""
    bEquip = ""

    def __init__(self, name, status):
        self.name = name
        self.status = status

    # Items:

    def smallPotion(self):
        if Hero.hp + 5 < Hero.hpmax:
            Hero.hp += 5
            console.print("You healed 5 hp!")
        if Hero.hp + 5 >= Warrior.hpmax:
            console.print("You healed " + str(Hero.hpmax - Hero.hp) + " hp!")
            Hero.hp = Hero.hpmax

    def mediumPotion(self):
        if Hero.hp + 10 < Hero.hpmax:
            Hero.hp += 10
            console.print("You healed 5 hp!")
        if Hero.hp + 10 >= Warrior.hpmax:
            console.print("You healed " + str(Hero.hpmax - Hero.hp) + " hp!")
            Hero.hp = Hero.hpmax

    def largePotion(self):
        if Hero.hp + 20 < Hero.hpmax:
            Hero.hp += 20
            console.print("You healed 5 hp!")
        if Hero.hp + 20 >= Warrior.hpmax:
            console.print("You healed " + str(Hero.hpmax - Hero.hp) + " hp!")
            Hero.hp = Hero.hpmax

    # Magic:

    def fireBall(self):
        enemy.health -= 100
        Hero.magic -= 4
        enemy.status = "Burning"

    def lightning(self):
        enemy.health -= 140
        Hero.magic -= 12
        enemy.status = "Hazed"

    def sludge(self):
        enemy.health -= 50
        Hero.magic -= 2
        enemy.poisoned = True

    def fireBlaze(self):
        enemy.health -= 500
        Hero.magic -= 40
        enemy.status = "Burning"

    def lightningMax(self):
        enemy.health -= 600
        Hero.magic -= 70
        enemy.status = "Hazed"


class GoblinFootSoldier:
    attack = 2
    defense = 2
    agility = 4
    health = 8
    hpmax = 8
    critChance = 100000
    exp = 5
    mp = 0

    def __init__(self, name, poisoned, items, weapons, headArmour, chestArmour, legArmour, boots, gold, status):
        self.name = name
        self.poisoned = poisoned
        self.items = items
        self.weapons = weapons
        self.headArmour = headArmour
        self.chestArmour = chestArmour
        self.legArmour = legArmour
        self.boots = boots
        self.gold = gold
        self.status = status

class bossOgre:
    attack = 12
    defense = 5
    agility = 1
    health = 40
    hpmax = 40
    critChance = 100000
    exp = 40
    mp = 0

    def __init__(self, name, poisoned, items, weapons, headArmour, chestArmour, legArmour, boots, gold, status):
        self.name = name
        self.poisoned = poisoned
        self.items = items
        self.weapons = weapons
        self.headArmour = headArmour
        self.chestArmour = chestArmour
        self.legArmour = legArmour
        self.boots = boots
        self.gold = gold
        self.status = status

class Lucifer:
    attack = 9999
    defense = 9999
    agility = 9999
    health = 9999
    hpmax = 9999
    critChance = 2
    exp = 1000000000000
    mp = 19019201920190190

    def __init__(self, name, poisoned, items, weapons, headArmour, chestArmour, legArmour, boots, gold, status):
        self.name = name
        self.poisoned = poisoned
        self.items = items
        self.weapons = weapons
        self.headArmour = headArmour
        self.chestArmour = chestArmour
        self.legArmour = legArmour
        self.boots = boots
        self.gold = gold
        self.status = status


class DarkFairy:
    attack = 5
    defense = 3
    agility = 20
    health = 15
    hpmax = 15
    critChance = 10000
    exp = 10
    mp = 5

    def __init__(self, name, poisoned, items, weapons, headArmour, chestArmour, legArmour, boots, gold, status):
        self.name = name
        self.poisoned = poisoned
        self.items = items
        self.weapons = weapons
        self.headArmour = headArmour
        self.chestArmour = chestArmour
        self.legArmour = legArmour
        self.boots = boots
        self.gold = gold
        self.status = status

    def fireball(self):
        player.hp -= 7
        player.status = "Burning"


class GiantGoblin:
    attack = 6
    defense = 10
    agility = 1
    health = 20
    hpmax = 20
    critChance = 10000
    exp = 20
    mp = 0

    def __init__(self, name, poisoned, items, weapons, headArmour, chestArmour, legArmour, boots, gold, status):
        self.name = name
        self.poisoned = poisoned
        self.items = items
        self.weapons = weapons
        self.headArmour = headArmour
        self.chestArmour = chestArmour
        self.legArmour = legArmour
        self.boots = boots
        self.gold = gold
        self.status = status


class DarkKnight:
    attack = 310
    defense = 1000
    agility = 300
    health = 1300
    hpmax = 1300
    critChance = 5
    exp = 0
    mp = 100

    def __init__(self, name, poisoned, items, weapons, headArmour, chestArmour, legArmour, boots, gold, status):
        self.name = name
        self.poisoned = poisoned
        self.items = items
        self.weapons = weapons
        self.headArmour = headArmour
        self.chestArmour = chestArmour
        self.legArmour = legArmour
        self.boots = boots
        self.gold = gold
        self.status = status

    def fireBall(self):
        Hero.hp -= 100
        enemy.mp -= 4
        Hero.status = "Burning"

    def lightning(self):
        Hero.hp -= 140
        enemy.mp -= 12
        Hero.status = "Hazed"

    def sludge(self):
        Hero.hp -= 50
        enemy.mp -= 2
        Hero.poisoned = True

    def fireBlaze(self):
        Hero.hp -= 500
        enemy.mp -= 40
        Hero.status = "Burning"

    def lightningMax(self):
        Hero.hp -= 600
        enemy.mp -= 70
        Hero.status = "Hazed"


def itemPickup():
    console.print(len(player.bag))
    if len(player.bag) < 20:
        for i in range(0, len(enemy.items)):
            player.bag.append(enemy.items[i])
        for i in range(0, len(enemy.weapons)):
            player.weapons.append(enemy.weapons[i])
        for i in range(0, len(enemy.headArmour)):
            player.headArmour.append(enemy.headArmour[i])
        for i in range(0, len(enemy.chestArmour)):
            player.chestArmour.append(enemy.chestArmour[i])
        for i in range(0, len(enemy.legArmour)):
            player.legArmour.append(enemy.legArmour[i])
        for i in range(0, len(enemy.boots)):
            player.boots.append(enemy.boots[i])
        player.gold += enemy.gold
    if len(player.bag) >= 20:
        while player.bag >= 20:
            removeItem = str(input("Would you like to remove an item? (Y/N): ")).upper()
            if removeItem == "Y":
                console.print("Which item would you like to remove?")
                for i in range(0, len(player.bag) - 1):
                    console.print(str(i + 1) + ". " + player.bag[i])
                itemremovenum = int(input(""))
                player.bag.remove(itemremovenum - 1)
                continue
            if removeItem == "N":
                console.print("You left the items")
                return True


gold = 0



print("""

╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╮╭━╮╱╱╱╱╱╭╮
╰╮╭╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃╰╯┃┃╱╱╱╱╭╯╰╮
╱┃┃┃┣╮╭┳━╮╭━━┳━━┳━━┳━╮╱┃╭╮╭╮┣━━┳━┻╮╭╋━━┳━╮
╱┃┃┃┃┃┃┃╭╮┫╭╮┃┃━┫╭╮┃╭╮╮┃┃┃┃┃┃╭╮┃━━┫┃┃┃━┫╭╯   ,_._._._._._._._._|__________________________________________________________,
╭╯╰╯┃╰╯┃┃┃┃╰╯┃┃━┫╰╯┃┃┃┃┃┃┃┃┃┃╭╮┣━━┃╰┫┃━┫┃    |_|_|_|_|_|_|_|_|_|_________________________________________________________/
╰━━━┻━━┻╯╰┻━╮┣━━┻━━┻╯╰╯╰╯╰╯╰┻╯╰┻━━┻━┻━━┻╯                      !
╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╰━━╯
""")

console.print("Welcome to dungeon master!\n", style="bold red")

Pname = str(input("What is your name?\n"))

global player
player = Warrior(Pname, "", False)

'''if className == 2:
    Pname = str(input("What is your characters name?\n")).capitalize()
    player = Monk(Pname)

if className == 3:
    Pname = str(input("What is your characters name?\n"))
    player = Mage(Pname)

if className == 3:
    Pname = str(input("What is your characters name?\n")).capitalize()
    Samurai = Warrior(Pname)
'''
critChance = player.critChance
player.AgilityBuff(False)
player.rockyLand(False)

while True:
    try:
        readyConfirmation = int(input("""Are you ready to adventure?
        [1] Yes
        [2] No
        \n"""))
        if readyConfirmation == "1":
            console.print("Welcome to the world of Fantasia")
            break
        if readyConfirmation == "2":
            console.print("R.I.P")
            quit()
    except ValueError:
        console.print("")
    else:
        break

console.print("\n \n \n \n")


def statsUpdate(attack=None, DandA=None, agility=None):
    if attack != None:
        if isinstance(attack, str):
            if attack == "Dagger":
                player.attack = 2 + player.battack
            if attack == "Sword":
                player.attack = 9 + player.battack
            if attack == "Halbard":
                player.attack = 10 + player.battack
        if isinstance(attack, int):
            player.attack = attack
    if DandA != None and agility != None:
        if isinstance(DandA, list):
            if DandA[0] == "Rusty Helmet":
                player.defense = 1 + player.bdefense
                player.agility = 0.96 * (player.agility)
            if DandA[0] == "Knights Helmet":
                player.defense += 3 + player.bdefense
                player.agility = 0.96 * (player.agility)
            if DandA[0] == "King's Crown":
                player.defense += 5 + player.bdefense
                player.agility = 0.99 * (player.agility)
            if DandA[1] == "Rusty Chestplate":
                player.defense = 3 + player.bdefense
                player.agility = 0.96 * (player.agility)
            if DandA[1] == "Knight's Chestplate":
                player.defense += 5 + player.bdefense
                player.agility = 0.96 * (player.agility)
            if DandA[1] == "King's Chestplate":
                player.defense += 10 + player.bdefense
                player.agility = 0.99 * (player.agility)
            if DandA[2] == "Tattred Leggings":
                player.defense = 2 + player.bdefense
                player.agility = 0.96 * (player.agility)
            if DandA[2] == "Leather Leggings":
                player.defense += 3 + player.bdefense
                player.agility = 0.96 * (player.agility)
            if DandA[2] == "King's Leggings":
                player.defense += 4 + player.bdefense
                player.agility = 0.99 * (player.agility)
            if DandA[3] == "Tattred Boots":
                player.defense = 1 + player.bdefense
                player.agility = 0.96 * (player.agility)
            if DandA[3] == "Knights Greaves":
                player.defense += 2 + player.bdefense
                player.agility = 0.96 * (player.agility)
            if DandA[3] == "King's boots":
                player.defense += 3 + player.bdefense
                player.agility = 0.99 * (player.agility)
        if isinstance(DandA, int):
            player.defense = DandA
        if isinstance(agility, int):
            player.agility = agility

    if attack == None and DandA == None and agility == None:
        if player.wEquip == "" and player.hEquip == "" and player.cEquip == "" and player.lEquip == "" and player.bEquip == "":
            player.agility = player.agilityMax
            player.attack = player.battack
            player.defense = player.bdefense


def equipScreen():
    console.print("\n")
    if player.wEquip != "":
        console.print("Weapon: " + player.wEquip)
    else:
        console.print("Weapon: None")
    if player.hEquip != "":
        console.print("Helmet: " + player.hEquip)
    else:
        console.print("Helmet: None")
    if player.cEquip != "":
        console.print("Chestplate: " + player.cEquip)
    else:
        console.print("Chestplate: None")
    if player.wEquip != "":
        console.print("Leggings: " + player.lEquip)
    else:
        console.print("Leggings: None")
    if player.bEquip != "":
        console.print("Boots: " + player.bEquip)
    else:
        console.print("Boots: None")
    if str(input("Would you like to change your equipment? (Y/N): ")).upper() == "Y":
        console.print("Which equipment would you like to change?: ")
        console.print("""
[1] Weapon
[2] Helmet
[3] Chestplate
[4] Leggings
[5] Boots
[6] Quit
            """)
        changeInput = int(input(""))
        if changeInput == 1:
            if len(player.weapons) == 0:
                console.print("You have no weapons!")
            else:
                for i in range(0, len(player.weapons)):
                    console.print(str(i + 1) + ". " + player.weapons[i])
                weaponChange = int(input("Which weapon would you like to equip?: "))
                player.wEquip = player.weapons[weaponChange - 1]
                console.print("You equiped your " + str(player.wEquip))
        if changeInput == 2:
            if len(player.headArmour) == 0:
                console.print("You have no helmets!")

            else:
                for i in range(0, len(player.headArmour)):
                    console.print(str(i + 1) + ". " + player.headArmour[i])
                headChange = int(input("Which helmet would you like to equip?"))
                player.hEquip = player.headArmour[headChange - 1]
                console.print("You equiped your " + str(player.hEquip))
        if changeInput == 3:
            if len(player.chestArmour) == 0:
                console.print("You have no Chestplates!")
            else:
                for i in range(0, len(player.chestArmour)):
                    console.print(str(i + 1) + ". " + player.chestArmour[i])
                chestChange = int(input("Which chestplate would you like to equip?"))
                player.cEquip = player.chestArmour[chestChange - 1]
                console.print("You equiped your " + str(player.cEquip))
        if changeInput == 4:
            if len(player.legArmour) == 0:
                console.print("You have no Leggings!")
            else:
                for i in range(0, len(player.legArmour)):
                    console.print(str(i + 1) + ". " + player.legArmour[i])
                legChange = int(input("Which leggings would you like to equip?"))
                player.lEquip = player.legArmour[legChange - 1]
                console.print("You equiped your " + str(player.lEquip))
        if changeInput == 5:
            if len(player.boots) == 0:
                console.print("You have no boots!")
            else:
                for i in range(0, len(player.boots)):
                    console.print(str(i + 1) + ". " + player.boots[i])
                bootChange = int(input("Which boots would you like to equip?"))
                player.bEquip = player.boots[bootChange - 1]
                console.print("You equiped your " + str(player.bEquip))

    else:
        console.print("\n")
    statsUpdate(player.wEquip, [player.hEquip, player.cEquip, player.lEquip, player.bEquip], "")


def shop():
    ()


def rest():
    ()


def homeScreen(level1Master=None, level2Master=None, level3Master=None):
    console.print("What would you like to do? ")
    if level1P == False and level1Master != True:
        console.print("[1] Level 1")
    elif level2P == False and level1Master == True:
        console.print("[1] Level 2")
    elif level3P == False or level2P == True or level2Master == True:
        console.print("[1] Level 3")
    elif level3Master == True:
        console.print("[1] Level Select")
    console.print("[2] Shop")
    if Warrior.poisoned or Monk.poisoned or Samurai.poisoned != True:
        console.print("[3] Rest")

    console.print("[4] Equipment")
    while True:
        try:
            homescreenInput = int(input('\n \n'))
        except ValueError:
            console.print("")
        else:
            break

    if homescreenInput == 1 and level1P == False and level1Master != True:
        level1()
    elif homescreenInput == 1 and (level1P == True and level2P == False) or level1Master == True and level2Master != True:
        level2()
        console.print("")
    elif homescreenInput == 1 and ((level3P == False) or level2Master == True):
        level3()
        console.print("")
    elif level3Master == True and homescreenInput == 1:
        print("""[1] Level 1
        [2] Level 2
        [3] Level 3""")
        levelSelect = input("")
        if levelSelect == 1:
            level1()
        if levelSelect == 2:
            level2()
        if levelSelect == 3:
            level3()

    if homescreenInput == 2 and level2P == False:
        console.print("There is no shop for you to go to!")
    else:
        shop()

    if homescreenInput == 3:
        rest()

    if homescreenInput == 4:
        equipScreen()


def inlevelMenue(eChangeAllowed, bagAllowed, gototownAllowed):
    menue = 0
    while True:
        numbermenue = 0
        echange = 0
        bchange = 0
        tchange = 0
        if eChangeAllowed == True:
            echange = numbermenue + 1
            numbermenue += 1
            console.print(str(echange) + ". Change Equipment")
        if bagAllowed == True:
            bchange = numbermenue + 1
            numbermenue += 1
            console.print(str(bchange) + ". Use bag items")
        if gototownAllowed == True:
            tchange = numbermenue + 1
            numbermenue += 1
            console.print(str(tchange) + ". Go Back to Town")
        if True:
            cCHange = numbermenue + 1
            numbermenue += 1
            console.print(str(cCHange) + ". Exit Menue")
        menue = int(input("What would you like to do?: "))

        if menue == echange:
            equipScreen()
        if menue == bchange:
            for i in range(0, len(player.bag)):
                console.print(str(i + 1) + "." + player.bag[i])
            while True:
                try:
                    bagInput = int(input("What item would you like to use?: "))
                except ValueError:
                    console.print("")
                else:
                    break
            if player.bag[bagInput - 1] == "smallPotion":
                player.smallPotion()
            if player.bag[bagInput - 1] == "mediumPotion":
                player.mediumPotion()
            if player.bag[bagInput - 1] == "largePotion":
                player.largePotion()

        if menue == tchange:
            if str(input(
                    "Are you sure you want to go back to town? Your level progress will be reset....  (Y/N)    ")).upper() == "Y":
                homeScreen()
            else:
                continue

        if menue == cCHange:
            break


def enemyDamage():
    magic = random.randrange(1, 4)

    if (player.agility - enemy.agility) / player.agility < 0.1:
        missChancE = random.randrange(1, 1001)
    elif (player.agility - enemy.agility) / player.agility < 0.25:
        missChancE = random.randrange(1, 751)
    elif (player.agility - enemy.agility) / player.agility < 0.5:
        missChancE = random.randrange(1, 251)
    elif (player.agility - enemy.agility) / player.agility < 0.75:
        missChancE = random.randrange(1, 151)
    elif (player.agility - enemy.agility) / player.agility < 0.85:
        missChancE = random.randrange(1, 101)
    elif (player.agility - enemy.agility) / player.agility < 0.9:
        missChancE = random.randrange(1, 56)
    elif (player.agility - enemy.agility) / player.agility < 0.95:
        missChancE = random.randrange(1, 26)
    elif (player.agility - enemy.agility) / player.agility < 1.:
        missChancE = random.randrange(1, 11)
    elif (player.agility - enemy.agility) / player.agility < 2.5:
        missChancE = random.randrange(1, 3)

    if missChancE == 1:
        console.print("The enemy missed the attack and did no damage to you!")
    else:
        if Hero.magicAllowed == True:
            if magic == 3 and enemy.mp >= 2:
                magicRand = random.randrange(1, 6)
                while magicRand != 7:
                    if enemy.mp > 4 and magicRand == 1:
                        enemy.fireball()
                    else:
                        magicRand = random.randrange(1, 6)
                        continue
                    if enemy.mp > 12 and magicRand == 2:
                        enemy.lighning()
                    else:
                        magicRand = random.randrange(1, 6)
                        continue
                    if enemy.mp > 2 and magicRand == 3:
                        enemy.sludge()
                    else:
                        magicRand = random.randrange(1, 6)
                        continue
                    if enemy.mp > 40 and magicRand == 4:
                        enemy.fireBlaze()
                    else:
                        magicRand = random.randrange(1, 6)
                        continue
                    if enemy.mp > 70 and magicRand == 5:
                        enemy.lightningMax()
                    else:
                        magicRand = random.randrange(1, 6)
                        continue

                enemy.fireball()
                console.print("The enemy cast fireball on you!")
                enemy.mp -= 2
        else:
            critE = random.randrange(1, enemy.critChance)
            if critE == 1:
                player.hp -= (enemy.attack * 2)
                console.print("Critical Hit! The enemy did " + str(enemy.attack * 2) + " damage to you!")
            else:
                player.hp -= enemy.attack
                console.print("The enemy damaged you by " + str(enemy.attack) + " hp!")
    if player.poisoned == True:
        player.hp -= round(0.07 * (player.hpmax))
        console.print("You lost " + (str(round(0.07 * (player.hpmax)))) + " points from the poison!")
    if enemy.poisoned == True:
        enemy.health -= round(0.07 * (enemy.hpmax))
        console.print("The enemy lost " + str(round(0.07 * (enemy.hpmax))) + " points from poison!")
    if player.status == "Burning":
        player.hp -= round(0.09 * (player.hpmax))
        console.print("You lost " + str(round(0.09 * (player.hpmax))) + " points from burning!")
    if Hero.poisoned == True:
        Hero.hp -= round(0.07 * (Hero.hpmax))
        console.print("You lost " + (str(round(0.07 * (Hero.hpmax)))) + " points from the poison!")
    if Hero.status == "Burning":
        Hero.hp -= round(0.09 * (Hero.hpmax))
        console.print("You lost " + str(round(0.09 * (Hero.hpmax))) + " points from burning!")
    if enemy.status == "Hazed":
        enemy.attack = 0.9 * (enemy.attack)


def typingEffect(str, time=None):
    if admin == True:
        t = 0
    else:
        if time is None:
            t = 0.1
        else:
            t = time
    for letter in str:
        sleep(t)  # In seconds
        sys.stdout.write(letter)
        sys.stdout.flush()


def level1():
    clearConsole()
    print("""
             ('-.        (`-.      ('-.                        
           _(  OO)     _(OO  )_  _(  OO)                       
 ,--.     (,------.,--(_/   ,. \(,------.,--.            .---. 
 |  |.-')  |  .---'\   \   /(__/ |  .---'|  |.-')       /_   | 
 |  | OO ) |  |     \   \ /   /  |  |    |  | OO )       |   | 
 |  |`-' |(|  '--.   \   '   /, (|  '--. |  |`-' |       |   | 
(|  '---.' |  .--'    \     /__) |  .--'(|  '---.'       |   | 
 |      |  |  `---.    \   /     |  `---.|      |        |   | 
 `------'  `------'     `-'      `------'`------'        `---' 


    """)
    pickup = ""

    def battle1(fighter, dropNames, asd, bsd, csd, mainPlayer):
        while fighter.hp > 0 and enemy.health > 0:
            console.print("\n")
            console.print(fighter.name + "'s HP: " + str(fighter.hp))
            console.print(enemy.name + "'s HP: " + str(enemy.health))
            console.print("MP: " + str(fighter.magic) + "\n")
            console.print("""What would you like to do?
                    [1] Attack
                    [2] Defend
                    [3] Item
                    [4] Flee """)
            if fighter.magic:
                console.print("         [5] Magic")

            battleD = int(input("\n"))

            if battleD == 1:

                if (enemy.agility - fighter.agility) / enemy.agility < 0.1:
                    missChancP = random.randrange(1, 1001)
                elif (enemy.agility - fighter.agility) / enemy.agility < 0.25:
                    missChancP = random.randrange(1, 751)
                elif (enemy.agility - fighter.agility) / enemy.agility < 0.5:
                    missChancP = random.randrange(1, 251)
                elif (enemy.agility - fighter.agility) / enemy.agility < 0.75:
                    missChancP = random.randrange(1, 151)
                elif (enemy.agility - fighter.agility) / enemy.agility < 0.85:
                    missChancP = random.randrange(1, 101)
                elif (enemy.agility - fighter.agility) / enemy.agility < 0.9:
                    missChancP = random.randrange(1, 56)
                elif (enemy.agility - fighter.agility) / enemy.agility < 0.95:
                    missChancP = random.randrange(1, 26)
                elif (enemy.agility - fighter.agility) / enemy.agility < 1.:
                    missChancP = random.randrange(1, 11)
                elif (enemy.agility - fighter.agility) / enemy.agility < 2.5:
                    missChancP = random.randrange(1, 3)
                elif (enemy.agility - fighter.agility) / enemy.agility < 5:
                    missChancP = random.randrange(1, 2)

                if missChancP == 1:
                    console.print("You missed your attack!")
                    enemyDamage()
                else:
                    crit = random.randrange(1, critChance)
                    if crit == 1:
                        enemy.health -= (fighter.attack * 1.5)
                        console.print("Critical Hit! You did " + str(fighter.attack * 1.5) + " damage on the enemy")
                        enemyDamage()
                        continue
                    else:
                        enemy.health -= fighter.attack
                        console.print("You did " + str(player.attack) + " damage on the enemy!")
                        enemyDamage()
                        continue

            if battleD == 2:
                defenceT = fighter.defense
                if defenceT > enemy.attack:
                    console.print("You defended the attack!")
                    defenceT -= 0.4 * (enemy.attack)
                    enemyDamage()
                    continue
                else:
                    console.print("You were unable to defend the attack!")
                    enemyDamage()
                    continue

            if battleD == 3:
                for i in range(0, len(fighter.bag)):
                    console.print(str(i + 1) + "." + fighter.bag[i])
                while True:
                    try:
                        bagInput = int(input("What item would you like to use?: "))
                    except ValueError:
                        console.print("")
                    else:
                        break
                if fighter.bag[bagInput - 1] == "smallPotion":
                    fighter.smallPotion()
                    enemyDamage()
                    continue
                if fighter.bag[bagInput - 1] == "mediumPotion":
                    fighter.mediumPotion()
                    enemyDamage()
                    continue
                if fighter.bag[bagInput - 1] == "largePotion":
                    fighter.largePotion()
                    enemyDamage()
                    continue

            if battleD == 4:
                if fighter.agility > enemy.agility:
                    global flee
                    flee = True
                    homeScreen()
                    break
                else:
                    console.print("You were unable to flee!")
                    continue

            if battleD == 5:
                console.print("""Spells:
                    [1] Fireball
                        MP Cost: 4

                    [2] Lightning
                        MP Cost: 12

                    [3] Sludge
                        MP Cost: 2

                    [4] Fire Blaze
                        MP Cost: 40

                    [5] Lightning Max
                        MP Cost: 70

                            """)
                magicChoice = int(input("What spell would you like to use?: "))
                if magicChoice == 1:
                    Hero.fireBall()
                if magicChoice == 2:
                    Hero.lightning()
                if magicChoice == 3:
                    Hero.sludge()
                if magicChoice == 4:
                    Hero.fireBlaze()
                if magicChoice == 5:
                    Hero.lightningMax()
                enemyDamage()
                continue

        if fighter.hp <= 0:
            console.print(enemy.name + " killed you! \n")
            fighter.hp = fighter.hpmax
            homeScreen()
        if mainPlayer == True:
            if (enemy.health <= 0):
                console.print("\nYou have succesfully slain " + enemy.name)
                player.status = ""
                player.poisoned = False
                Hero.status = ""
                Hero.poisoned = False
                player.exp += enemy.exp
            time.sleep(0.5)
            console.print(enemy.name + " dropped " + dropNames)
            global pickup1
            pickup1 = str(input("Would you like to pick them up? (Y/N): ")).upper()
            if pickup1 == "Y":
                itemPickup()

            if pickup1 == "N":
                console.print("You left the items......")
            else:
                while pickup1 != "Y" and pickup1 != "N":
                    pickup1 = str(input("Would you like to pick them up? (Y/N): ")).upper
            pickup = pickup1
            console.print("\nYou gained " + str(enemy.exp) + " exp!")
            if player.exp >= round((4 * (player.level ** 3)) / 5):
                player.level += 1
                player.exp -= player.exp
                console.print("You have reached level " + str(player.level) + "!")
                time.sleep(1)
                temphp = player.hpmax
                player.hpmax = player.hpmax + (2 ** player.level)
                player.hp = player.hpmax
                tempAttck = player.battack
                player.battack += 2 ** player.level
                tempdef = player.bdefense
                player.bdefense += 2 ** player.level
                tempagil = player.agilityMax
                player.agilityMax += 2 ** player.level

                console.print(str(temphp) + " hp --> " + str(player.hpmax) + " hp")
                time.sleep(1)
                console.print(str(tempAttck) + " Attack --> " + str(player.battack) + " Attack")
                time.sleep(1)
                console.print(str(tempdef) + " defense --> " + str(player.bdefense) + " defense")
                time.sleep(1)
                console.print(str(tempagil) + " Agility --> " + str(player.agilityMax) + " Agility")
                time.sleep(1)
                console.print("Health Restored!")
                statsUpdate()

            while True:
                while True:
                    nextMove = int(input("""

                                    [1] Equipment Change
                                    [2] Continue Adventure
                                    [3] Menue

                                    """))
                    if nextMove == 1:
                        equipScreen()
                    elif nextMove == 2:
                        breakOut = True
                        break
                    elif nextMove == 3:
                        inlevelMenue(asd, bsd, csd)
                    else:
                        continue
                if breakOut == True:
                    break

    time.sleep(1)
    typingEffect("You find yourself in an unknown place with no weapons and no armour\n", )
    time.sleep(1)
    typingEffect("You suddenly see a goblin who looks poisoned rushing at you and instinctively take battle stance! \n",
                 0.045)
    global enemy
    enemy = GoblinFootSoldier("The goblin", True, [], ["Dagger"], [], [], [], [], 30, "")
    battle1(player, "a Dagger and 30 gold", True, True, False, True)
    if player.hp <= 0:
        return False
    level1P = True
    homeScreen(True, False, False)

def level2():
    clearConsole()

    print("""
                 ('-.        (`-.      ('-.                           
           _(  OO)     _(OO  )_  _(  OO)                          
 ,--.     (,------.,--(_/   ,. \(,------.,--.            .-----.  
 |  |.-')  |  .---'\   \   /(__/ |  .---'|  |.-')       / ,-.   \ 
 |  | OO ) |  |     \   \ /   /  |  |    |  | OO )      '-'  |  | 
 |  |`-' |(|  '--.   \   '   /, (|  '--. |  |`-' |         .'  /  
(|  '---.' |  .--'    \     /__) |  .--'(|  '---.'       .'  /__  
 |      |  |  `---.    \   /     |  `---.|      |       |       | 
 `------'  `------'     `-'      `------'`------'       `-------' """)

    def battle1(fighter, dropNames, asd, bsd, csd, mainPlayer):
        while fighter.hp > 0 and enemy.health > 0:
            console.print("\n")
            console.print(fighter.name + "'s HP: " + str(fighter.hp))
            console.print(enemy.name + "'s HP: " + str(enemy.health))
            console.print("MP: " + str(fighter.magic) + "\n")
            console.print("""What would you like to do?
                    [1] Attack
                    [2] Defend
                    [3] Item
                    [4] Flee """)
            if fighter.magic:
                console.print("         [5] Magic")

            battleD = int(input("\n"))

            if battleD == 1:

                if (enemy.agility - fighter.agility) / enemy.agility < 0.1:
                    missChancP = random.randrange(1, 1001)
                elif (enemy.agility - fighter.agility) / enemy.agility < 0.25:
                    missChancP = random.randrange(1, 751)
                elif (enemy.agility - fighter.agility) / enemy.agility < 0.5:
                    missChancP = random.randrange(1, 251)
                elif (enemy.agility - fighter.agility) / enemy.agility < 0.75:
                    missChancP = random.randrange(1, 151)
                elif (enemy.agility - fighter.agility) / enemy.agility < 0.85:
                    missChancP = random.randrange(1, 101)
                elif (enemy.agility - fighter.agility) / enemy.agility < 0.9:
                    missChancP = random.randrange(1, 56)
                elif (enemy.agility - fighter.agility) / enemy.agility < 0.95:
                    missChancP = random.randrange(1, 26)
                elif (enemy.agility - fighter.agility) / enemy.agility < 1.:
                    missChancP = random.randrange(1, 11)
                elif (enemy.agility - fighter.agility) / enemy.agility < 2.5:
                    missChancP = random.randrange(1, 3)
                elif (enemy.agility - fighter.agility) / enemy.agility < 5:
                    missChancP = random.randrange(1, 2)

                if missChancP == 1:
                    console.print("You missed your attack!")
                    enemyDamage()
                else:
                    crit = random.randrange(1, critChance)
                    if crit == 1:
                        enemy.health -= (fighter.attack * 1.5)
                        console.print("Critical Hit! You did " + str(fighter.attack * 1.5) + " damage on the enemy")
                        enemyDamage()
                        continue
                    else:
                        enemy.health -= fighter.attack
                        console.print("You did " + str(player.attack) + " damage on the enemy!")
                        enemyDamage()
                        continue

            if battleD == 2:
                defenceT = fighter.defense
                if defenceT > enemy.attack:
                    console.print("You defended the attack!")
                    defenceT -= 0.4 * (enemy.attack)
                    enemyDamage()
                    continue
                else:
                    console.print("You were unable to defend the attack!")
                    enemyDamage()
                    continue

            if battleD == 3:
                for i in range(0, len(fighter.bag)):
                    console.print(str(i + 1) + "." + fighter.bag[i])
                while True:
                    try:
                        bagInput = int(input("What item would you like to use?: "))
                    except ValueError:
                        console.print("")
                    else:
                        break
                if fighter.bag[bagInput - 1] == "smallPotion":
                    fighter.smallPotion()
                    enemyDamage()
                    continue
                if fighter.bag[bagInput - 1] == "mediumPotion":
                    fighter.mediumPotion()
                    enemyDamage()
                    continue
                if fighter.bag[bagInput - 1] == "largePotion":
                    fighter.largePotion()
                    enemyDamage()
                    continue

            if battleD == 4:
                if fighter.agility > enemy.agility:
                    global flee
                    flee = True
                    homeScreen()
                    break
                else:
                    console.print("You were unable to flee!")
                    continue

            if battleD == 5:
                console.print("""Spells:
                    [1] Fireball
                        MP Cost: 4

                    [2] Lightning
                        MP Cost: 12

                    [3] Sludge
                        MP Cost: 2

                    [4] Fire Blaze
                        MP Cost: 40

                    [5] Lightning Max
                        MP Cost: 70

                            """)
                magicChoice = int(input("What spell would you like to use?: "))
                if magicChoice == 1:
                    Hero.fireBall()
                if magicChoice == 2:
                    Hero.lightning()
                if magicChoice == 3:
                    Hero.sludge()
                if magicChoice == 4:
                    Hero.fireBlaze()
                if magicChoice == 5:
                    Hero.lightningMax()
                enemyDamage()
                continue

        if fighter.hp <= 0:
            console.print(enemy.name + " killed you! \n")
            fighter.hp = fighter.hpmax
            homeScreen()
        if mainPlayer == True:
            if (enemy.health <= 0):
                console.print("\nYou have succesfully slain " + enemy.name)
                player.status = ""
                player.poisoned = False
                Hero.status = ""
                Hero.poisoned = False
                player.exp += enemy.exp
            time.sleep(0.5)
            console.print(enemy.name + " dropped " + dropNames)
            global pickup1
            pickup1 = str(input("Would you like to pick them up? (Y/N): ")).upper()
            if pickup1 == "Y":
                itemPickup()

            if pickup1 == "N":
                console.print("You left the items......")
            else:
                while pickup1 != "Y" and pickup1 != "N":
                    pickup1 = str(input("Would you like to pick them up? (Y/N): ")).upper
            pickup = pickup1
            console.print("\nYou gained " + str(enemy.exp) + " exp!")
            if player.exp >= round((4 * (player.level ** 3)) / 5):
                player.level += 1
                player.exp -= player.exp
                console.print("You have reached level " + str(player.level) + "!")
                time.sleep(1)
                temphp = player.hpmax
                player.hpmax = player.hpmax + (2 ** player.level)
                player.hp = player.hpmax
                tempAttck = player.battack
                player.battack += 2 ** player.level
                tempdef = player.bdefense
                player.bdefense += 2 ** player.level
                tempagil = player.agilityMax
                player.agilityMax += 2 ** player.level

                console.print(str(temphp) + " hp --> " + str(player.hpmax) + " hp")
                time.sleep(1)
                console.print(str(tempAttck) + " Attack --> " + str(player.battack) + " Attack")
                time.sleep(1)
                console.print(str(tempdef) + " defense --> " + str(player.bdefense) + " defense")
                time.sleep(1)
                console.print(str(tempagil) + " Agility --> " + str(player.agilityMax) + " Agility")
                time.sleep(1)
                console.print("Health Restored!")
                statsUpdate()

            while True:
                while True:
                    nextMove = int(input("""

                                    [1] Equipment Change
                                    [2] Continue Adventure
                                    [3] Menue

                                    """))
                    if nextMove == 1:
                        equipScreen()
                    elif nextMove == 2:
                        breakOut = True
                        break
                    elif nextMove == 3:
                        inlevelMenue(asd, bsd, csd)
                    else:
                        continue
                if breakOut == True:
                    break

    typingEffect(
        "You spot a town in the distance and see 2 different paths, one is through the forest with many different monsters and the other is filled with 2 giant goblins.\n")
    typingEffect("The town is overrun with monsters, you must save them!\n")

    while True:
        pathChoice = input("""Which path would you like to take?
    
                [1] First Path(Small Monsters)
                [2] Second Path(Giant Goblins)\n \n""")
        if str(pathChoice) == "1":
            typingEffect("Small monster path it is!\n")
            typingEffect(
                "As soon as you start walking on the path, you notice that it is very rocky, and you have no boots\n")
            player.rockyLand(True)
            typingEffect("You are unable to walk as fast as you were before\n")
            typingEffect(
                "You see a small dark particle flying around and go closer to check it out. As you get closer, you see that it is a Dark Fairy, and it is really fast.\nThe dark fairy has noticed you!\n")

            enemy = DarkFairy("The Dark Fairy", False, ["mediumPotion", "smallPotion", "smallPotion"], [], [], [], [],
                              ["Tattred Boots"], 40, "")
            battle1(player, " a Medium Potion, 2 small potions, Tattred Boots and 40 gold", True, True, False, True)
            if player.hp <= 0:
                return False
            if player.bEquip != "":
                player.rockyLand(False)
                console.print("The land was no longer hard to traverse!")
                typingEffect(
                    "You are very relieved that your feet aren't getting stabbed by rocks every step you take.\n")
            typingEffect(
                "You keep walking through the forest until you are unable to move forward. It seems like there is some sort of barrier!\n")
            typingEffect(
                "You suddenly hear a booming voice say \"State your full name and intention truthfully or die!\"\n")
            if str(input("Name: ")).lower() != player.name.lower():
                homeScreen()
            console.print(
                "You state that your intention is to save the people in the town on the other side of the forest that is overrun by gobblins")
            typingEffect("You then try to put your hand through and see that the barrier is lifted\n")
            typingEffect(
                "You take a step but then suddenly everything is turning dark until everything is pitch black\n")
            time.sleep(8)
            clearConsole()
            typingEffect("...........\n", 0.6)
            typingEffect(
                "You slowly open your eyes but everything looks blurry. There is some sort of red figure in the distance.\n")
            typingEffect("What is that? You take a second to refocus your vision", 0.2)
            time.sleep(3)
            print("""
                            /\\
                            ||
                            ||
                            ||
                            ||                                               ~-----~
                            ||                                            /===--  ---~~~
                            ||                   ;'                 /==~- --   -    ---~~~
                            ||                (/ ('              /=----         ~~_  --(  '
                            ||             ' / ;'             /=----               \__~
         '                ~==_=~          '('             ~-~~      ~~~~        ~~~--\~'
         \\\\                (c_\_        .i.             /~--    ~~~--   -~     (     '
          `\               (}| /       / : \           / ~~------~     ~~\   (
          \ '               ||/ \      |===|          /~/             ~~~ \ \(
          ``~\              ~~\  )~.~_ >._.< _~-~     |`_          ~~-~     )\\
           '-~                 {  /  ) \___/ (   \   |` ` _       ~~         '
           \ -~\                -<__/  -   -  L~ -;   \\\\    \ _ _/
           `` ~~=\                  {    :    }\ ,\    ||   _ :(
            \  ~~=\__                \ _/ \_ /  )  } _//   ( `|'
            ``    , ~\--~=\           \     /  / _/ / '    (   '
             \`    } ~ ~~ -~=\   _~_  / \ / \ )^ ( // :_  / '
             |    ,          _~-'   '~~__-_  / - |/     \ (
              \  ,_--_     _/              \_'---', -~ .   \\
               )/      /\ / /\   ,~,         \__ _}     \_  "~_
               ,      { ( _ )'} ~ - \_    ~\  (-:-)       "\   ~ 
                      /'' ''  )~ \~_ ~\   )->  \ :|    _,       " 
                     (\  _/)''} | \~_ ~  /~(   | :)   /          }
                    <``  >;,,/  )= \~__ {{{ '  \ =(  ,   ,       ;
                   {o_o }_/     |v  '~__  _    )-v|  "  :       ,"
                   {/"\_)       {_/'  \~__ ~\_ \\\_} '  {        /~\\
                   ,/!          '_/    '~__ _-~ \_' :  '      ,"  ~ 
                  (''`                  /,'~___~    | /     ,"  \ ~' 
                 '/, )                 (-)  '~____~";     ,"     , }
               /,')                    / \         /  ,~-"       '~'
           (  ''/                     / ( '       /  /          '~'
        ~ ~  ,, /) ,                 (/( \)      ( -)          /~'
      (  ~~ )`  ~}                   '  \)'     _/ /           ~'
     { |) /`,--.(  }'                    '     (  /          /~'
    (` ~ ( c|~~| `}   )                        '/:\         ,'
     ~ )/``) )) '|),                          (/ | \)                 
      (` (-~(( `~`'  )                        ' (/ '
       `~'    )'`')                              '
         ` ``""")
            typingEffect(
                "It's a knight on top of a dragon! Why are you here? You look around and see that you're wearing some sort of shiny armour\n")
            typingEffect("The knight suddenly starts coming for you!")
            hero = Hero(" Unknown", "")
            enemy = DarkKnight(" The Dark Knight", False, [], [], [], [], [], [], 0, '')
            hero.magicAllowed = True


            def battleHero():
                while hero.hp > 0 and enemy.health > 0:
                    console.print("\n")
                    console.print(hero.name + "'s HP: " + str(hero.hp))
                    console.print(enemy.name + "'s HP: " + str(enemy.health))
                    console.print("MP: " + str(hero.magic) + "\n")
                    console.print("""What would you like to do?
                                [1] Attack
                                [2] Defend
                                [3] Item
                                [4] Flee 
                                [5] Magic""")

                    battleD = int(input("\n"))

                    if battleD == 1:

                        if (enemy.agility - hero.agility) / enemy.agility < 0.1:
                            missChancP = random.randrange(1, 1001)
                        elif (enemy.agility - hero.agility) / enemy.agility < 0.25:
                            missChancP = random.randrange(1, 751)
                        elif (enemy.agility - hero.agility) / enemy.agility < 0.5:
                            missChancP = random.randrange(1, 251)
                        elif (enemy.agility - hero.agility) / enemy.agility < 0.75:
                            missChancP = random.randrange(1, 151)
                        elif (enemy.agility - hero.agility) / enemy.agility < 0.85:
                            missChancP = random.randrange(1, 101)
                        elif (enemy.agility - hero.agility) / enemy.agility < 0.9:
                            missChancP = random.randrange(1, 56)
                        elif (enemy.agility - hero.agility) / enemy.agility < 0.95:
                            missChancP = random.randrange(1, 26)
                        elif (enemy.agility - hero.agility) / enemy.agility < 1.:
                            missChancP = random.randrange(1, 11)
                        elif (enemy.agility - hero.agility) / enemy.agility < 2.5:
                            missChancP = random.randrange(1, 3)
                        elif (enemy.agility - hero.agility) / enemy.agility < 5:
                            missChancP = random.randrange(1, 2)

                        if missChancP == 1:
                            console.print("You missed your attack!")
                            battleknight()
                        else:
                            crit = random.randrange(1, critChance)
                            if crit == 1:
                                enemy.health -= round(hero.attack * 1.5)
                                console.print(
                                    "Critical Hit! You did " + str(round(hero.attack * 1.5)) + " damage on the enemy")
                                battleknight()
                                continue
                            else:
                                enemy.health -= hero.attack
                                console.print("You did " + str(hero.attack) + " damage on the enemy!")
                                battleknight()
                                continue

                    if battleD == 2:
                        defenceT = hero.defense
                        if defenceT > enemy.attack:
                            console.print("You defended the attack!")
                            defenceT -= 0.4 * (enemy.attack)
                            battleknight()
                            continue
                        else:
                            console.print("You were unable to defend the attack!")
                            battleknight()
                            continue

                    if battleD == 3:
                        for i in range(0, len(hero.bag)):
                            console.print(str(i + 1) + "." + hero.bag[i])
                        while True:
                            try:
                                bagInput = int(input("What item would you like to use?: "))
                            except ValueError:
                                console.print("")
                            else:
                                break
                        if hero.bag[bagInput - 1] == "smallPotion":
                            hero.smallPotion()
                            battleknight()
                            continue
                        if hero.bag[bagInput - 1] == "mediumPotion":
                            hero.mediumPotion()
                            battleknight()
                            continue
                        if hero.bag[bagInput - 1] == "largePotion":
                            hero.largePotion()
                            battleknight()
                            continue

                    if battleD == 4:
                        if hero.agility > enemy.agility:
                            global flee
                            flee = True
                            homeScreen()
                            break
                        else:
                            console.print("You were unable to flee!")
                            continue

                    if battleD == 5:
                        console.print("""Spells:
                                [1] Fireball
                                    MP Cost: 4
    
                                [2] Lightning
                                    MP Cost: 12
    
                                [3] Sludge
                                    MP Cost: 2
    
                                [4] Fire Blaze
                                    MP Cost: 40
    
                                [5] Lightning Max
                                    MP Cost: 70
    
                                        """)
                        magicChoice = int(input("What spell would you like to use?: "))
                        if magicChoice == 1:
                            hero.fireBall()
                        if magicChoice == 2:
                            hero.lightning()
                        if magicChoice == 3:
                            hero.sludge()
                        if magicChoice == 4:
                            hero.fireBlaze()
                        if magicChoice == 5:
                            hero.lightningMax()
                        battleknight()
                        continue

                if hero.hp <= 0:
                    console.print(enemy.name + " killed you! \n")
                    hero.hp = hero.hpmax
                    homeScreen()


            def battleknight():
                magic = random.randrange(1, 4)
                if (hero.agility - enemy.agility) / hero.agility < 0.1:
                    missChancE = random.randrange(1, 1001)
                elif (hero.agility - enemy.agility) / hero.agility < 0.25:
                    missChancE = random.randrange(1, 751)
                elif (hero.agility - enemy.agility) / hero.agility < 0.5:
                    missChancE = random.randrange(1, 251)
                elif (hero.agility - enemy.agility) / hero.agility < 0.75:
                    missChancE = random.randrange(1, 151)
                elif (hero.agility - enemy.agility) / hero.agility < 0.85:
                    missChancE = random.randrange(1, 101)
                elif (hero.agility - enemy.agility) / hero.agility < 0.9:
                    missChancE = random.randrange(1, 56)
                elif (hero.agility - enemy.agility) / hero.agility < 0.95:
                    missChancE = random.randrange(1, 26)
                elif (hero.agility - enemy.agility) / hero.agility < 1.:
                    missChancE = random.randrange(1, 11)
                elif (hero.agility - enemy.agility) / hero.agility < 2.5:
                    missChancE = random.randrange(1, 3)

                if missChancE == 1:
                    console.print("The enemy missed the attack and did no damage to you!")

                else:
                    if magic == 3 and enemy.mp >= 2:
                        magicRand = random.randrange(1, 6)
                        while magicRand != 7:
                            if enemy.mp > 4 and magicRand == 1:
                                enemy.fireball()
                                magicRand = 7
                                break
                            elif enemy.mp > 12 and magicRand == 2:
                                enemy.lighning()
                                magicRand = 7
                                break
                            elif enemy.mp > 2 and magicRand == 3:
                                enemy.sludge()
                                magicRand = 7
                                break
                            elif enemy.mp > 40 and magicRand == 4:
                                enemy.fireBlaze()
                                magicRand = 7
                                break
                            elif enemy.mp > 70 and magicRand == 5:
                                enemy.lightningMax()
                                magicRand = 7
                                break
                            else:
                                magicRand = random.randrange(1, 6)
                                continue
                    else:
                        critE = random.randrange(1, enemy.critChance)
                        if critE == 1:
                            hero.hp -= (enemy.attack * 2)
                            console.print("Critical Hit! The enemy did " + str(enemy.attack * 2) + " damage to you!")
                        else:
                            hero.hp -= enemy.attack
                            console.print("The enemy damaged you by " + str(enemy.attack) + " hp!")
                if hero.poisoned == True:
                    hero.hp -= round(0.07 * (hero.hpmax))
                    console.print("You lost " + (str(round(0.07 * (hero.hpmax)))) + " points from the poison!")
                if enemy.poisoned == True:
                    enemy.health -= round(0.07 * (enemy.hpmax))
                    console.print("The enemy lost " + str(round(0.07 * (enemy.hpmax))) + " points from poison!")
                if hero.status == "Burning":
                    hero.hp -= round(0.09 * (hero.hpmax))
                    console.print("You lost " + str(round(0.09 * (hero.hpmax))) + " points from burning!")
                if enemy.status == "Burning":
                    Hero.hp -= round(0.09 * (Hero.hpmax))
                    console.print("The enemy lost " + str(round(0.09 * (enemy.hpmax))) + " points from burning!")
                if enemy.status == "Hazed":
                    enemy.attack = 0.9 * (enemy.attack)
                if hero.status == "Hazed":
                    hero.attack = 0.9 * (hero.attack)


            battleHero()

            typingEffect("....", 1)
            clearConsole()

            typingEffect(
                "You wake up back to where you were standing and wonder what just happened. Were you dreaming?\n")
            typingEffect("You rub your face and notice that your hand is glowing. What is happening.\n")
            typingEffect("It stops glowing and you are relieved.\n")
            typingEffect("Then suddenly.....\n")
            clearConsole()
            print("""
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@(*(#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&/../@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@&  .   /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.. ... %@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@(. ......@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@. ..   .*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@&  .       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.  .      %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/.. .. .. . /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/.  ...    .,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,.        .. ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*. .      .. .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#  .. . .. .  /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%    . .  . . #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&* ..  . . . #@@@@@@@@@@@@@@@@@@@@@@@@@@@@   ...  .. ,&@@@@@@@@@@@@@@(@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@&%@@@@@@@@@@@@@@@@@@@%. ...  . @@@@@@@@@@@@@@@@@@@@@@@/ ..  . .%@@@@@@@@@@@@@@@@@@@@*@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@%(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@&.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@, @@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@*.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*,*#@@@@@@@@@(,,,#@@@@@@@@@@@@@@@@@@@@@@@@@@@@# .#@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@(  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&. ...@@@@@ ... (@@@@@@@@@@@@@@@@@@@@@@@@@@@# . &@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@.. @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%./@@@@@(.(@@@@@@@@@@@@@@@@@@@@@@@@@@@@/. . &@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@.  .*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,.@... &@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@* . .#@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ .*#...  &@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@*.. .  (@@  (@  &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@* /@/ #%. ...   &@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@.. %  .,    ...,@( .#@@../@@&#@@@%&@@&(@@*/@@,#@.. %& . *... ...  @&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@. . . ..  . / .. #. . ,#. (@( .#@ .%%. /% .( .  ,. ...,.   &(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@%.  .. ... .   . . ..  %  . @ .,, .    .   . (... @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&..@/.   (.. .,.. .( .. #....& .  .(@  .   *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(.(@#   @%  #&   %@ .  @@.. .#@@&*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&@@@***(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@*#((#(@(,(.((/&*#/%*((/&//#&#@@/((/&*///@@&@@(*@(*@#&(@((#(/@/*@(/(%&(@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@#%&@%&#&&%%%&#@%@#&&%&(@%#&@%%@#%&#@#@@%@@@@@@#@##@(&@%@&#&&&@&@@%#@#(&@@@@@@@@@@@@@@@@@@@@@@@@@@""")
            time.sleep(3)
            clearConsole()
            print("""@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@    %@@@&#%&((,(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#.#(&%/&&@@%    &@@@@@@@@@@@@@@@@@@@@@@@@@
    @&@@@@@@@@@@@@@@@@@@@@@@@& &%#%@*@@@%&,&* &(&&%.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*#%%(@ *&.%&@@@(@%#%& %@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@&&@&@@@@@@@@@@@@@@.%####%.&%#*( &(&#*&&(#%&& #%@(&@@@@@@@@@@@@@@@@@@@@@@@&*&%# &&&%(&@,#&#& (,#%&.%####%,@@@@@@@@@@@@@@@@&@@@@
    @@@@@@&&&&@@@@@@@@@@  ,. //.(##%  ,/ &**#/@@&##(&%*%%/#*/ &@@#@@@@@@@@@@@@& #/##,&&###&@@(%/,&,#   &(%(.// .,  @@@@@@@@@&&&@&&@@@@
    @@@@@@@@@@@@@@@@@ *.           ./(#(* %*%( @.&&%,, /%%#%@@@&&@@@@%@@@@@@@&&%#(%/...%&&,@ /%*% ,%%((.            /.@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@ ,,.  , ,,. ,,       (.,,%(/@@&&&%#.&&%&#&&&&&&&&& &&&&&&&&&#&&&% #%&&&@&/(%.../       ,, .,, ,  ,,, @@@@@@@@@@@@@@
    @@@@@/@@@@@@@&(*,, ,.         /*,  #  */. ( %%%&#@&&&&&&&&&&&&&&&.&&&&&&&%%&&&&&&&#&#%% / ./*  #  ,,/         ., ,,,(@@@@@@@@(@@@@
    @@@@@/@@@@@@@ @/.  ,,,,,..*.  &@@@&/./# .*  %###%#%&&&&&&&&&&&&&&#&&&&&&&&&&%%%@%/#%###  *. %/.*@@@@@ ..*..,,,,,  .*@ &@@@@@@,@@@@
    @@@@@@.@@@@@&@./  , ,*  .**@@@@@@@@@@@//#(#*  /###%%&%&&&&&&&&&&&&&&&&&&%###&#&%####/  *((#*/@@@@@@@@@@@*,.  /, ,  / @@@@@@@,@@@@@
    @@@@@@@&/ @@@@/( ,* .,**  @@@@@@@@@@@@@,* ((  #(##########%&&&&%#%&#&&%###########((#  /(.*.@@@@@@@@@@@@@  **,. *, ((@@@@ *#@@@@@@
    @@@@@@@@@,*( # / %%%./   %@&&&@@@@@@@@@&(*,//.. (#########(###%%%##%############//(.*.//,*#&@@@@@@@&@&&&@&   / %%% / # (*.@@@@@@@@
    @@@@@@@@@@@@@@(* ,*(#/(,(###**/(,@@@@@@@@,,( . //##(#(#(##%##%####%(##%(%%%//////**/.  /* @@@@@@@&*#.*(/##(,(/%//*,*/@@@@@@@@@@@@@
    @@@@@@@@@@@@@@/#, /#.%&*.#(#*(**(/###@@@@%%,* #/*(%%(/((*((#//#/*/#//## %(%(((##//.,/ *, @@@@@%##//*/(#/*#/ &%*//*.#*@@@@@@@@@@@@@
    @@@@@@@@@@@@@@#,(/*/(( #,&&&.,#*/*// #&@@&% ,./((/.,*/(((#%((**(#%(////%###(,/,/.//,, ,  @@@@# //,/*# .%@@ # *#,*/(.(@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@,#% ,*/(%%, &@&   //* ,.@@@ , ./**     /*,*/.((/,/.(.*(((**,*      ./,*./&@@@,* *// . @@@..%%(,/, ## @@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@  /% *%*#%/#( @@ /(*,#(% @@&  /#/,      .        **.  ,,  .         (. ,.@@@.%(#,**/ @@ *%(##*%* %,  @@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@#. ( *,(%%*.%%#.,( */*# @@@@ ,/,   .,. .  .   ,*(**..    .....,,   *.  @@@@*#*// (,.#%%,/%%**, ( ,*@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@#@ % ,.(*,*.,,./ .*,(&@@&  //(  .., . ..   ,.*%/*        ..,.. ,*/,, .@@@@*,*  /,,, **./,, % @%@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@,@@ #%. ,  *.*( .,.@@@@@,**/#/*/###*/.**** *    *   *,  . *((//*/*.  @@@@@,,  (*.*  , .%( @@ &@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@.  *#*,., &@@@@@@@/,.,...  .,,,,,,,.,*     *   .,**//////,*/,/ @@@@@@&& ,.,*#/  .@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ,,             **,      * .          .,,,** @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&@&@&&@&  .**  , ., /* .  * . *.     ,  /  .*&@&&@@&&@&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@&@@@&@ (** *,,,* */  **   ....,   , . *@@@@&@@&@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@&&&&&&@&&/.*  *  .**//*/**.,,, ,. , , /. &&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@./, *( /. * ** . / ..# //,, / ,&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@./ *     &*%#*,(*  *%.&   / . &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&/* (%      &,.    .,/,/((   @@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#*/* //   , ,,/(((/, .(%,, . @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&,,, %, .   , (%@&*(%,##%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&/*.*,.   .   *%%.&@@%(@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/*, /,/ ,.%    #,%@//#.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&@***(,**,,, *  &##%,*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&#*,(*.(/ .%##,.*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.%((  (@@@@,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&//..@@,&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&,/@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@""")
            time.sleep(3)
            clearConsole()
            typingEffect("....\n", 0.4)
            console.print("What")
            time.sleep(1)
            console.print("Was")
            time.sleep(1)
            console.print("That!!!!!")
            console.print("")
            typingEffect("You look around and see that you are in town, but in a daze")

        if str(pathChoice) == "2":
            typingEffect("Giant Goblin path it is!\n")
            typingEffect("The terrain is all flat so it is really easy to traverse!\n")
            console.print("The first Giant goblin in your way spots you!")
            enemy = GiantGoblin(" Giant Goblin #1", False, [], [], ["Rusty Helmet"], [], [], [], 50, "")
            battle1(player, " Rusty Helmet and 50 gold", True, True, False, True)
            typingEffect("It starts raining a lot and there is loud thunder booming\n")
            typingEffect("🆆🅷🅾 🅳🅰🆁🅴🆂 🅲🆁🅾🆂🆂 🅼🆈 🅳🅾🅼🅰🅸🅽\n")
            typingEffect("You get startled and immediately jump back\n")
            clearConsole()
            console.print("""                 .eeeeeeeee
                    .$$$$$$$$P\"
                   .$$$$$$$$P
                  z$$$$$$$$P
                 z$$$$$$$$\"
                z$$$$$$$$\"
               d$$$$$$$$\"
              d$$$$$$$$\"
            .d$$$$$$$P
           .$$$$$$$$P
          .$$$$$$$$$.........
         .$$$$$$$$$$$$$$$$$$\"
        z$$$$$$$$$$$$$$$$$P\"
       -**********$$$$$$$P
                 d$$$$$$\"
               .d$$$$$$\"
              .$$$$$$P\"
             z$$$$$$P
            d$$$$$$\"
          .d$$$$$$\"
         .$$$$$$$\"
        z$$$$$$$beeeeee
       d$$$$$$$$$$$$$*
      ^\"\"\"\"\"\"\"\"$$$$$\"
              d$$$*
             d$$$\"
            d$$*
           d$P\"
         .$$\"
        .$P\"
       .$\"
      .P\"
     .\"     
    /\"""")
            clearConsole()
            typingEffect("Suddenly, lightning strikes in front of you\n \n")
            typingEffect("Your puny little tooth pick can't do anything to me so I suggest you lower it\n")
            print("""     __/)     (\__
      ,-'~~(   _   )~~`-.
     /      \/'_`\/      \
    |       /_(_)_\       |
    |     _(/(\_/)\)_     |
    |    / // \ / \\ \    |
     \  | ``  / \ ''  |  /
      \  )   /   \   (  /
       )/   /     \   \(
       '    `-`-'-'    `""")
            typingEffect("Its an Angel!\n")
            typingEffect("I bestow upon you the great blessing of the gods\n")
            console.print("\n")
            typingEffect("You suddenly felt much more power surging through your veins!\n")
            player.attack += 5
            typingEffect("The angel suddenly dissapeared and you were left very confused\n")
            enemy = GiantGoblin(" Giant Goblin #2", False, [], [], [], [], [], [], 50, "")
            typingEffect("You walk a few more steps and inspect the place\n")
            typingEffect("The goblin charges at you!\n")
            battle1(player, " 50 gold", True, True, False, True)
            typingEffect("You make your way to town\n")

        else:
            if str(input("Would you like to take an alternate path?: (Y/N) \n")).upper() == "Y":
                typingEffect(
                    "You started walking on the alternate path and felt a very dark aura.... Almost as if the land itself was imbued with some sort of dark energy \n")
                typingEffect("A dark figure with horns and eyes suddenly appears in front of you!")
                enemy = Lucifer("Lucifer", False, [], [], [], [], [], [], 10000000000000, "")
                battle1(player, " nothing", True, True, False, True)

        break
    level2P = True
    homeScreen(True, True, False)

def level3():
    clearConsole()
    print("""             ('-.        (`-.      ('-.                           
           _(  OO)     _(OO  )_  _(  OO)                          
 ,--.     (,------.,--(_/   ,. \(,------.,--.            .-----.  
 |  |.-')  |  .---'\   \   /(__/ |  .---'|  |.-')       /  -.   \ 
 |  | OO ) |  |     \   \ /   /  |  |    |  | OO )      '-' _'  | 
 |  |`-' |(|  '--.   \   '   /, (|  '--. |  |`-' |         |_  <  
(|  '---.' |  .--'    \     /__) |  .--'(|  '---.'      .-.  |  | 
 |      |  |  `---.    \   /     |  `---.|      |       \ `-'   / 
 `------'  `------'     `-'      `------'`------'        `----''  """"")
    def battle1(fighter, dropNames, asd, bsd, csd, mainPlayer):
        while fighter.hp > 0 and enemy.health > 0:
            console.print("\n")
            console.print(fighter.name + "'s HP: " + str(fighter.hp))
            console.print(enemy.name + "'s HP: " + str(enemy.health))
            console.print("MP: " + str(fighter.magic) + "\n")
            console.print("""What would you like to do?
                    [1] Attack
                    [2] Defend
                    [3] Item
                    [4] Flee """)
            if fighter.magic:
                console.print("         [5] Magic")

            battleD = int(input("\n"))

            if battleD == 1:

                if (enemy.agility - fighter.agility) / enemy.agility < 0.1:
                    missChancP = random.randrange(1, 1001)
                elif (enemy.agility - fighter.agility) / enemy.agility < 0.25:
                    missChancP = random.randrange(1, 751)
                elif (enemy.agility - fighter.agility) / enemy.agility < 0.5:
                    missChancP = random.randrange(1, 251)
                elif (enemy.agility - fighter.agility) / enemy.agility < 0.75:
                    missChancP = random.randrange(1, 151)
                elif (enemy.agility - fighter.agility) / enemy.agility < 0.85:
                    missChancP = random.randrange(1, 101)
                elif (enemy.agility - fighter.agility) / enemy.agility < 0.9:
                    missChancP = random.randrange(1, 56)
                elif (enemy.agility - fighter.agility) / enemy.agility < 0.95:
                    missChancP = random.randrange(1, 26)
                elif (enemy.agility - fighter.agility) / enemy.agility < 1.:
                    missChancP = random.randrange(1, 11)
                elif (enemy.agility - fighter.agility) / enemy.agility < 2.5:
                    missChancP = random.randrange(1, 3)
                elif (enemy.agility - fighter.agility) / enemy.agility < 5:
                    missChancP = random.randrange(1, 2)

                if missChancP == 1:
                    console.print("You missed your attack!")
                    enemyDamage()
                else:
                    crit = random.randrange(1, critChance)
                    if crit == 1:
                        enemy.health -= (fighter.attack * 1.5)
                        console.print("Critical Hit! You did " + str(fighter.attack * 1.5) + " damage on the enemy")
                        enemyDamage()
                        continue
                    else:
                        enemy.health -= fighter.attack
                        console.print("You did " + str(player.attack) + " damage on the enemy!")
                        enemyDamage()
                        continue

            if battleD == 2:
                defenceT = fighter.defense
                if defenceT > enemy.attack:
                    console.print("You defended the attack!")
                    defenceT -= 0.4 * (enemy.attack)
                    enemyDamage()
                    continue
                else:
                    console.print("You were unable to defend the attack!")
                    enemyDamage()
                    continue

            if battleD == 3:
                for i in range(0, len(fighter.bag)):
                    console.print(str(i + 1) + "." + fighter.bag[i])
                while True:
                    try:
                        bagInput = int(input("What item would you like to use?: "))
                    except ValueError:
                        console.print("")
                    else:
                        break
                if fighter.bag[bagInput - 1] == "smallPotion":
                    fighter.smallPotion()
                    enemyDamage()
                    continue
                if fighter.bag[bagInput - 1] == "mediumPotion":
                    fighter.mediumPotion()
                    enemyDamage()
                    continue
                if fighter.bag[bagInput - 1] == "largePotion":
                    fighter.largePotion()
                    enemyDamage()
                    continue

            if battleD == 4:
                if fighter.agility > enemy.agility:
                    global flee
                    flee = True
                    homeScreen()
                    break
                else:
                    console.print("You were unable to flee!")
                    continue

            if battleD == 5:
                console.print("""Spells:
                    [1] Fireball
                        MP Cost: 4

                    [2] Lightning
                        MP Cost: 12

                    [3] Sludge
                        MP Cost: 2

                    [4] Fire Blaze
                        MP Cost: 40

                    [5] Lightning Max
                        MP Cost: 70

                            """)
                magicChoice = int(input("What spell would you like to use?: "))
                if magicChoice == 1:
                    Hero.fireBall()
                if magicChoice == 2:
                    Hero.lightning()
                if magicChoice == 3:
                    Hero.sludge()
                if magicChoice == 4:
                    Hero.fireBlaze()
                if magicChoice == 5:
                    Hero.lightningMax()
                enemyDamage()
                continue

        if fighter.hp <= 0:
            console.print(enemy.name + " killed you! \n")
            fighter.hp = fighter.hpmax
            homeScreen()
        if mainPlayer == True:
            if (enemy.health <= 0):
                console.print("\nYou have succesfully slain " + enemy.name)
                player.status = ""
                player.poisoned = False
                Hero.status = ""
                Hero.poisoned = False
                player.exp += enemy.exp
            time.sleep(0.5)
            console.print(enemy.name + " dropped " + dropNames)
            global pickup1
            pickup1 = str(input("Would you like to pick them up? (Y/N): ")).upper()
            if pickup1 == "Y":
                itemPickup()

            if pickup1 == "N":
                console.print("You left the items......")
            else:
                while pickup1 != "Y" and pickup1 != "N":
                    pickup1 = str(input("Would you like to pick them up? (Y/N): ")).upper
            pickup = pickup1
            console.print("\nYou gained " + str(enemy.exp) + " exp!")
            if player.exp >= round((4 * (player.level ** 3)) / 5):
                player.level += 1
                player.exp -= player.exp
                console.print("You have reached level " + str(player.level) + "!")
                time.sleep(1)
                temphp = player.hpmax
                player.hpmax = player.hpmax + (2 ** player.level)
                player.hp = player.hpmax
                tempAttck = player.battack
                player.battack += 2 ** player.level
                tempdef = player.bdefense
                player.bdefense += 2 ** player.level
                tempagil = player.agilityMax
                player.agilityMax += 2 ** player.level

                console.print(str(temphp) + " hp --> " + str(player.hpmax) + " hp")
                time.sleep(1)
                console.print(str(tempAttck) + " Attack --> " + str(player.battack) + " Attack")
                time.sleep(1)
                console.print(str(tempdef) + " defense --> " + str(player.bdefense) + " defense")
                time.sleep(1)
                console.print(str(tempagil) + " Agility --> " + str(player.agilityMax) + " Agility")
                time.sleep(1)
                console.print("Health Restored!")
                statsUpdate()

            while True:
                while True:
                    nextMove = int(input("""

                                    [1] Equipment Change
                                    [2] Continue Adventure
                                    [3] Menue

                                    """))
                    if nextMove == 1:
                        equipScreen()
                    elif nextMove == 2:
                        breakOut = True
                        break
                    elif nextMove == 3:
                        inlevelMenue(asd, bsd, csd)
                    else:
                        continue
                if breakOut == True:
                    break
    typingEffect("You finally make it to town and the goblins are oddly making way for you to go\n")
    typingEffect("You see a giant ogre come out from the center, this must be their boss......\n")
    enemy = bossOgre("The Boss Ogre", True, [], [], [], [], [], [], 100, "")
    battle1(player, "100 gold", True, True, False, True)
    typingEffect("You beat the boss and successfully rescue all the town's citizens")
    typingEffect("The end....... for now")
    homeScreen(True, True, True)


def itemPickup():
    if len(player.bag) < 20:
        for i in range(0, len(enemy.items)):
            player.bag.append(enemy.items[i])
        for i in range(0, len(enemy.weapons)):
            player.weapons.append(enemy.weapons[i])
        for i in range(0, len(enemy.headArmour)):
            player.headArmour.append(enemy.headArmour[i])
        for i in range(0, len(enemy.chestArmour)):
            player.chestArmour.append(enemy.chestArmour[i])
        for i in range(0, len(enemy.legArmour)):
            player.legArmour.append(enemy.legArmour[i])
        for i in range(0, len(enemy.boots)):
            player.boots.append(enemy.boots[i])
        player.gold += enemy.gold
    if len(player.bag) >= 20:
        while player.bag >= 20:
            removeItem = str(input("Would you like to remove an item? (Y/N): ")).upper()
            if removeItem == "Y":
                console.print("Which item would you like to remove?")
                for i in range(0, len(player.bag) - 1):
                    console.print(str(i + 1) + ". " + player.bag[i])
                itemremovenum = int(input(""))
                player.bag.remove(itemremovenum - 1)
                continue
            if removeItem == "N":
                console.print("You left the items")
                return True


homeScreen()


