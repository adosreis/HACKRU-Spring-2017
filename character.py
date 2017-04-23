#from main import binary_answer_list
# call empty skills if starting new game
# else load current skills
from utils import clear

binary_answer_list = ["Y", "y", "yes", "YES", "Yes", "No", "N", "NO", "no", "n"]
remaining_pts = 0

# create character class with empty variables

class character:
    name = ""
    skills = {"Strength": 0, "Perception": 0, "Endurance": 0, "Charisma": 0, "Intelligence": 0, "Agility": 0, "Luck": 0}

    def __init__(self, inskills):
        self.name = inskills.get("name")
        self.skills = {key:inskills[key] for key in ["Strength","Perception","Endurance","Charisma","Intelligence","Agility","Luck",]}
        print(self.name, self.skills)



# function used to define all skill traits, using input attribute each time
def charcheck(attribute):
    global remaining_pts
    ipt = int(input("How many points would you like to allocate to this? "))
    leftover_pts = remaining_pts - ipt
    while ipt > 10 or ipt < 0 or leftover_pts < 0:
        ipt = int(input("Please enter a valid number between 0 and 10. Make sure you have enough points to spend for this attribute... "))
        leftover_pts = remaining_pts - ipt
    remaining_pts = leftover_pts
    print("You have {} points remaining.\n".format(remaining_pts))
    return ipt

# run through each skill trait here
def create_character():
    global remaining_pts
    happy = 0
    while(happy == 0):
        remaining_pts = 28
        name = input("Hello what is your name? ")

        print("You have 28 skills points to spend.")

        print("Strength determines your power and carry capacity.")
        s = charcheck("Strength")

        print("Perception allows you to notice things, open up new dialogue options on occasion, and how far away you start in random encounters.")
        p = charcheck("Perception")

        print("Endurance determines your hitpoints and resistance to negative effects.")
        e = charcheck("Endurance")

        print("Charisma determines your ability to communicate with others.")
        c = charcheck("Charisma")

        print("Intelligence determines your ability to learn and comprehend.")
        i = charcheck("Intelligence")

        print("Agility determines you ability to move.")
        a = charcheck( "Agility")

        print("Luck dictates the outcome of random events.")
        l = charcheck("Luck")

        # Print current values for review
        print("Strength:    ",s)
        print("Perception:  ",p)
        print("Endurance:   ",e)
        print("Charisma:    ",c)
        print("Intelligence:",i)
        print("Agility:     ",a)
        print("Luck:        ",l)
        print("Total:       ",s+p+e+c+i+a+l)

        # confirm with player if skills are okay
        con = None
        while(not (con in binary_answer_list)):
            con = input("Are you happy with your traits? \n")
        if con in binary_answer_list[:4]:
            happy = 1
        if con in binary_answer_list[4:]:
            happy = 0
        clear()
    return character({"name":name,"Strength":s,"Perception":p,"Endurance":e,"Charisma":c,"Intelligence":i,"Agility":a,"Luck":l})

