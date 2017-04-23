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
	"You create a molotov cocktail. Now what will you target..."],[]),

Event("Charisma","second",["The music playing from the radio is interrupted by sudden static sounds.",
 "It comes and goes periodically, but you think you hear voices, like someone is trying to communicate with you.",
 "The radio static makes you so angry that you decide to change the radio station. The static stops.",
"Keep listening.",
"You can't identify what the voices are saying, and they gradually disappear.",
"You turn up the volume to hear the sound louder.",
"The voices frighten you. You become a coward.",
"Twiddle with the radio dial in hopes of a better radio signal",
"You find a country music radio station and enjoy the music. You forget about the noises."],[]),

Event("Strength","third",["You are approached by a naked woman with more wrinkles in her skin than you imagined possible.  Visibly delusional, she stumbles onto the hood of your car and begins drooling on the windshield.  She seems to be falling asleep.",
"What do you do?",
"You ball your fists, ready to give this lady a faceful of knuckle.  The way she's licking your windshield just rubs you the wrong way, and she should learn a thing or two about... whatever it is she's doing to you and your car.",
	 "You sock her right in the side of the head with such force that she flops like a fish with a moan that can only be described as goat-like.  Oh! And it looks like you managed to knock out one of her gold teeth! Score! You pocket it and return to the car.",
	 "As you approach her, the nude crude and lewd lady bucks back and kicks one of your teeth out.  While you're dizzy, she quickly stumbles away and what's better.  You've got a lisp now, dick.",
"Turn on the windshield wipers.",
	 "You wipe her arms and face off your windshield, and the rest of her body follows suit and flops to your doorside. She may be dead. But you've got more important things to do than worry about whether or not someone just died on your car.",
	 "You manage to slap her awake with your persistance, but the crazy old bat grabs the wipers and snaps them right off your car!  Where in the world did this brute strength come from?  You're not willing to find out. Your driver slams on the petal and speeds away.  The crazy old lady tumbles to the side, and the wipers go with her.",
 "Honk the horn!",
	 "The woman snaps back to life and hisses wildly, then leaps into the bushes.",
	 "Alarmed, the woman flails maniacally and percusses a series of dinks and dents into your car.",
 "Ask her to kindly remove her floppy self from your car.",
	 "The woman murmurs, 'mhmm,' and kindly removes herself from your car.",
	 "'No,' she groans.  You ask again.  She calls you a dick and rolls off the hood, across the street, and onto the sidewalk."],[])]

# event class

class Event:
    attribute_type = ""
    name = ""
    text = []
    events = []

# event constructor

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
        for i in range(0,7):
            e = Events[0]
            history[i] = interpretEvent(e)

    else:
        print("when we last left off!")
        start = history[history.index(None)-1]


def return_history():
    return history




