import os

Character_feats = {'ancestry feats' : { 1 : "false", 5 : "false", 9 : "false", 13 : "false", 17 : "false"} ,
                    'skill feats' : {'Background' : "false", 2 : "false", 4 : "false", 6 : "false", 8 : "false", 10 : "false", 12 : "false", 14 : "false", 16 : "false", 18 : "false", 20 : "false"}, 
                    'general feats' : { 3 : "false", 7 : "false", 11 : "false", 15 : "false", 19 : "false"}
                    }
class Dwarf :
    def __init__ (self, strength, dexterity, constitution, intelligence, wisdom, charisma, health, speed, heritage_bonus, dwarf, gimli) :
        self.strength = strength + 10
        self.dexterity = dexterity + 10
        self.constitution = constitution + 12
        self.intelligence = intelligence + 10
        self.wisdom = wisdom + 12
        self.charisma = charisma + 8
        self.health = health + 10
        self.speed = speed + 20
        self.gimli = "true"
        self.dwarf = {
            'heritage' : {'Ancient-Blooded' : 'Dwarven heroes of old could shrug off their enemies’ magic, and some of that resistance manifests in you. You gain the Call on Ancient Blood reaction, but your resistance hampers your connection to magic items. Reduce your total Resonance Points by 2 (minimum 0)',
            'Desert Dwarf' : 'As a proud denizen of the desert, you have incredible resilience against hot environments. This grants you resistance to fire equal to half your level (minimum 1) and the ability to ignore extreme and severe heat up to 140° F.',
            'Stronghearted Dwarf' : 'Your blood runs hearty and strong, and you can shake off toxins that would lay others low. You gain poison resistance equal to half your level (minimum 1), and each of your successful saving throws against an ongoing poison reduces its stage by 2, or 1 for a virulent poison. Each critical success against an ongoing poison reduces its stage by 3, or 2 for a virulent poison.',
            'Unburdened Dwarf ' : 'Your ancestors fought in ancient wars, generations after generations adapting to wearing massive suits of armor. If your Speed would be reduced by armor you wear or the encumbered condition, you ignore 5 feet of that reduction.'},
            'feats' : {'Ancestral Hatred' : 'You have shaped your hatred of ancestral dwarven foes into a powerful weapon. Choose two of the following creature traits: derro, duergar, giant, or orc. You gain a +1 circumstance bonus to damage rolls against creatures with one of the chosen traits. If a creature with a chosen trait critically succeeds at an attack against you, this bonus increases to +4 against that creature for 1 minute. Special Your GM can add appropriate creature traits to this list if your character is from a community that commonly fights other types of enemies.', 
            '''Ancient's Blood''' : 'Trigger You attempt a saving throw against a magical effect. Your ancestors’ innate resistance to magic has manifested in you. You gain a +2 circumstance bonus to the triggering saving throw. Special Your resistance hampers your connection to magic items. Reduce your total Resonance Points by 2 (minimum 0). For more information about Resonance Points, see page 376.',
            'Boulder Roll' : 'Your dwarven build allows you to push foes around. Take a Step into the square of a foe that is your size or smaller, and the foe must move into the empty space directly behind it. The foe must move even if doing so places it in harm’s way. The foe can attempt to block your Step by rolling a Fortitude saving throw against your Athletics DC. If the foe attempts this saving throw, regardless of the saving throw’s result, the creature takes bludgeoning damage equal to your level plus your Strength modifier. If the foe can’t move into an empty space (if it is surrounded by solid objects or other creatures, for example), your Boulder Roll has no effect. Prerequisites Mountain Roots',
            'Giant Bane' : 'Your squat stature and your hatred for giantkind give you an edge when fighting them. You gain a +1 circumstance bonus to your Armor Class against giants; Fortitude and Reflex DCs against giants’ attempts to Disarm, Grapple, Shove, or Trip you; Survival checks to track giants; Perception checks to notice giants; and Stealth checks to avoid being noticed by giants.',
            'Hardy' : 'Your blood runs hearty and strong, and you can shake off toxins that would lay others low. You gain poison resistance equal to half your level (minimum 1), and each of your successful saving throws against an ongoing poison reduces its stage by 2, or 1 for a virulent poison. Each critical success against an ongoing poison reduces its stage by 3, or 2 for a virulent poison.',
            'Mountain Root' : 'You can plant your feet on the ground to become nearly immovable. You gain a +2 circumstance bonus to your Fortitude or Reflex DC whenever anyone attempts to Shove or Trip you. This bonus also applies to saves against spells or effects that attempt to knock you prone. In addition, if any ability or effect would force you to move 10 feet or more in any direction, you are moved only half the distance.',
            'Rock Runner' : 'Your innate connection to stone makes you adept at moving across uneven surfaces. When you take the Step action, you can ignore difficult terrain caused by uneven ground made of stone and earth. In addition, when you use the Acrobatics skill to Balance on narrow surfaces or uneven ground made of stone or earth, you aren’t flat-footed, and you treat a success on the Acrobatics check as if it were a critical success.',
            'Stonecunning' : 'You have a knack for noticing inconsistencies and craftsmanship techniques in the stonework around you. You gain a +2 circumstance bonus to Perception checks to notice unusual stonework. This bonus applies to checks to discover mechanical traps made of stone or hidden inside of stone. If you aren’t using the Seek action or searching, the GM rolls a secret check without the bonus and with a –2 circumstance penalty for you to notice unusual stonework anyway (in such cases, this feat takes on the secret trait).',
            'Weapon Cunning (Dwarf)' : 'Whenever you critically hit using a weapon of the axe, hammer, or pick group, you apply the weapon’s critical specialization effect. Prerequisites Weapon Familiarity (Dwarf).',
            'Weapon Familiarity(Dwarf)' : 'Your kin have instilled in you an affinity for hardhitting weapons, and you prefer them to more elegant arms. You are trained with the battleaxe, pick, and warhammer. In addition, you gain access to all uncommon dwarf weapons. For the purpose of proficiencies, you treat martial dwarf weapons as simple weapons and exotic dwarf weapons as martial weapons.'}
        }
        print (self.dwarf[ 'heritage' ])
        heritage_input = "false"
        while heritage_input == "false":
            print ('\nWhat is your Heritage?\n')
            print ('1) Ancient-Blooded ')
            print ('2) Desert Dwarf')
            print ('3) Stronghearted Dwarf')
            print ('4) Unburdened Dwarf')
            choice = input('')
            print (choice)
            if choice == '1' :
                heritage_input = "true"
                self.dwarf = self.dwarf['heritage']["Ancient-Blooded"]
            elif choice == '2' :
                heritage_input = "true"
                self.dwarf = self.dwarf['heritage']['Desert Dwarf']
            elif choice == '3' :
                heritage_input = "true"
                self.heritage_bonus = self.dwarf['heritage']['Stronghearted Dwarf']
            elif choice == '4' :
                heritage_input = "true"
                self.dwarf = self.dwarf['heritage']['Unburdened Dwarf']
        else:
            print ('\n \nYou selected something invalid\n \n')
        #clear the screen
        os.system ('cls') 
        print (self.dwarf['feats'])
        feat_choice = "false"
        while feat_choice == "false" :
            print ('What feat do you choose?')
            print ('1) Ancestral Hatred')
            print ('''2) Ancient's Blood''')
            print ('3) Giant Bane')
            print ('4) Hardy')
            print ('5) Mountain Root')
            print ('6) Rock Runner')
            print ('7) Stonecunning')
            print ('8) Weapon Familiarity(Dwarf)')
            feat_choice = input('')
            if feat_choice == 1 :
                Character_Feats['ancestry_feats'][1] = self.dwarf['feats']['Ancestral Hatred'] 
                feat_choice = "true"
            elif feat_choice == 2 :
                Character_Feats['ancestry_feats'][1] = dwarf_feats['feats']['''Ancient's Blood'''] 
                feat_choice = "true"
            elif feat_choice == 3 :
                Character_Feats['ancestry_feats'][1] = dwarf_feats['feats']['Giant Bane'] 
                feat_choice = "true"
            elif feat_choice == 4 :
                Character_Feats['ancestry_feats'][1] = dwarf_feats['feats']['Hardy'] 
                feat_choice = "true"
            elif feat_choice == 5 :
                Character_Feats['ancestry_feats'][1] = dwarf_feats['feats']['Mountain Root'] 
                feat_choice = "true" 
            elif feat_choice == 6 :
                Character_Feats['ancestry_feats'][1] = dwarf_feats['feats']['Rock Runner'] 
                feat_choice = "true"
            elif feat_choice == 7 :
                Character_Feats['ancestry_feats'][1] = dwarf_feats['feats']['Stonecunning'] 
                feat_choice = "true"
            elif feat_choice == 8 :
                Character_Feats['ancestry_feats'][1] = dwarf_feats['feats']['Weapon Familiarity(Dwarf)'] 
                feat_choice = "true" 
        else:
            print ('\n \nYou selected something invalid\n \n')
            #clear the screen
        os.system ('cls')                                                                             
class Elf :
    def __init__ (self, strength, dexterity, constitution, intelligence, wisdom, charisma, health, speed, heritage_bonus) :
        self.strength = strength 
        self.dexterity = dexterity +2
        self.constitution = constitution - 2
        self.intelligence = intelligence + 2
        self.wisdom = wisdom 
        self.charisma = charisma 
        self.health = health + 6
        self.speed = speed + 30
        legolas = "true"
        self.elf_heritage = {
            'Arctic Elf' : 'You dwell deep in the frozen lands of the arctic north and have gained incredible resilience against cold environments. This adaptation grants you resistance to cold equal to half your level (minimum 1) and the ability to ignore extreme and severe cold down to –80° F.',
            'Cavern Elf' : 'You come from underground tunnels or from caverns where light is scarce. You gain darkvision.',
            'Keen-eared Elf' : 'Your ears are finely tuned, able to detect even the slightest whispers of sound. As long as you can hear normally, you can use the Seek action to sense unseen creatures in a 60-foot cone instead of a 30-foot cone. When using the Seek action to sense unseen creatures that you could hear within 30 feet, you gain a +2 circumstance bonus. ',
            'Jungle Elf' : 'You’re adapted to life in the deep jungle, and you know how to climb through a jungle more easily and use the foliage to your advantage. When climbing trees, vines, and other foliage, you move at half your Speed on a success and at full Speed on a critical success (and you move at full Speed on a success if you have Quick Climb). This doesn’t affect you if you’re using a climb Speed. You can always use the Take Cover action when within a forest or jungle area to gain cover, even if you’re not next to an obstacle you can take cover behind.'
        }
        print (self.elf_heritage)
        heritage_input = "false"
        while heritage_input == "false":
            print ('\nWhat is your Heritage?\n')
            print ('1) Arctic Elf ')
            print ('2) Cavern Elf')
            print ('3) Keen-eared Elf')
            print ('4) Jungle Elf')
            choice = input('')
            print (choice)
            if choice == '1' :
                heritage_input = "true"
                self.heritage_bonus = self.elf_heritage["Arctic Elf"]
            elif choice == '2' :
                heritage_input = "true"
                self.heritage_bonus = self.elf_heritage['Cavern Elf']
            elif choice == '3' :
                heritage_input = "true"
                self.heritage_bonus = self.elf_heritage['Keen-eared Elf']
            elif choice == '4' :
                heritage_input = "true"
                self.heritage_bonus = self.elf_heritage['Jungle Elf']
        else:
            print ('\n \nYou selected something invalid\n \n')
        #clear the screen
        os.system ('cls')

class Gnome :
    def __init__ (self, strength, dexterity, constitution, intelligence, wisdom, charisma, health, speed, heritage_bonus) :
        self.strength = strength - 2
        self.dexterity = dexterity 
        self.constitution = constitution + 2
        self.intelligence = intelligence
        self.wisdom = wisdom 
        self.charisma = charisma + 2
        self.health = health + 8
        self.speed = speed + 20
        weebee = "true"
        self.gnome_heritage = {
            'Bleachling' : 'Something in your background caused you to react strangely to the Bleaching compared to other gnomes. Instead of dying, you lost your color but remained stable. You are immune to the Bleaching and gain the Animal Speaker feat. It’s possible for your heritage to change from your starting heritage to bleachling during the course of play due to the effects of the Bleaching, though typically only in campaigns that span an incredibly long amount of time.',
            'Deep Gnome' : 'Also called a svirfneblin, you come from underground and have found a way to stave off the gnome malaise known as the Bleaching. You gain darkvision and are immune to the Bleaching.',
            'Fell Gnome' : 'Unlike most gnomes, you have a connection to some of the darker fey, such as gremlins and redcaps. You can cast chill touch as an innate primal spell at will. The cantrip is heightened to a spell level equal to half your level rounded up.',
            'Sharp-nosed Gnome' : 'You see all colors as brighter, hear all sounds as richer, and especially smell all scents with incredible detail. You gain a +2 circumstance bonus to sense an unseen creature that is close enough for you to smell (typically within 30 feet, though halve the distance if you are upwind and double the distance if you are downwind).'
        }
        print (self.gnome_heritage)
        heritage_input = "false"
        while heritage_input == "false":
            print ('\nWhat is your Heritage?\n')
            print ('1) Bleachling ')
            print ('2) Deep Gnome')
            print ('3) Fell Gnome')
            print ('4) Sharp-nosed Gnome')
            choice = input('')
            print (choice)
            if choice == '1' :
                heritage_input = "true"
                self.heritage_bonus = self.gnome_heritage["Bleachling"]
            elif choice == '2' :
                heritage_input = "true"
                self.heritage_bonus = self.gnome_heritage['Deep Gnome']
            elif choice == '3' :
                heritage_input = "true"
                self.heritage_bonus = self.gnome_heritage['Fell Gnome']
            elif choice == '4' :
                heritage_input = "true"
                self.heritage_bonus = self.gnome_heritage['Sharp-nosed Gnome']
        else:
            print ('\n \nYou selected something invalid\n \n')
        #clear the screen
        os.system ('cls')

class Goblin :
    def __init__ (self, strength, dexterity, constitution, intelligence, wisdom, charisma, health, speed, heritage_bonus) :
        self.strength = strength 
        self.dexterity = dexterity + 2
        self.constitution = constitution 
        self.intelligence = intelligence 
        self.wisdom = wisdom - 2
        self.charisma = charisma + 2 
        self.health = health + 6
        self.speed = speed + 25
        norman = "true"
        self.goblin_heritage = {
            'Bigbelly Goblin' : 'You can subsist on food that most folks would consider spoiled. You are always considered fed with poor meals in a settlement as long as garbage is readily available, without using the Subsist on the Streets downtime activity. You gain a +2 circumstance bonus to saving throws against toxins, against gaining the sick condition, and on removing the sick condition, but only if the toxin or condition resulted from something you ate or drank. Treat a success on Fortitude saves to reduce the effect of an ingested toxin or the sick condition as a critical success. You can eat and drink things when you have the sick condition.',
            'Inflammable Goblin' : 'Your ancestors have always had a connection to fire and a thicker skin, allowing you to resist burning. You gain resistance to fire equal to half your level (minimum 1). Your flat check to remove persistent fire damage (see page 323) is DC 15 instead of DC 20 without requiring an action to reduce the DC.',
            'Razortooth Goblin' : 'Your family can use their teeth as formidable weapons. You gain a jaws unarmed attack that deals 1d6 piercing damage.',
            'Snow Goblin' : 'As a snow goblin, you live in deeply cold lands and have skin ranging from sky blue to navy in color. You gain resistance to cold equal to half your level (minimum 1) and the ability to ignore extreme and severe cold down to –80° F.'
        }
        print (self.goblin_heritage)
        heritage_input = "false"
        while heritage_input == "false":
            print ('\nWhat is your Heritage?\n')
            print ('1) Bigbelly Goblin ')
            print ('2) Inflammable Goblin')
            print ('3) Razortooth Goblin')
            print ('4) Snow Goblin')
            choice = input('')
            print (choice)
            if choice == '1' :
                heritage_input = "true"
                self.heritage_bonus = self.goblin_heritage["Bigbelly Goblin"]
            elif choice == '2' :
                heritage_input = "true"
                self.heritage_bonus = self.goblin_heritage['Inflammable Goblin']
            elif choice == '3' :
                heritage_input = "true"
                self.heritage_bonus = self.goblin_heritage['Razortooth Goblin']
            elif choice == '4' :
                heritage_input = "true"
                self.heritage_bonus = self.goblin_heritage['Snow Goblin']
        else:
            print ('\n \nYou selected something invalid\n \n')
        #clear the screen
        os.system ('cls')

class Halfling :
    def __init__ (self, strength, dexterity, constitution, intelligence, wisdom, charisma, health, speed, heritage_bonus) :
        self.strength = strength - 2
        self.dexterity = dexterity + 2
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom + 2
        self.charisma = charisma 
        self.health = health + 6
        self.speed = speed + 25
        frodo = "true"
        self.halfling_heritage = {
            'Gutsy Halfling' : 'Your family line is known for keeping a level head and staving off fear when the chips go down, making them wise leaders. If you succeed at a saving throw against an emotion effect, treat your result as a critical success instead of a success.',
            'Jungle Halfling' : 'You live deep in the jungle, and you’ve learned how to use your small size to wriggle through undergrowth, vines, and other obstacles. You can ignore difficult terrain from trees and foliage, whether in a jungle or elsewhere.',
            'Nomadic Halfling' : 'Your ancestors have traveled from place to place for generations. You gain a new language of your choice, and every time you take the Multilingual feat, you gain another new language.',
            'Twilight Halfling' : 'Your ancestors performed many acts under cover of dusk and developed eyesight beyond even the usual keen eyes of halflings. You gain low-light vision.'
        }
        print (self.halfling_heritage)
        heritage_input = "false"
        while heritage_input == "false":
            print ('\nWhat is your Heritage?\n')
            print ('1) Gutsy Halfling')
            print ('2) Jungle Halfling')
            print ('3) Nomadic Halfling')
            print ('4) Twilight Halfling')
            choice = input('')
            print (choice)
            if choice == '1' :
                heritage_input = "true"
                self.heritage_bonus = self.halfling_heritage['Gutsy Halfling']
            elif choice == '2' :
                heritage_input = "true"
                self.heritage_bonus = self.halfling_heritage['Jungle Halfling']
            elif choice == '3' :
                heritage_input = "true"
                self.heritage_bonus = self.halfling_heritage['Nomadic Halfling']
            elif choice == '4' :
                heritage_input = "true"
                self.heritage_bonus = self.halfling_heritage['Twilight Halfling']
        else:
            print ('\n \nYou selected something invalid\n \n')
        #clear the screen
        os.system ('cls')

class Human :
    def __init__ (self, strength, dexterity, constitution, intelligence, wisdom, charisma, health, speed, heritage_bonus) :
        self.strength = strength 
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom 
        self.charisma = charisma 
        self.health = health + 8
        self.speed = speed + 25
        boromir = "true"
        self.human_heritage = {
            'Half-elf' : 'Either one of your parents was an elf, or one or both were half-elves. You have pointed ears and other telltale signs of elf heritage. You gain the elf trait and low-light vision. In addition, you can select elf, half-elf, and human feats whenever you gain an ancestry feat.',
            'Half-orc' : 'Either one of your parents was an orc, or one or both were half-orcs. You have a green tinge to your skin and other indicators of orc heritage. You gain the orc trait and low-light vision. In addition, you can select orc, half-orc, and human feats whenever you gain an ancestry feat.',
            'Skilled Heritage' : 'Your ingenuity allows you to train in a wide variety of skills. You become trained in one skill of your choice. At 5th level, you become an expert in the chosen skill.',
            'Versatile Heritage' : 'Versatility and ambition have fueled humanity’s ascendance to its position as the most common ancestry in most nations throughout the world. Select a general feat of your choice for which you meet the prerequisites.'
        }
        print (self.human_heritage)
        heritage_input = "false"
        while heritage_input == "false":
            print ('\nWhat is your Heritage?\n')
            print ('1) Half-elf ')
            print ('2) Half-orc')
            print ('3) Skilled Heritage')
            print ('4) Versatile Heritage')
            choice = input('')
            print (choice)
            if choice == '1' :
                heritage_input = "true"
                boromir = "false"
                aragorn = "true"
                self.heritage_bonus = self.human_heritage["Half-elf"]
            elif choice == '2' :
                heritage_input = "true"
                boromir = "false"
                daelan = "true"
                self.heritage_bonus = self.human_heritage['Half-orc']
            elif choice == '3' :
                heritage_input = "true"
                self.heritage_bonus = self.human_heritage['Skilled Heritage']
            elif choice == '4' :
                heritage_input = "true"
                self.heritage_bonus = self.human_heritage['Versatile Heritage']
        else:
            print ('\n \nYou selected something invalid\n \n')
        #clear the screen
        os.system ('cls')
