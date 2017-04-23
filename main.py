from saving import XML
from character import create_character,binary_answer_list
from game import play
from utils import clear



if __name__ == '__main__':
    print("Escape: New Jersey\n"
          "Well, that sucks! Looks like you're stuck in SUICIDE HEIGHTS, in the dreaded state NEW JERSEY. It can't be too hard to escape, right? \n"
          "Unfortunately, you're horribly mistaken.  You'll probably encounter a series of EVENTS that unwillingly happen to you and your party of THREE RELATIVELY NONDESCRIPT COMPANIONS.n "
          "All you have to do is decide which unfortunate thing you want to have happen. There are different possible outcomes for each choice you make depending on the LIKELIHOOD of your success,\n"
          " based on whatever RELEVENT STAT is applicable to the situation and a RANDOMLY GENERATED NUMBER from the opponent. That's right. You're fighting numbers. Can you win and find your way home?\n"
          "... Well, no you can't. This is a trial version. As of right now, escape is just a pipe dream, and you're just playing for the sadistic amusement. \n"
          "Enjoy!\n"
          "- Dev. Team \n")

    root = XML()
    con = ""
    while(not (con in binary_answer_list)):
        con = input("Continue from last save? Y/N? \n")
    if con in binary_answer_list[:4]:
        clear()
        root.get_characters()
        c = None
        while(not c):
            c = root.load_character(input("Character name? \n"))
            if(not c):
                print("Character not found!")
                root.get_characters()
                print("try again?")
    if con in binary_answer_list[4:]:
        clear()
        c = create_character()
    play(c)
    root.save(c)
