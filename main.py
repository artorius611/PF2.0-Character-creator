import os 
from Pieces import Ancestry
from Pieces import Bonus_stat
from Pieces import Background

strength = 0
dexterity = 0
constitution = 0
intelligence = 0
wisdom = 0
charisma = 0
health = 0
speed = 0
heritage_bonus = 0
dwarf = 0                    
gimli = 0
choice = 0
bonus_user_input = 0

print ('\nWhat is your Ancestry?\n')
print ('1) Dwarf')
print ('2) Elf')
print ('3) Gnome')
print ('4) Goblin')
print ('5) Halfling')
print ('6) Human')
choice = input('Which Ancestry do you choose? ')     
valid_user_input = "false"
while valid_user_input == "false" :
    if choice == '1' :
        valid_user_input = "true"
        user_race = Ancestry.Dwarf (strength, dexterity, constitution, intelligence, wisdom, charisma, health, speed, dwarf)
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
                user_race.strength = user_race.strength + bonus
            elif choice == 2 :
                bonus_user_input = 1
                user_race.dexterity = user_race.dexterity + bonus
            elif choice == 3 :
                bonus_user_input = 1
                user_race.intelligence = user_race.intelligence + bonus
            elif choice == 4 :
                bonus_user_input = 1
                user_race.charisma = user_race.charisma + bonus
            else:
                print ('\nYou selected something invalid\n')
            # the string below clears the screen
            os.system ('cls')
    elif choice == '2' :
        valid_user_input = "true"
        user_race = Ancestry.Elf (strength, dexterity, constitution, intelligence, wisdom, charisma, health, speed, heritage_bonus)
        while bonus_user_input == 0:
            print ('\nWhat is your bonus stat?\n')
            print ('1) Str')
            print ('2) Con')
            print ('3) Wis')
            print ('4) Cha')
            choice = int(input(''))
            bonus = 2
            if choice == 1 :
                bonus_user_input = 1
                user_race.strength = user_race.strength + bonus
            elif choice == 2 :
                bonus_user_input = 1
                user_race.constitution = user_race.constitution + bonus
            elif choice == 3 :
                bonus_user_input = 1
                user_race.wisdom = user_race.wisdom + bonus
            elif choice == 4 :
                bonus_user_input = 1
                user_race.charisma = user_race.charisma + bonus
            else:
                print ('\nYou selected something invalid\n')
            # the string below clears the screen
            os.system ('cls')
    elif choice == '3' :
        valid_user_input = "true"
        user_race = Ancestry.Gnome (strength, dexterity, constitution, intelligence, wisdom, charisma, health, speed, heritage_bonus)
        while bonus_user_input == 0:
            print ('\nWhat is your bonus stat?\n')
            print ('1) Str')
            print ('2) Dex')
            print ('3) Wis')
            print ('4) Int')
            choice = int(input(''))
            bonus = 2
            if choice == 1 :
                bonus_user_input = 1
                user_race.strength = user_race.strength + bonus
            elif choice == 2 :
                bonus_user_input = 1
                user_race.dexterity = user_race.dexterity + bonus
            elif choice == 3 :
                bonus_user_input = 1
                user_race.wisdom = user_race.wisdom + bonus
            elif choice == 4 :
                bonus_user_input = 1
                user_race.intelligence = user_race.intelligence + bonus
            else:
                print ('\nYou selected something invalid\n')
            # the string below clears the screen
            os.system ('cls')
    elif choice == '4' :
        valid_user_input = "true"
        user_race = Ancestry.Goblin (strength, dexterity, constitution, intelligence, wisdom, charisma, health, speed, heritage_bonus)
        while bonus_user_input == 0 :
            print ('\nWhat is your bonus stat?\n')
            print ('1) Str')
            print ('2) Con')
            print ('3) Wis')
            print ('4) Int')
            choice = int(input(''))
            bonus = 2
            if choice == 1 :
                bonus_user_input = 1
                user_race.strength = user_race.strength + bonus
            elif choice == 2 :
                bonus_user_input = 1
                user_race.constitution = user_race.constitution + bonus
            elif choice == 3 :
                bonus_user_input = 1
                user_race.wisdom = user_race.wisdom + bonus
            elif choice == 4 :
                bonus_user_input = 1
                user_race.intelligence = user_race.intelligence + bonus
            else:
                print ('\nYou selected something invalid\n')
            # the string below clears the screen
            os.system ('cls')
    elif choice == '5' :
        valid_user_input = "true"
        user_race = Ancestry.Halfling (strength, dexterity, constitution, intelligence, wisdom, charisma, health, speed, heritage_bonus)
        while bonus_user_input == 0 :
            print ('\nWhat is your bonus stat?\n')
            print ('1) Str')
            print ('2) Con')
            print ('3) Int')
            print ('4) Cha')
            choice = int(input(''))
            print (choice)
            bonus = 2
            if choice == 1 :
                bonus_user_input = 1
                user_race.strength = user_race.strength + bonus
            elif choice == 2 :
                bonus_user_input = 1
                user_race.constitution = user_race.constitution + bonus
            elif choice == 3 :
                bonus_user_input = 1
                user_race.intelligence = user_race.intelligence + bonus
            elif choice == 4 :
                bonus_user_input = 1
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
# print current stats after Ancestry
print ('Your Health is:', user_race.health, '\nYour Speed is: ', user_race.speed, 'ft.') 
print ('STR:', user_race.strength, '\n Dex', user_race.dexterity, '\n Con', user_race.constitution, '\n Int', user_race.intelligence, '\n Wis', user_race.wisdom, '\n Cha', user_race.charisma, '\nYour heritage:\n',  Ancestry.Character_feats['ancestry feats'][1])

print ('\nWhat is your Background?\n')
print ('1) Acolyte')
print ('2) Acrobat')
print ('3) Animal Whisperer')
print ('4) Barkeep')
print ('5) Blacksmith')
print ('6) Criminal')
choice = input('Choose your history: ')   
valid_user_input = "false"
while valid_user_input == "false" :
    if choice == '1' :
        valid_user_input = "true"
        user_back = Background.Acolyte (strength, dexterity, constitution, intelligence, wisdom, charisma, health, speed)
    else:
        print('\n \n You selected something invalid\n \n')
user_current = user_race.strength + user_back.strength, user_race.dexterity + user_back.dexterity, user_race.constitution + user_back.constitution, user_race.intelligence + user_back.intelligence, user_race.wisdom + user_back.wisdom, user_race.charisma + user_back.charisma
print ('Your Health is:', user_race.health, '\nYour Speed is: ', user_race.speed, 'ft.') 
print ('STR:', user_back.strength, '\n Dex', user_back.dexterity, '\n Con', user_back.constitution, '\n Int', user_back.intelligence, '\n Wis', user_back.wisdom, '\n Cha', user_back.charisma, '\nYour background:\n', Ancestry.Character_Feats['skill feats']['Background'])
