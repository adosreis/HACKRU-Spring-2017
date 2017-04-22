from saving import load, open, get_characters
from character import create_character

if __name__ == '__main__':
    open()
    myList = ["Y","y","yes","YES","Yes","No","N","NO","no","n"]
    con = ""
    while(not myList.Contains(con)):
        con = input("Continue? Y/N?")
    if myList[:4].Contains(con):
        get_characters()
        load(input("Character name?"))
    if myList[:-4].Contains(con):
        create_character()

