import os 



str_ch = 10
dex_ch = 10
con_ch = 10
int_ch = 10
wis_ch = 10
cha_ch = 10
speed = 0
health = 0

class Halfling :
    def __init__ (self, frodo, str_ch, dex_ch, con_ch, int_ch, wis_ch, cha_ch, speed, health) :
        frodo = "true"
        self.dex_ch = dex_ch + 2
        self.wis_ch = wis_ch + 2
        self.str_ch = str_ch - 2
        self.con_ch = con_ch
        self.int_ch = int_ch
        self.cha_ch = cha_ch 
        self.speed = speed + 25
        self.ch_hp = health + 6

valid_user_input = "false"
while valid_user_input == "false" :
    print ('''
    What is your Ancestry?
    
    ''')
    print ('1) Halfling')
    print ()
    choice = input('Which Ancestry do you choose? ')
    if choice == '1' :
        valid_user_input = "true"
        user_race = Halfling(str_ch, dex_ch, con_ch, int_ch, wis_ch, cha_ch, speed, ch_hp)
        #bonus_user_input == "false"
        #while bonus_user_input == "false":
        #    print ('''  
    #
    #        What is your bonus stat?
    #
     #       ''')
      #      print ('1) Str')
       #     print ('2) Con')
        #    print ('3) Int')
         #   print ('4) Cha')
         #   choice = input('Which bonus stat do you choose?')
         #   if choice == 1 :
         #      bonus_user_input = "true"
         #        = user_race.str_ch + 2
         #   elif choice == 2 :
         #       bonus_user_input = "true"
         #       con_ch = user_race.con_ch + 2
         #   elif choice == 3 :
         #       bonus_user_input = "true"
         #       int_ch = user_race.int_ch + 2
         #   elif choice == 4 :
         #       bonus_user_input = "true"
         #       cha_ch = user_race.cha_ch + 2
         #   else:
         #       print ('''
         #   
         #       You selected something invalid
         #   
         #       ''')
            # the string below clears the screen
         #   os.system ('cls')        
    else:
        print ('''
        
        
        You selected something invalid
        
        
        ''')
        # the string below clears the screen
    os.system ('cls')
print ('''
Your health is: ''', user_race.ch_hp, ''' \n Your Speed is:''', user_race.speed, '''
Your Stats are:\n STR:''', user_race.str_ch, '\n Dex', user_race.dex_ch, '\n Con', user_race.con_ch, '\n Int', user_race.int_ch, '\n Wis', user_race.wis_ch, '\n Cha', user_race.cha_ch)
