import os

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
