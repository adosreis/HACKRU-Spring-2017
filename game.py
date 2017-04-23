import random
from character import character
from combat import fight
from conversation import converse
from character import character
from utils import clear

history = [None,None,None,None,None,None,None]
char = None

Events = [Event("Intelligence","start",["You encounter a half-empty bottle of vodka in the gutter.",
"You're parched and, after all, you are in New Jersey, so a little bit of innebriation might make it a little bit better...",
"The sight of it reminds you of your father.  You see his face in the shimmer of the glass and realize that it's your reflection.  Blinded by rage, you plunge your fist into the bottle, shattering the glass along with your composure. You suck it up and move on.",
"Grab the bottle! Chug chug chug!",
	"That... wasn't vodka. You become very ill.",
"Shots, shots, shots for everyone!",
	"Those shots hit you and your friends a little too hard. Your party all becomes plastered.",
"Hmmm... I think I can make a molotov cocktail out of that!",
	"You create a molotov cocktail. Now what will you target..."],[]), Event("Charisma","second",["The music playing from the radio is interrupted by sudden static sounds.",
          "It comes and goes periodically, but you think you hear voices, like someone is trying to communicate with you.",
          "The radio static makes you so angry that you decide to change the radio station. The static stops.",
          "Keep listening.",
            "You can't identify what the voices are saying, and they gradually disappear.",
          "You turn up the volume to hear the sound louder.",
            "The voices frighten you. You become a coward.",
          "Twiddle with the radio dial in hopes of a better radio signal",
            "You find a country music radio station and enjoy the music. You forget about the noises."],[])]

class Event:
    attribute_type = ""
    name = ""
    text = []
    events = []


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
    global char, history
    char = c
    start = None
    print(c)
    if(history[0] is None):
        print("Character creation is completed! Begin new adventure!")

    else:
        print("when we last left off!")
        start = history[history.index(None)-1]


def return_history():
    return history




