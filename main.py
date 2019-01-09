import os 

strength = 10
dexterity = 10
constitution = 10
intelligence = 10
wisdom = 10
charisma = 10
health = 0
speed = 0

class Halfling :
    def __init__ (self, strength, dexterity, constitution, intelligence, wisdom, charisma, health, speed) :
        self.dexterity = dexterity + 2
        self.wisdom = wisdom + 2
        self.strength = strength - 2
        self.constitution = constitution
        self.intelligence = intelligence
        self.charisma = charisma 
        self.health = health + 6
        self.speed = speed + 25
        frodo = "true"

class Bonus_Stat :
    def __init__ (self, strength, dexterity, constitution, intelligence, wisdom, charisma, health, speed) :
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
        user_race = Halfling (strength, dexterity, constitution, intelligence, wisdom, charisma, health, speed)
        bonus_user_input = "false"
        while bonus_user_input == "false":
            print ('\nWhat is your bonus stat?\n')
            print ('1) Str')
            print ('2) Con')
            print ('3) Int')
            print ('4) Cha')
            choice = input('Which bonus stat do you choose?')
            if choice == 1 :
               bonus_user_input = "true"
               bonus_user = Halfling(strength) + Bonus_stat(strength)
               print ('Your Health is:', user_race.health, '\nYour Speed is: ', user_race.speed, 'ft. \nYour Stats are:\n STR:', bonus_user.strength, '\n Dex', user_race.dexterity, '\n Con', user_race.constitution, '\n Int', user_race.intelligence, '\n Wis', user_race.wisdom, '\n Cha', user_race.charisma)
            elif choice == 2 :
                bonus_user_input = "true"
                bonus_user = Halfling(constitution) + Bonus_stat(con)
            elif choice == 3 :
                bonus_user_input = "true"
                intelligence = user_race.intelligence + 2
            elif choice == 4 :
                bonus_user_input = "true"
                charisma = user_race.charisma + 2
            else:
                print ('\nYou selected something invalid\n')
            # the string below clears the screen
            os.system ('cls')        
    else:
        print ('''
        
        
        You selected something invalid
        
        
        ''')
        # the string below clears the screen
    os.system ('cls')
print ('Your Health is:', user_race.health, '\nYour Speed is: ', user_race.speed, 'ft. \nYour Stats are:\n STR:', user_race.strength, '\n Dex', user_race.dexterity, '\n Con', user_race.constitution, '\n Int', user_race.intelligence, '\n Wis', user_race.wisdom, '\n Cha', user_race.charisma)
