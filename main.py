import Character_Choice as CC
import Game_Over as G_O




if __name__ == "__main__":
    User_Character = CC.Character_Choice().title()
    User_Name = CC.User_Name_Choice().title()
    print(
        f"(Charzeen) Hello {User_Name} and welcome to the world of Rimsky. Currently you are stuck in the pits of Picarus. These\n"
        f"pits are used to imprison the nastiest that Rimsky has to offer and I am Charzeen, the warden of these pits.\n"
        f"We recently had a large scale break out due to the dark lord Razim attacking us to free his minions. However\n"
        f"you seem to have been left behind. Do you serve Razim?")
    c1 = input("(You) Yes, I serve the almighty Lord Razim.(1)\n"
               "(You) No, I don't know where I am.(2)\n")
    if c1 == "1":
        print("\x1B[3m" + "Charzeen quickly raises his executioners axe and slices your head off." + "\x1b[0m")



