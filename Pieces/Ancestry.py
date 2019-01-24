import os
from Pieces import Ancestry
from Pieces import Bonus_stat

class Acolyte :
    def __init__ (self, strength, dexterity, constitution, intelligence, wisdom, charisma, health, speed) :
        self.dexterity = dexterity 
        self.wisdom = wisdom 
        self.strength = strength 
        self.constitution = constitution 
        self.intelligence = intelligence 
        self.charisma = charisma
        self.health = health
        self.speed = speed
        self.bonus_user_input = 0
        print ('You spent your early days in a religious monastery or cloister. You may have traveled out into the world to spread the message of your religion or because you cast away the teachings of your faith, but deep inside you’ll always carry the lessons you learned.')
        choice = input('Is this the background you want?')
        print ('1) Yes')
        print ('2) No')
        if choice == 1 :
            Ancestry.Character_Feats['skill feats']['Background'] = Bonus_stat.general_feats['skill feats']['Student of the Canon'] 
            print('Choose two ability boosts. One must be to Constitution or Wisdom, and one is a free ability boost.')
            while bonus_user_input == 0:
                print ('\nDo you Choose Wisdom or Constitution?\n')
                print ('1) Constitution')
                print ('2) Wisdom')
                choice = int(input(''))
                print (choice)
                bonus = 2
                if choice == 1 :
                    bonus_user_input = 1
                    user_race.constitution = user_race.constitution + bonus
                elif choice == 2 :
                    bonus_user_input = 1
                    user_race.wisdom = user_race.wisdom + bonus
                else:
                    print ('\nYou selected something invalid\n')
                # the string below clears the screen
                os.system ('cls')
                while bonus_user_input == 1:
                    print ('\nWhat is your bonus stat?\n')
                    print ('1) Str')
                    print ('2) Dex')
                    print ('3) Int')
                    print ('4) Cha')
                    choice = int(input(''))
                    print (choice)
                    bonus = 2
                    if choice == 1 :
                        bonus_user_input = 2
                        user_race.strength = user_race.strength + bonus
                    elif choice == 2 :
                        bonus_user_input = 2
                        user_race.dexterity = user_race.dexterity + bonus
                    elif choice == 3 :
                        bonus_user_input = 2
                        user_race.intelligence = user_race.intelligence + bonus
                    elif choice == 4 :
                        bonus_user_input = 2
                        user_race.charisma = user_race.charisma + bonus
                    else:
                        print ('\nYou selected something invalid\n')
                    # the string below clears the screen
                    os.system ('cls')
        else :
            print ('Choose a different background')
            os.system ('cls')
