from saving import XML
from character import create_character,binary_answer_list
from game import play



if __name__ == '__main__':
    root = XML()
    con = ""
    while(not (con in binary_answer_list)):
        con = input("Continue? Y/N?")
    if con in binary_answer_list[:4]:
        root.get_characters()
        c = None
        while(not c):
            c = root.load_character(input("Character name?"))
            if(not c):
                print("Character not found!")
                root.get_characters()
                print("try again?")
    if con in binary_answer_list[:-4]:
        c = create_character()
    play(c)