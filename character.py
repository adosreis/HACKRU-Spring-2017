#from main import binary_answer_list
# call empty skills if starting new game
# else load current skills

binary_answer_list = ["Y", "y", "yes", "YES", "Yes", "No", "N", "NO", "no", "n"]

class character:
    name = ""
    skills = {"Strength": 0, "Perception": 0, "Endurance": 0, "Charisma": 0, "Intelligence": 0, "Agility": 0, "Luck": 0}

    def __init__(self, skills):
        self.name = skills.get("name")
        self.skills = skills[:1]


remaining_pts = 0


def charcheck(remaining_pts, attribute):
    global remaining_pts
    ipt = ("How many points would you like to allocate to %s", attribute)
    leftover_pts = remaining_pts - ipt
    while ipt > 10 or ipt < 0 or leftover_pts < 0:
        ipt = ("Please enter a valid number between 0 and 10. Make sure you have enough points to spend for this attribute.")
        leftover_pts = remaining_pts - ipt
    remaining_pts = leftover_pts
    print("You have %f points remaining", remaining_pts)
    return ipt


def create_character():
    global remaining_pts
    remaining_pts = 28
    happy = 0
    while(happy == 0):
        name = input("Hello what is your name?")

        print("Strength determines your power and carry capacity.")
        s = charcheck(remaining_pts, "Strength")

        print("Perception allows you to notice things, open up new dialogue options on occasion, and how far away you start in random encounters.")
        p = charcheck(remaining_pts, "Perception")

        print("Endurance determines your hitpoints and resistance to negative effects.")
        e = charcheck(remaining_pts, "Endurance")

        print("Description of Charisma")
        c = charcheck(remaining_pts, "Charisma")

        print("Description of Intelligence")
        i = charcheck(remaining_pts, "Intelligence")

        print("Description of Agility")
        a = charcheck(remaining_pts, "Agility")

        print("Description of Luck")
        l = charcheck(remaining_pts, "Luck")

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

