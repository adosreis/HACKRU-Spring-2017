from saving import load, open, get_characters
from character import character, create_character

binary_answer_list = ["Y", "y", "yes", "YES", "Yes", "No", "N", "NO", "no", "n"]

if __name__ == '__main__':
    open()
    con = ""
    while(not (con in binary_answer_list)):
        con = input("Continue? Y/N?")
    if con in binary_answer_list[:4]:
        get_characters()
        load(input("Character name?"))
    if con in binary_answer_list[:-4]:
        create_character()

