import random
from character import character
from combat import fight
from conversation import converse

history = [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]
character = None

class Event:
    name = ""
    enemies = []
    text = {}
    events = {}



    def __init__(self, name, enemies, text, events):
        self.name = name
        self.enemies = enemies
        self.text = text
        self.events = events

def interpretEvent(event):
    skill_picker = ["Strength","Perception","Endurance","Charisma","Intelligence","Agility","Luck"]
    skill_roll = character.skills.get(random.choice(skill_picker))
    if(random.randint(1,9) > skill_roll):
        fight(event)
    else:
        converse(event)



def getHistory(loaded_history):
    for i in range(20):
        history[i] = loaded_history[i]

def play(c):
    character = c
    if(history[0] is None):
        print("a new story starts!")
    else:
        print("when we last left off!")
        start = history[history.index(None)-1]




