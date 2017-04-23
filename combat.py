from character import character
from utils import clear
import random

# define fight function
def fight(char,event):
    clear()
    print("you done messed up now bruh, you gotta fight")
    print(event.text[2])
    skill_of_combat =[]
    skill_picker = ["Strength", "Perception", "Endurance", "Charisma", "Intelligence", "Agility", "Luck"]
    # pick 3 random skills from character traits
    for i in range(3):
        skill_of_combat.append(char.skills.get(random.choice(skill_picker)))
    total = 0
    ai_total = 0
    # compare 3 random skills to random AI total
    for skill in skill_of_combat:
        total += skill
        ai_total+= random.randint(0,10)
    # if player total exceeds AI total, player wins combat roll; otherwise player partakes in 'combat'
    if total > ai_total:
        print("ok you win!")
        return random.randint(1,6)#broke
    else:
        print("you lost")
        return 0#broke
