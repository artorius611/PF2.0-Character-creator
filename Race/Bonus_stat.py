import decision

class Bonus_Stat :
    def __init__ (self, strength, dexterity, constitution, intelligence, wisdom, charisma) :
        self.dexterity = dexterity + 2
        self.wisdom = wisdom + 2
        self.strength = strength + 2
        self.constitution = constitution + 2
        self.intelligence = intelligence + 2
        self.charisma = charisma + 2
        self.bonus_user_input = 0
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
                        user_race.strength = user_race.strength + bonus
            elif choice == 2 :  
                if self.bonus_user_input == 1 :
                    print ('you cant select the same bonus')
                else :
                    self.bonus_user_input = self.bonus_user_input + 1
                    user_race.dexterity = user_race.dexterity + bonus
            elif choice == 3 :
                if self.bonus_user_input == 1 :
                    print ('you cant select the same bonus')
                else :
                    self.bonus_user_input = self.bonus_user_input + 1
                    user_race.constitution = user_race.constitution + bonus
            elif choice == 4 :
                if self.bonus_user_input == 1 :
                    print ('you cant select the same bonus')
                else :
                    self.bonus_user_input = self.bonus_user_input + 1
                    user_race.intelligence = user_race.intelligence + bonus
            elif choice == 5 :
                if self.bonus_user_input == 1 :
                    print ('you cant select the same bonus')
                else :
                    self.bonus_user_input = self.bonus_user_input + 1
                    user_race.wisdom = user_race.wisdom + bonus
            elif choice == 6 :
                if self.bonus_user_input == 1 :
                    print ('you cant select the same bonus')
                else :
                    self.bonus_user_input = self.bonus_user_input + 1
                    user_race.charisma = user_race.charisma + bonus
            else:
                print ('\nYou selected something invalid\n')
            # the string below clears the screen
            os.system ('cls')
