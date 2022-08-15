import time
import sys
import random

# support function


def pause(message):
    print(message)
    time.sleep(5)


# Player health and attack
life = 70

attack = 15

# Equipment Booleans

excalibur = False

adamantine = False

# Fathers health and attack

dad_life = 300

dad_attack = 50

# crystal mage health and attack

mage_life = 55

mage_attack = 20

# bog monster health and attack
monster_life = 15

monster_attack = 2


def Acquired_Excalibur():

    global excalibur

    global attack

    attack += 50

    excalibur = True


def Acquired_Adamantine():

    global adamantine

    global life

    life += 180

    adamantine = True


def fight_bog_monster(life, attack, monster_life, monster_attack):

    while(True):
        chance = random.randint(1, 2)
        if chance == 1:
            pause("You attack the bog monster with your broadsword. 15 damage")
            monster_life -= attack

        else:
            pause(" The bog monster spits sludge at you. 2 damage ")
            life -= 2

        if life <= 0:
            pause("You have perished!")

            pause("Do you want to play again?")

            print("Please choose either y or n")

            val = input()

            while(True):
                if val == 'y':
                    game()
                elif val == 'n':
                    print("Thank you for playing! Goodbye")
                    with open('GameOver.txt', 'r') as f:
                        for line in f:
                            print(line.rstrip())
                    sys.exit()
                else:
                    print("Please choose either y or n")

        if monster_life < 0:
            pause("You slayed the bog monster.")
            pause("From its corpse you pull out a sword.")
            pause("It seems to be called Excalibur")

            with open('Excalibur.txt', 'r') as f:
                for line in f:
                    print(line.rstrip())
            pause("You replace your broadsword with it")

            pause("You head back towards the sign")

            Acquired_Excalibur()

            three_signs_choice()


def fight_crystal_mage(life, attack, Excalibur, mage_attack, mage_life):

    while(True):
        chance = random.randint(1, 2)
        if chance == 1 and excalibur is False:
            pause("You attack the crystal mage with your broadsword.")
            pause("It doesnt seem to be effective against its crystal hide")
            mage_life -= attack
        elif chance == 1 and excalibur is True:
            pause("You swing at the crystal mage with excalibur. ")
            pause("You do immense damage to the creature")
            pause("You deal " + str(attack) + " damage")
            mage_life -= attack
        else:
            pause("The crystal mage uses the super attack Crystal Cataclysm.")
            pause("Sharp crystals rain down on you from above")
            pause("Crystal Mage deals " + str(mage_attack) + " damage")
            life -= mage_attack

        if life <= 0:
            pause("You have perished!")

            pause("Do you want to play again?")

            print("Please choose either y or n")

            val = input("Please type your reponse here: ")

            while(True):
                if val == 'y':
                    game()
                elif val == 'n':
                    print("Thank you for playing! Goodbye")
                    with open('GameOver.txt', 'r') as f:
                        for line in f:
                            print(line.rstrip())
                    sys.exit()
                else:
                    print("Please choose either y or n")

        if mage_life <= 0:
            pause("The crystal mage explodes in a flash of light. ")
            pause("You acquired the holy adamantine shield.")
            pause("It can protect against curses!")

            with open('AdamantineShield.txt', 'r') as f:
                for line in f:
                    print(line.rstrip())

            Acquired_Adamantine()

            pause("You head back to the way you came across the plains")

            three_signs_choice()


def fight_father(player_life, player_attack, Excalibur, dad_life, dad_attack):
    while(True):
        chance = random.randint(1, 2)
        if chance == 1 and excalibur is False:
            pause("You attack your father with the broadsword.")
            pause("It doesnt even faze him")
            dad_life -= player_attack

        elif chance == 1 and excalibur is True:
            pause("You cut your father with excalibur.")
            pause("You managed to damage him somewhat.")
            pause("You deal " + str(player_attack) + " damage")
            dad_life -= player_attack
        else:
            pause("Your father uses the dark magic, 'The BlightMaster'! ")
            pause("The darkness destroys everything in its path. ")
            pause("He deals " + str(dad_attack) + " damage")
            player_life -= dad_attack

        if player_life <= 0:
            pause("You have perished!")

            pause("Do you want to play again?")

            print("Please choose either y or n")

            val = input()

            while(True):
                if val == 'y':
                    game()
                elif val == 'n':
                    print("Thank you for playing! Goodbye")
                    with open('GameOver.txt', 'r') as f:
                        for line in f:
                            print(line.rstrip())
                    sys.exit()
                else:
                    print("Please choose either y or n")

        if dad_life <= 0:
            pause("Dad: I am sorry it had to come to this son....")
            pause("Dad: Here, take this magic and may it prove useful to you.")
            pause("Dad: Good luck....")
            pause(" You have inherited 'The BlightMaster'! ")
            pause("You managed to defeat your father")
            pause("You continue onwards.....")

            pause("Thanks for playing!")

            pause("Do you want to play again?")

            print("Please choose either y or n")

            val = input()

            while(True):
                if val == 'y':
                    game()
                elif val == 'n':
                    print("Thank you for playing! Goodbye")
                    with open('TheEnd.txt', 'r') as f:
                        for line in f:
                            print(line.rstrip())
                    sys.exit()
                else:
                    print("Please choose either y or n")


# Location functions
def three_signs_choice():

    global excalibur

    global adamantine

    if excalibur is True and adamantine is True:
        pause("You approach a field that spreads out in all directions")

        pause(" Looks like there are three signs in the middle")

        with open('signFinal.txt', 'r') as f:
            for line in f:
                print(line.rstrip())

    else:

        pause("You approach a field that spreads out in all directions")

        pause(" Looks like there are three signs in the middle")

        with open('sign.txt', 'r') as f:
            for line in f:
                print(line.rstrip())

    print("Where do you want to go ? ")

    pause("Choose 1 to go to the aurora cave")

    pause("Press 2 to go to the marsh")

    pause("Press 3 to go to the lonely house")

    while(True):
        val = input("Type a value here: ")
        if val == "1" and adamantine is False:
            aurora_cave()
        elif val == "1" and adamantine is True:
            aurora_cave_2()
        elif val == "2" and excalibur is False:
            marsh()
        elif val == "2" and excalibur is True:
            marsh_2()
        elif val == "3":
            the_lonely_house()
        else:
            print("Please choose a value that is either 1,2 or 3")


def marsh():
    pause("You go straight towards the marsh")

    pause("As you advance forward you notice the terrain start to change.")

    pause("The plants seem to be different then normal.")

    pause(" Eventually a huge bog comes into view ")

    with open('marsh.txt', 'r') as f:
        for line in f:
            print(line.rstrip())

    pause(" Suddenly a huge amorphous blob rises from the marsh.")

    pause("You see something glowing inside of it")

    pause(" What do you want to do?")

    pause("Choose 1 to fight the monster")

    pause("Choose 2 to runaway")

    while(True):
        val = input("Please type your response here: ")

        if val == "1":
            pause("You approach the monster and prepare to fight")

            fight_bog_monster(life, attack, monster_life, monster_attack)
        elif val == "2":
            pause("You runaway to fight again another day")

            pause("You head back to the three signs")

            three_signs_choice()


def marsh_2():
    pause("You go straight towards the marsh")

    pause("You start seeing weird vegetation. Cattails and things like that")

    pause("You suddenly come across a huge bog")

    with open('marsh2.txt', 'r') as f:
        for line in f:
            print(line.rstrip())

    pause("You defeated the bog monster here. There is nothing else to do")

    pause("You head back to the signs")

    three_signs_choice()


def aurora_cave():
    pause("You take a left towards the aurora cave")

    pause("You walk across the plain for what felt like hours")

    pause("You eventually see  a mountain in the distance")

    with open('Mountain.txt', 'r') as f:
        for line in f:
            print(line.rstrip())

    pause(' You enter the cave and see an amazing view. ')

    pause("Diamond trees as far as the eye can see.")

    pause(" You see a house that seems to be out of place")

    with open('CaveInterior2.txt', 'r') as f:
        for line in f:
            print(line.rstrip())

    pause("What do you want to do?")

    pause("Choose 1 to knock on the door")

    pause("Choose 2 to go back to the signs")


    while(True):
        val = input("Please type your response here: ")

        if val == "1":

            pause("You knock on the door of the house")

            pause("The door opens forcefully and knocks you on your back.")

            pause(" The crystal mage steps forward from the house")

            pause(" It has no face but you can clearly sense its malice")

            pause(" The crystal mage attacks!")

            fight_crystal_mage(attack, life, excalibur, mage_attack, mage_life)

        elif val == "2":
            pause("You decide to leave. ")
            pause("You head back the way you came towards the three signs")

            three_signs_choice()
        else:
            pause("Please choose a value that is either 1 or 2")


def aurora_cave_2():
    pause("You take a left towards the Aurora Cave")

    pause("You walk for what feels like hours")

    pause("You see a mountain in the distance")

    with open('Mountain2.txt', 'r') as f:
        for line in f:
            print(line.rstrip())

    pause("You enter the mountain cave")

    pause("and come across a beautiful landscape made of crystal.")

    with open('CaveInterior.txt', 'r') as f:
        for line in f:
            print(line.rstrip())

    pause("There is a house in the middle. ")

    pause("The crystal mage was destroyed here.")

    pause("There is nothing left do do")

    pause("You head back outside the cave and towards the signs")

    three_signs_choice()


def the_lonely_house():
    pause("You take a right towards the lonely house")

    pause("The heat of the sun seemed to get weaker the further you went.")

    pause("It feels unnatural...")

    pause(" Eventually you reach a small house ")

    pause("with mountains in the background surrounded by strange trees")

    with open('TheHouse.txt', 'r') as f:
        for line in f:
            print(line.rstrip())

    pause("You climb up the stairs towards the door")

    pause(" What do you want to do?")

    print("Choose 1 to knock on the door")

    print("Choose 2 to go back the way you came")

    while(True):
        value = input("Please choose a value: ")

        if value == "1":
            pause("You knock on the door of the house")

            pause("A man opens the door")

            if excalibur is False and adamantine is False:

                pause("He looks really disheveled ")

                pause("and his hair seems to cover his face")

                pause(" Strange Man: What do you want? ")

                pause("Can't you see that I want to be left alone.")

                pause("Why else would I be out here?")

                pause(" Strange Man: I see, you are looking for your father.")

                pause("I would recommend getting much stronger.")

                pause(" Go collect both the Excalibur")

                pause("from the Bog monster in the Marsh")

                pause("and the Holy adamantine shield")

                pause("from the crystal mage in the aurora cave")

                pause("You leave the house to search for the other areas.")

                three_signs_choice()

            elif excalibur is True and adamantine is False:
                pause("You have excalibur")

                pause("but you still need the adamantine shield.")

                pause("Go to the aurora cave and acquire it")

                pause("You leave the house to search for the other areas.")

                three_signs_choice()

            elif excalibur is False and adamantine is True:
                pause("You have the adamantine shield")

                pause("but you still need the excalibur.")

                pause("Go to the marsh and claim it")

                pause("You leave the house to search for the other areas.")

                three_signs_choice()

            else:
                pause("Strange Man: Looks like you have everything.....")

                pause("Strange Man: Sorry...")

                pause("I haven't been entirely honest with you....")

                pause("Dad: I am your father.")

                pause("Dad: The Darkness attached itself to me.")

                pause("Dad: I couldnt bring it back home")

                pause("Dad: so I exiled myself to THE PLAINS")

                pause("Dad: I have been watching your progress")

                pause("Dad: Remember this?")

                with open('flower.txt', 'r') as f:
                    for line in f:
                        print(line.rstrip())

                pause("These flowers allowed me to see your growth.")

                pause(" I am happy to see that you have been getting stronger")

                pause("You are a true warrior now...")

                pause("Dad: Its time to see if you are worthy. ")

                pause("of inheriting this power I now wield")

                pause("Dad: I will not go easy on you..... ")

                pause(" Your father approaches. ")

                pause("The darkness he wields is overbearing.")

                pause("Time to end this nightmare")

                fight_father(life, attack, excalibur, dad_life, dad_attack)

        elif value == "2":
            pause("You turn away and head back the way you came.")

            three_signs_choice()

        else:
            print("Please choose a value that is either 1 or 2")


# Main function
def game():

    with open('GameIntroduction.txt', 'r') as f:
        for line in f:
            print(line.rstrip())

    pause(" You are an adventurer. ")

    pause("he unknown is a source of great inspiration")

    pause("and drives you towards undiscovered lands")

    pause(" Your father was a well known nomad")

    pause("who dissapeared in a mysterious place known only as THE PLAINS")

    pause(" Rumors have been circling throughout the land ")

    pause("that there is a dark power that has taken root in that place")

    pause(" You leave the house and head out to the east")

    three_signs_choice()


# start the game
game()
