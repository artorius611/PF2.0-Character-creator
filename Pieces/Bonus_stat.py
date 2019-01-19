from Pieces import Ancestry
from Pieces import Race

class Bonus_Stat :
    def __init__ (self, strength, dexterity, constitution, intelligence, wisdom, charisma, health, speed, heritage_bonus, dwarf, gimli) :
        self.dexterity = dexterity 
        self.wisdom = wisdom 
        self.strength = strength 
        self.constitution = constitution 
        self.intelligence = intelligence 
        self.charisma = charisma
        self.health = health
        self.speed = speed
        self.dwarf = 0
        self.gimli = 0
        race = Race.Selection(choice)
        if race == 1 :
            bonus_race = Ancestry.Dwarf (strength, dexterity, constitution, intelligence, wisdom, charisma, health, speed, heritage_bonus, dwarf, gimli)
            while bonus_user_input == 0:
                print ('\nWhat is your bonus stat?\n')
                print ('1) Str')
                print ('2) Dex')
                print ('3) Int')
                print ('4) Cha')
                choice = int(input(''))
                bonus = 2
                if choice == 1 :
                    bonus_user_input = 1
                    bonus_race.strength = bonus_race.strength + bonus
                elif choice == 2 :
                    bonus_user_input = 1
                    bonus_race.dexterity = bonus_race.dexterity + bonus
                elif choice == 3 :
                    bonus_user_input = 1
                    bonus_race.intelligence = bonus_race.intelligence + bonus
                elif choice == 4 :
                    bonus_user_input = 1
                    bonus_race.charisma = bonus_race.charisma + bonus
                else:
                    print ('\nYou selected something invalid\n')
                # the string below clears the screen
                os.system ('cls')
        else : 
            while self.bonus_user_input <= 1:
                print ('\nWhat is your bonus stat?\n')
                print ('1) Str')
                print ('2) Dex')
                print ('3) Con')
                print ('4) Int')
                print ('5) Wis')
                print ('6) Cha')
                choice = int(input(''))
                print (choice)
                bonus = 2
                if choice == 1 :
                    if self.bonus_user_input == 1 :
                        print ('you cant select the same bonus')
                    else :
                        self.bonus_user_input = self.bonus_user_input + 1
                        bonus_race.strength = bonus_race.strength + bonus
                elif choice == 2 :  
                    if self.bonus_user_input == 1 :
                        print ('you cant select the same bonus')
                    else :
                        self.bonus_user_input = self.bonus_user_input + 1
                        bonus_race.dexterity = bonus_race.dexterity + bonus
                elif choice == 3 :
                    if self.bonus_user_input == 1 :
                        print ('you cant select the same bonus')
                    else :
                        self.bonus_user_input = self.bonus_user_input + 1
                        bonus_race.constitution = bonus_race.constitution + bonus
                elif choice == 4 :
                    if self.bonus_user_input == 1 :
                        print ('you cant select the same bonus')
                    else :
                        self.bonus_user_input = self.bonus_user_input + 1
                        bonus_race.intelligence = bonus_race.intelligence + bonus
                elif choice == 5 :
                    if self.bonus_user_input == 1 :
                        print ('you cant select the same bonus')
                    else :
                        self.bonus_user_input = self.bonus_user_input + 1
                        bonus_race.wisdom = bonus_race.wisdom + bonus
                elif choice == 6 :
                    if self.bonus_user_input == 1 :
                        print ('you cant select the same bonus')
                    else :
                        self.bonus_user_input = self.bonus_user_input + 1
                        bonus_race.charisma = bonus_race.charisma + bonus
                else:
                    print ('\nYou selected something invalid\n')
                # the string below clears the screen
                os.system ('cls')
