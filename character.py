#from main import binary_answer_list
# call empty skills if starting new game
# else load current skills

binary_answer_list = ["Y", "y", "yes", "YES", "Yes", "No", "N", "NO", "no", "n"]
remaining_pts = 0

class character:
    name = ""
    skills = {"Strength": 0, "Perception": 0, "Endurance": 0, "Charisma": 0, "Intelligence": 0, "Agility": 0, "Luck": 0}

    def __init__(self, inskills):
        self.name = inskills.get("name")
        self.skills = {key:inskills[key] for key in ["Strength","Perception","Endurance","Charisma","Intelligence","Agility","Luck",]}
        print(self.skills)





def charcheck( attribute):
    global remaining_pts
    ipt = int(input("How many points would you like to allocate to this"))
    leftover_pts = remaining_pts - ipt
    while ipt > 10 or ipt < 0 or leftover_pts < 0:
        ipt = int(input("Please enter a valid number between 0 and 10. Make sure you have enough points to spend for this attribute."))
        leftover_pts = remaining_pts - ipt
    remaining_pts = leftover_pts
    print("You have {} points remaining".format(remaining_pts))
    return ipt


def create_character():
    global remaining_pts
    happy = 0
    while(happy == 0):
        remaining_pts = 28
        name = input("Hello what is your name?")

        print("Strength determines your power and carry capacity.")
        s = charcheck("Strength")

        print("Perception allows you to notice things, open up new dialogue options on occasion, and how far away you start in random encounters.")
        p = charcheck("Perception")

        print("Endurance determines your hitpoints and resistance to negative effects.")
        e = charcheck("Endurance")

        print("Description of Charisma")
        c = charcheck("Charisma")

        print("Description of Intelligence")
        i = charcheck("Intelligence")

        print("Description of Agility")
        a = charcheck( "Agility")

        print("Description of Luck")
        l = charcheck("Luck")

        # Print current values for review
        print("Strength:     %f",s)
        print("Perception:   %f",p)
        print("Endurance:    %f",e)
        print("Charisma:     %f",c)
        print("Intelligence: %f",i)
        print("Agility:      %f",a)
        print("Luck:         %f",l)

        con = None
        while(not (con in binary_answer_list)):
            con = input("Are you happy with your traits?")
        if con in binary_answer_list[:4]:
            happy = 1
        if con in binary_answer_list[:-4]:
            happy = 0

