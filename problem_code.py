      while bonus_user_input == "true":
            print ('\nWhat is your bonus stat?\n')
            print ('1) Str')
            print ('2) Con')
            print ('3) Int')
            print ('4) Cha')
            choice = input('')
            print (choice)
            bonus = 2
            if choice == 1 :
                bonus_user_input = "false"
                bonus_user = user_race.strength + bonus
            elif choice == 2 :
                bonus_user_input = "false"
                bonus_user = user_race.constitution + bonus
            elif choice == 3 :
                bonus_user_input = "false"
                bonus_user = user_race.intelligence + bonus
            elif choice == 4 :
                bonus_user_input = "false"
                bonus_user = user_race.charisma + bonus
            else:
                print ('\nYou selected something invalid\n')
            # the string below clears the screen
            os.system ('cls')
