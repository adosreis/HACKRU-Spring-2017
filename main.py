from saving import load, open, get_characters
from character import character, create_character
from game import play

binary_answer_list = ["Y", "y", "yes", "YES", "Yes", "No", "N", "NO", "no", "n"]

if __name__ == '__main__':
    open()
    con = ""
    while(not (con in binary_answer_list)):
        con = input("Continue? Y/N?")
    if con in binary_answer_list[:4]:
        get_characters()
        c = None
        while(not c):
            c = load(input("Character name?"))
            if(not c):
                print("Character not found!")
                get_characters()
                print("try again?")
    if con in binary_answer_list[:-4]:
        c = create_character()
    play(c)