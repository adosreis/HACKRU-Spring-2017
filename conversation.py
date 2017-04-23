import random
# define converse function to process event text and responses

def converse(char, event):
    print(event.text[0])
    print(event.text[1])
    print("Your available options are:")
    print("1: ", event.text[3])
    print("2: ", event.text[5])
    print("3: ", event.text[7])
    response = int(input("What do you do? "))
    if response == 1:
        print(event.text[4])
        return random.randint(2,4)
    if response == 2:
        print(event.text[6])
        return random.randint(5,7)
    if response == 3:
        print(event.text[8])
        return random.randint(7,9)

# event texts used for reference

