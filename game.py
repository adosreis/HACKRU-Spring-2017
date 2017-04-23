import random
from character import character
from combat import fight
from conversation import converse
from character import character
from utils import clear

history = [None,None,None,None,None,None,None]
char = None



# event class

class Event:
    attribute_type = ""
    name = ""
    text = []
    events = []

# event constructor

    def __init__(self, attribute_type,name, text):
        self.attribute_type =attribute_type
        self.name = name
        self.text = text


Events = [Event("Endurance","start",["You encounter a half-empty bottle of vodka in the gutter.",
"You're parched and, after all, you are in New Jersey, so a little bit of innebriation might make it a little bit better...",
"The sight of it reminds you of your father.  You see his face in the shimmer of the glass and realize that it's your reflection.  Blinded by rage, you plunge your fist into the bottle, shattering the glass along with your composure. You suck it up and move on.",
"Grab the bottle! Chug chug chug!",
	"That... wasn't vodka. You become very ill.",
"Shots, shots, shots for everyone!",
	"Those shots hit you and your friends a little too hard. Your party all becomes plastered.",
"Hmmm... I think I can make a molotov cocktail out of that!",
	"You create a molotov cocktail. Now what will you target..."],),

Event("Charisma","second",["The music playing from the radio is interrupted by sudden static sounds.",
 "It comes and goes periodically, but you think you hear voices, like someone is trying to communicate with you.",
 "The radio static makes you so angry that you decide to change the radio station. The static stops.",
"Keep listening.",
"You can't identify what the voices are saying, and they gradually disappear.",
"You turn up the volume to hear the sound louder.",
"The voices frighten you. You become a coward.",
"Twiddle with the radio dial in hopes of a better radio signal",
"You find a country music radio station and enjoy the music. You forget about the noises."],),

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
	 "'No,' she groans.  You ask again.  She calls you a dick and rolls off the hood, across the street, and onto the sidewalk."]),

Event("Luck","fourth",["While traveling on a stray isolated road in the Pine Barrens, you spot a large rustic chest among the trees right off the road. Something tells you it might contain something valuable, but you because you didn't take a history class in college you have no idea.",
"With the tools you have laying around in your car, do you dare open its contents?",
"The chest won't budge, and its sharp edges and studded design cut your fingers as you continuously try to pry the container. You get angry and declare war on the hunk of junk.",
"It's hammer time!",
"Your hammer manages to crack the chest open, but as you keep pushing down spiders spill out of the tiny creases. You panic and it slams shut. Your hammer breaks and you give up on opening it.",
"Wake up Mr. Freeman",
"You manage to pry the chest open with a crowbar, but it wasn't easy. You see a pile of golden treasure inside that you manage to grab and take back with you. However, you are exhausted.",
"Burn baby burn!",
"You lather the chest in gasoline and light a match. The wooden shell of the ancient relic smokes and burns like a campfire until nothing remains. Your hopes of treasure are dying until you spot an engraved flask in the rubble and ashes. You take a sip and taste nasty whiskey; you feel better."]),


Event("Perception","fifth",["Cracks begin to appear in the asphalt.  Jutting from one of these cracks is a pike with a severed goat head that you could have sworn watched you while you passed it. As eager as you were to shrug it off, your solace was cut short by yet another goat head on a pike.  The cracks are getting deeper.",
"Your tire gets stuck in a fissure, and before you is another pike.  This time, you're being watched by a foam mannequin head, decorated with an uncanny wig and ping-pong balls with markered-on pupils for eyes.  You hear a rustling from a nearby bush on your right, and a figure stands in the window in the house on the left. What will you do?",
"You pull the pike from the ground.  Fortunately it's heavy and it could make a good weapon to defend yourself with. You threaten the shaky bush.  A raccoon starts serpentining at you.",
"The raccoon leaps into the sharp end of your pike. No guilt here; he did it to himself. You look back over to see that the man in the window is now hidden by blinds. Out of sight, out of mind, eh?  You fill the fissure under your tire with the mannequin head and raccoon, and it seems to be enough to get your tire out so you can move on and pretend this never happened.",
"The raccoon scurries around your legs and you stumble back, trip over the rough terrain and fall. Your eyes follow the pike as it falls from your grasp and rolls to the feet of the man who was watching you from his window. 'My murals,' he says, 'do they frighten you?' You're too frightened to respond. 'They frighten many.' He says, leaning down to your arm with a syringe. The last thing you remember is the needle jabbing into your arm before you wake up in your car a few blocks down the street. The pikes are gone. Was it a dream? You feel like... this might not be the last you've seen of the goat heads and the shadowy man.",
"Gun it.",
"The tires screech and you feel the car lunging gently again and again.  You look over as the man is leaving the window.  The door begins to creak open and an amber light is cast partway across the street. The silhouette of the man narrowly creeps into frame just as the tire catches enough grip to send you wheeling down the road, away from the encounter.",
"The tire rips, shreds, then pops.  You, uhh.... what was that noise...?",
"Send your pal Dom out there to see if he can fix it.",
"Dom manages to push the car with just enough momentum to set it free from its earthy clamp.  He runs up to the side door and gets back in as it's moving and you manage to escape.",
"Dom manages to push the car with just enough momentum to set it free from its earthy clamp, but something's wrong. Dom's foot fell into a bear trap in one of the cracks in the road.  He collapses, grasping his ankle, then waves his bloodied hands as he quickly disappears in the rear view mirror.",
"Ask the man in the window for help.",
"The man comes to your aide.  He stands by your carside, still shrouded with enough shadow to conceal his face. 'What brings you here,' he asks. 'We're trying to go north, back to New York.' The man sighs. 'You may try,' he says, and as he speaks, the car starts to groan and shake.  'But there are some things you can not escape.' He turns and walks back towards the house.  The car now seems to be free, so you set forth.",
"The man stands in the window for a good while as you contemplate your next move.  In a blink, he's gone.  You ask your friends if they saw where he went, and they saw it just as you did; he was there, and now he's gone.  The earth begins to tremble.  You jostle the door handles, but they refuse to budge. The car begins to sink.  The windows become consumed by the darkness of the surrounding earth, and as the last ounce of light disappears, you hear an unknown voice say 'You will soon understand your fate.'  You peel away the blackness as you open your eyes to find that you're alive, awake, and parked in the middle of the road.  There is no crack holding your tire in place, and so you leave in silence."]),

Event("Intelligence","sixth",["You see an armchair in the middle of the road.",
"That's... odd.",
"You arm-wrestle the armchair.",
"You win! The armchair becomes your companion.",
"But... how?",
"Just drive around it.  What's the big deal?",
"You drive around it.",
"You can't drive around it. It's a really big armchair. You have to take a detour down some one-way roads and shoddy roads pocked with pot-holes.",
"We could use another armchair in the back of the van!",
"You have a new armchair! You and your companions are happier and heal faster!",
"You have a new armchair, but... it's full of lice. You and your companions take one additional point of damage each time you take damage.",
"Arm yourself. It could be preparing an armchair army.",
"You take the first shot and blow a hole right through it's cushion! This must have been an armchair scout, though, so you decide to escape quickly before armchair reinforcements arrive.",
"The armchair was a distraction!  Both sides of the car are being swarmed by armchairs, rolling down the hills.  It's really hard to understand what's happening, but the car takes some heavy damage as you escape the bizarre encounter."])]

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
    if c ==None:
        print("You're nobody!")
        return
    clear()
    global char, history
    char = c
    start = None
    if(history[0] is None):
        print("Character creation is completed! Begin new adventure!")
        e = Events[0]
        for i in range(0,6):
            if e == None:
                print("you died, sorry")
                return
            x = interpretEvent(e)
            if x and e:
                history[i+1] = Events[int(x)]
                if history[i+1]:
                    e = Events[int(interpretEvent(history[i+1]))]


    else:
        print("when we last left off!")
        e = history[history.index(None)-1]
        for i in range(history.index(None)-1, 6):
            if e == None:
                print("you died, sorry")
                return
            x = interpretEvent(e)
            if x and e:
                history[i + 1] = Events[int(x)]
                e = Events[interpretEvent(history[i + 1])]


def return_history():
    return history


