import os 
from Pieces import Ancestry
from Pieces import Bonus_stat
from Pieces import Race

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

a = Ancestry()
a.user_race((strength, dexterity, constitution, intelligence, wisdom, charisma, health, speed, heritage_bonus, choice, dwarf, gimli))
print ('Your Health is:', a.health, '\nYour Speed is: ', a.speed, 'ft.') 
print ('STR:', a.strength, '\n Dex', a.dexterity, '\n Con', a.constitution, '\n Int', a.intelligence, '\n Wis', a.wisdom, '\n Cha', a.charisma, '\nYour heritage:\n',  a.heritage_bonus)
print (Ancestry.Character_feats['ancestry feats'][1])
b = Bonus_stat.Bonus_Stat (strength, dexterity, constitution, intelligence, wisdom, charisma, health, speed, heritage_bonus, choice, dwarf, gimli)
print ('Your Health is:', b.health, '\nYour Speed is: ', b.speed, 'ft.') 
print ('STR:', b.strength, '\n Dex', b.dexterity, '\n Con', b.constitution, '\n Int', b.intelligence, '\n Wis', b.wisdom, '\n Cha', b.charisma, '\nYour heritage:\n',  b.heritage_bonus)
