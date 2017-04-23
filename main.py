from saving import load_character, open, get_characters
from character import create_character,binary_answer_listy
from game import play



if __name__ == '__main__':
    open()
    con = ""
    while(not (con in binary_answer_list)):
        con = input("Continue? Y/N?")
    if con in binary_answer_list[:4]:
        get_characters()
        c = None
        while(not c):
            c = load_character(input("Character name?"))
            if(not c):
                print("Character not found!")
                get_characters()
                print("try again?")
    if con in binary_answer_list[:-4]:
        c = create_character()
    play(c)