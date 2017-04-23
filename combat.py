from character import character
import random
# define fight function
def fight(char,event):
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
        return event.events[3]
    else:
        return event.events[4]
