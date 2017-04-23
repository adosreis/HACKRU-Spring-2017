from saving import XML
from character import create_character,binary_answer_list
from game import play
from utils import clear



if __name__ == '__main__':
    print("Escape: New Jersey")
    root = XML()
    con = ""
    while(not (con in binary_answer_list)):
        con = input("Continue from last save? Y/N?")
    if con in binary_answer_list[:4]:
        clear()
        root.get_characters()
        c = None
        while(not c):
            c = root.load_character(input("Character name?"))
            if(not c):
                print("Character not found!")
                root.get_characters()
                print("try again?")
    if con in binary_answer_list[4:]:
        clear()
        c = create_character()
    play(c)
    root.save(c)
