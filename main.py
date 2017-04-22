from saving import load, create_character

def game(a):

if __name__ == '__main__':
    myList = ["Y","y","yes","YES","Yes","No","N","NO","no","n"]
    con = ""
    while(not myList.Contains(con)):
        con = input("Continue? Y/N?")
    if myList[:4].Contains(con):
        print()
        load(input("Character name?"))
    if myList[:-4].Contains(con):
        create_character()

