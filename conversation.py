def converse(event):
    print(event[0])
    print(event[1])
    print("Your available options are:")
    print("1: ", event[3])
    print("2: ", event[5])
    print("3: ", event[7])
    response = int(input("What do you do? "))
    if response == 1:
        print(event[4])
    if response == 2:
        print(event[6])
    if response == 3:
        print(event[8])



Event1 = ["You encounter a half-empty bottle of vodka in the gutter.",
"You're parched and, after all, you are in New Jersey, so a little bit of innebriation might make it a little bit better...",
"The sight of it reminds you of your father.  You see his face in the shimmer of the glass and realize that it's your reflection.  Blinded by rage, you plunge your fist into the bottle, shattering the glass along with your composure. You suck it up and move on.",
"Grab the bottle! Chug chug chug!",
	"That... wasn't vodka. You become very ill.",
"Shots, shots, shots for everyone!",
	"Those shots hit you and your friends a little too hard. Your party all becomes plastered.",
"Hmmm... I think I can make a molotov cocktail out of that!",
	"You create a molotov cocktail. Now what will you target..."]

Event2 = ["The music playing from the radio is interrupted by sudden static sounds.",
          "It comes and goes periodically, but you think you hear voices, like someone is trying to communicate with you.",
          "The radio static makes you so angry that you decide to change the radio station. The static stops.",
          "Keep listening.",
            "You can't identify what the voices are saying, and they gradually disappear.",
          "You turn up the volume to hear the sound louder.",
            "The voices frighten you. You become a coward.",
          "Twiddle with the radio dial in hopes of a better radio signal",
            "You find a country music radio station and enjoy the music. You forget about the noises."]

Event3 = []


