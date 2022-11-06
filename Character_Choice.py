
def Character_Choice():
     print("CHOOSE YOUR CHARACTER!")
     print("Mage:\n Weapon: Fireball Spell\n Armor: Hooded Robes\n Ability: Petrify")
     print("Mages are very smart, have very powerful spells and can petrify enemies for a short period of time.")
     print("Fighter:\n Weapon: Sword and shield\n Armor: Steel Studded Leather Armor\n Ability: Slash Flurry")
     print(
          "Fighters are dexterous and have a sword for attacking and a shield for defense. Fighters can use slash flurry\n"
          "to unleash a flurry of attacks on their enemies doing high damage.")
     print("Warlord:\n Weapon: Warhammer\n Armor: Full Steel Armor\n Ability: Rage")
     print(
          "Warlords are very powerful and wield a heavy warhammer that does very high damage but is slow to swing. They can\n"
          "use their built up anger at the world to unleash rage, rage allows the warlord to swing one giant blow that\n"
          "will put most enemies down immediately.")
     print("Thief:\n Weapon: Double Daggers\n Armor: Cloth Armor\n Ability: Sneak")
     print(
          "Thieves are very sly and quick on their feet. They have two razor sharp daggers made out of obsidian and can\n"
          "cut through any flesh with ease. They are able to use their slyness to sneak past enemies without being seen or\n"
          "heard.")
     User_Character = input("Selection: ")
     while User_Character.upper() not in ["MAGE", "FIGHTER", "WARLORD", "THIEF"]:
          print("That's not an option!")
          User_Character = input("Selection: ")

     Confirm_Character = 1

     while Confirm_Character == 1:
          Confirm_Character = input(f"You are a {User_Character.title()}. Is this right? Y/N: ")
          if Confirm_Character.upper() == "Y":
               break
          elif Confirm_Character.upper() == "N":
               Character_Choice()
          else:
               Confirm_Character = 1
     return User_Character


def User_Name_Choice():
     print(f"Now what is your name?")
     User_Name = input("Name: ")
     Confirm_Character = 1
     while Confirm_Character == 1:
          Confirm_Character = input(f"Your name is {User_Name.title()}. Is this right? Y/N: ")
          if Confirm_Character.upper() == "Y":
               break
          elif Confirm_Character.upper() == "N":
               Re_Choose = input("Press N to change your name or C to change your character: ")
               if Re_Choose.upper() == "N":
                    User_Name_Choice()
               elif Re_Choose.upper() == "C":
                    Character_Choice()
               else:
                    print("That wasn't an option.")
          else:
               Confirm_Character = 1
     return User_Name


