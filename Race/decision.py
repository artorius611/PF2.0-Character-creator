import os
import Ancestry
import Bonus_stat

class Decision () :
    def __init__ (self, strength, dexterity, constitution, intelligence, wisdom, charisma) :
        self.dexterity = dexterity
        self.wisdom = wisdom
        self.strength = strength
        self.constitution = constitution
        self.intelligence = intelligence
        self.charisma = charisma
        valid_user_input = "false"
        while valid_user_input == "false" :
            print ('\nWhat is your Ancestry?\n')
            print ('1) Dwarf')
            print ('2) Elf')
            print ('3) Gnome')
            print ('4) Goblin')
            print ('5) Halfling')
            print ('6) Human')
            choice = input('Which Ancestry do you choose? ')
            if choice == '1' :
                valid_user_input = "true"
                user_race = Ancestry.Dwarf (strength, dexterity, constitution, intelligence, wisdom, charisma, health, speed, heritage_bonus)
                bonus_user_input = "true"
                while bonus_user_input == "true":
                    print ('\nWhat is your bonus stat?\n')
                    print ('1) Str')
                    print ('2) Dex')
                    print ('3) Int')
                    print ('4) Cha')
                    choice = int(input(''))
                    print (choice)
                    bonus = 2
                    if choice == 1 :
                        bonus_user_input = "false"
                        user_race.strength = user_race.strength + bonus
                    elif choice == 2 :
                        bonus_user_input = "false"
                        user_race.dexterity = user_race.dexterity + bonus
                    elif choice == 3 :
                        bonus_user_input = "false"
                        user_race.intelligence = user_race.intelligence + bonus
                    elif choice == 4 :
                        bonus_user_input = "false"
                        user_race.charisma = user_race.charisma + bonus
                    else:
                        print ('\nYou selected something invalid\n')
                    # the string below clears the screen
                    os.system ('cls')
            elif choice == '2' :
                valid_user_input = "true"
                user_race = Ancestry.Elf (strength, dexterity, constitution, intelligence, wisdom, charisma, health, speed, heritage_bonus)
                bonus_user_input = "true"
                while bonus_user_input == "true":
                    print ('\nWhat is your bonus stat?\n')
                    print ('1) Str')
                    print ('2) Con')
                    print ('3) Wis')
                    print ('4) Cha')
                    choice = int(input(''))
                    print (choice)
                    bonus = 2
                    if choice == 1 :
                        bonus_user_input = "false"
                        user_race.strength = user_race.strength + bonus
                    elif choice == 2 :
                        bonus_user_input = "false"
                        user_race.constitution = user_race.constitution + bonus
                    elif choice == 3 :
                        bonus_user_input = "false"
                        user_race.wisdom = user_race.wisdom + bonus
                    elif choice == 4 :
                        bonus_user_input = "false"
                        user_race.charisma = user_race.charisma + bonus
                    else:
                        print ('\nYou selected something invalid\n')
                    # the string below clears the screen
                    os.system ('cls')
            elif choice == '3' :
                valid_user_input = "true"
                user_race = Ancestry.Gnome (strength, dexterity, constitution, intelligence, wisdom, charisma, health, speed, heritage_bonus)
                bonus_user_input = "true"
                while bonus_user_input == "true":
                    print ('\nWhat is your bonus stat?\n')
                    print ('1) Str')
                    print ('2) Dex')
                    print ('3) Wis')
                    print ('4) Int')
                    choice = int(input(''))
                    print (choice)
                    bonus = 2
                    if choice == 1 :
                        bonus_user_input = "false"
                        user_race.strength = user_race.strength + bonus
                    elif choice == 2 :
                        bonus_user_input = "false"
                        user_race.dexterity = user_race.dexterity + bonus
                    elif choice == 3 :
                        bonus_user_input = "false"
                        user_race.wisdom = user_race.wisdom + bonus
                    elif choice == 4 :
                        bonus_user_input = "false"
                        user_race.intelligence = user_race.intelligence + bonus
                    else:
                        print ('\nYou selected something invalid\n')
                    # the string below clears the screen
                    os.system ('cls')
            elif choice == '4' :
                valid_user_input = "true"
                user_race = Ancestry.Goblin (strength, dexterity, constitution, intelligence, wisdom, charisma, health, speed, heritage_bonus)
                bonus_user_input = "true"
                while bonus_user_input == "true":
                    print ('\nWhat is your bonus stat?\n')
                    print ('1) Str')
                    print ('2) Con')
                    print ('3) Wis')
                    print ('4) Int')
                    choice = int(input(''))
                    print (choice)
                    bonus = 2
                    if choice == 1 :
                        bonus_user_input = "false"
                        user_race.strength = user_race.strength + bonus
                    elif choice == 2 :
                        bonus_user_input = "false"
                        user_race.constitution = user_race.constitution + bonus
                    elif choice == 3 :
                        bonus_user_input = "false"
                        user_race.wisdom = user_race.wisdom + bonus
                    elif choice == 4 :
                        bonus_user_input = "false"
                        user_race.intelligence = user_race.intelligence + bonus
                    else:
                        print ('\nYou selected something invalid\n')
                    # the string below clears the screen
                    os.system ('cls')
            elif choice == '5' :
                valid_user_input = "true"
                user_race = Ancestry.Halfling (strength, dexterity, constitution, intelligence, wisdom, charisma, health, speed, heritage_bonus)
                bonus_user_input = "true"
                while bonus_user_input == "true":
                    print ('\nWhat is your bonus stat?\n')
                    print ('1) Str')
                    print ('2) Con')
                    print ('3) Int')
                    print ('4) Cha')
                    choice = int(input(''))
                    print (choice)
                    bonus = 2
                    if choice == 1 :
                        bonus_user_input = "false"
                        user_race.strength = user_race.strength + bonus
                    elif choice == 2 :
                        bonus_user_input = "false"
                        user_race.constitution = user_race.constitution + bonus
                    elif choice == 3 :
                        bonus_user_input = "false"
                        user_race.intelligence = user_race.intelligence + bonus
                    elif choice == 4 :
                        bonus_user_input = "false"
                        user_race.charisma = user_race.charisma + bonus
                    else:
                        print ('\nYou selected something invalid\n')
                    # the string below clears the screen
                    os.system ('cls')
            elif choice == '6' :
                valid_user_input = "true"
                user_race = Ancestry.Human (strength, dexterity, constitution, intelligence, wisdom, charisma, health, speed, heritage_bonus)
                bonus_user_input = Bonus_stat.Bonus_Stat(strength, dexterity, constitution, intelligence, wisdom, charisma)
            else:
                print ('\n \nYou selected something invalid\n \n')
            # the string below clears the screen
            os.system ('cls')
