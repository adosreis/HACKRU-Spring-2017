import xml.etree.ElementTree as ET
from character import character
from game import Event, getHistory

file = "save_data.xml"

class XML:
    root = None
    def __init__(self):
        tree = ET.parse(file)
        self.root = tree.getroot()


    def get_characters(self):
        if self.root:
            for char in self.root.findall('character'):
                print(char.find("name").text)



    # loads a character (if it exists) and his history
    def load_character(self,character_name):
        character_attributes = {"name": character_name, "Strength": 0, "Perception": 0, "Endurance": 0, "Charisma": 0,"Intelligence": 0, "Agility": 0, "Luck": 0}
        for char in self.root.findall("character"):
            if character_name == char.find('name').text:
                character_attributes["Strength"] = int(char.find("Strength").text)
                character_attributes["Perception"] = int(char.find("Perception").text)
                character_attributes["Endurance"] = int(char.find("Endurance").text)
                character_attributes["Charisma"] = int(char.find("Charisma").text)
                character_attributes["Intelligence"] = int(char.find("Intelligence").text)
                character_attributes["Agility"] = int(char.find("Agility").text)
                character_attributes["Luck"] = int(char.find("Luck").text)
                loaded_history = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
                                  None, None, None, None, None]
                i = 0
                for event in char.findall("event"):
                    name = event.find("name").text
                    enemies = event.find("enemies").text
                    text = event.find("text").text
                    events = event.find("events").text
                    e = Event(name, enemies, text, events)
                    loaded_history[i] = e
                    i += 1
                getHistory(loaded_history)

                # print("Character not found")
        c = character(character_attributes)
        return c


    def save(self):
        print("nothing yet")
