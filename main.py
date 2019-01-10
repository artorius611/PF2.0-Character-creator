import os 

strength = 10
dexterity = 10
constitution = 10
intelligence = 10
wisdom = 10
charisma = 10
health = 0
speed = 0
heritage_bonus = 0

class Halfling :
    def __init__ (self, strength, dexterity, constitution, intelligence, wisdom, charisma, health, speed, heritage_bonus) :
        self.dexterity = dexterity + 2
        self.wisdom = wisdom + 2
        self.strength = strength - 2
        self.constitution = constitution
        self.intelligence = intelligence
        self.charisma = charisma 
        self.health = health + 6
        self.speed = speed + 25
        frodo = "true"
        self.halfling_heritage = {
            'Gutsy' : 'Your family line is known for keeping a level head and staving off fear when the chips go down, making them wise leaders. If you succeed at a saving throw against an emotion effect, treat your result as a critical success instead of a success.',
            'Jungle' : 'You live deep in the jungle, and you’ve learned how to use your small size to wriggle through undergrowth, vines, and other obstacles. You can ignore difficult terrain from trees and foliage, whether in a jungle or elsewhere.',
            'Nomadic' : 'Your ancestors have traveled from place to place for generations. You gain a new language of your choice, and every time you take the Multilingual feat, you gain another new language.',
            'Twilight' : 'Your ancestors performed many acts under cover of dusk and developed eyesight beyond even the usual keen eyes of halflings. You gain low-light vision.'
        }
        print (self.halfling_heritage)
        heritage_input = "false"
        while heritage_input == "false":
            print ('\nWhat is your Heritage?\n')
            print ('1) Gutsy ')
            print ('2) Jungle')
            print ('3) Nomadic')
            print ('4) Twilight')
            choice = input('')
            print (choice)
            if choice == '1' :
                heritage_input = "true"
                self.heritage_bonus = self.halfling_heritage["Gutsy"]
            elif choice == '2' :
                heritage_input = "true"
                self.heritage_bonus = self.halfling_heritage['Jungle']
            elif choice == '3' :
                heritage_input = "true"
                self.heritage_bonus = self.halfling_heritage['Nomadic']
            elif choice == '4' :
                heritage_input = "true"
                self.heritage_bonus = self.halfling_heritage['Twilight']
        else:
            print ('\n \nYou selected something invalid\n \n')
        #clear the screen
        os.system ('cls')   

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
        user_race = Halfling (strength, dexterity, constitution, intelligence, wisdom, charisma, health, speed, heritage_bonus)
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
