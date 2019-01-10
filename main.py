import os 
from Race import Ancestry

strength = 10
dexterity = 10
constitution = 10
intelligence = 10
wisdom = 10
charisma = 10
health = 0
speed = 0
heritage_bonus = 0

class Bonus_Stat :
    def __init__ (self, strength, dexterity, constitution, intelligence, wisdom, charisma) :
        self.dexterity = dexterity + 2
        self.wisdom = wisdom + 2
        self.strength = strength + 2
        self.constitution = constitution + 2
        self.intelligence = intelligence + 2
        self.charisma = charisma + 2

valid_user_input = "false"
while valid_user_input == "false" :
    print ('\nWhat is your Ancestry?\n')
    print ('1) Halfling')
    print ()
    choice = input('Which Ancestry do you choose? ')
    if choice == '1' :
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
    else:
        print ('\n \nYou selected something invalid\n \n')
    # the string below clears the screen
    os.system ('cls')


print ('Your Health is:', user_race.health, '\nYour Speed is: ', user_race.speed, 'ft. \n STR:', user_race.strength, '\n Dex', user_race.dexterity, '\n Con', user_race.constitution, '\n Int', user_race.intelligence, '\n Wis', user_race.wisdom, '\n Cha', user_race.charisma, '\nYour heritage:\n',  user_race.heritage_bonus)
