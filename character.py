fron main import binary_answer_list
# call empty skills if starting new game
# else load current skills


class character:
    name = ""
    skills = {"Strength": 0, "Perception": 0, "Endurance": 0, "Charisma": 0, "Intelligence": 0, "Agility": 0, "Luck": 0}

    def __init__(self, skills):
        self.name = skills.get("name")
        self.skills = skills[:1]

def create_character():
    remaining_pts = 28
    happy = 0
    while(happy == 0):
        name = input("Hello what is your name?")
        print("Description of Strength")
        s = input("How many points would you like to allocate to Strength")
        print("Description of perception")
        p = input("How many points would you like to allocate to Perception")
        print("Description of Endurance")
        e = input("How many points would you like to allocate to Endurance")
        print("Description of Charisma")
        c = input("How many points would you like to allocate to Charisma")
        print("Description of Intelligence")
        i = input("How many points would you like to allocate to Intelligence")
        print("Description of Agility")
        a = input("How many points would you like to allocate to Agility")
        print("Description of Luck")
        l = input("How many points would you like to allocate to Luck")
        con = ""

        while(not (con in binary_answer_list):
            input("")