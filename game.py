import random
from character import character
from combat import fight
from conversation import converse
from character import character
from utils import clear

history = [None,None,None,None,None,None,None]
char = None

class Event:
    attribute_type = ""
    name = ""
    text = {}
    events = {}


    def __init__(self, attribute_type,name, text, events):
        self.attribute_type =attribute_type
        self.name = name
        self.text = text
        self.events = events

def interpretEvent(event):
    global char
    if(random.randint(1,9) > char.skills.get(event.attribute_type)):
        return fight(char,event)
    else:
        return converse(char,event)



def getHistory(loaded_history):
    for i in range(7):
        history[i] = loaded_history[i]

def play(c):
    clear()
    global char
    char = c
    start = None
    if(history[0] is None):
        print("a new story starts!")

    else:
        print("when we last left off!")
        start = history[history.index(None)-1]

def return_history():
    return history




