import xml.etree.ElementTree as ET
from character import character
from game import Event, getHistory, return_history
from utils import clear

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
    def load_character(self, character_name):
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
                    text = event.find("text").text
                    events = event.find("events").text
                    e = Event(name, enemies, text, events)
                    loaded_history[i] = e
                    i += 1
                getHistory(loaded_history)

                # print("Character not found")
        clear()
        c = character(character_attributes)
        return c


    def save(self, char):
        print("Quicksaving...")
        for character in self.root.iter("character"):
            if char.name == character.find('name').text:
                character.find("Strength").text = char.skills["Strength"]
                character.find("Perception").text = char.skills["Perception"]
                character.find("Endurance").text = char.skills["Endurance"]
                character.find("Charisma").text = char.skills["Charisma"]
                character.find("Intelligence").text = char.skills["Intelligence"]
                character.find("Agility").text = char.skills["Agility"]
                character.find("Luck").text = char.skills["Luck"]
                i = 0
                history = return_history()
                for event in character.findall("event"):
                    event.find("name").text = history[i].name
                    event.find("text").text = history[i].text
                    event.find("events").text = history[i].events
                    i += 1
                character.set('updated', 'yes')
            else:
                new_char = Element("character")
                new_char.find('name').text = char.name
                character.find("Strength").text = char.skills["Strength"]
                character.find("Perception").text = char.skills["Perception"]
                character.find("Endurance").text = char.skills["Endurance"]
                character.find("Charisma").text = char.skills["Charisma"]
                character.find("Intelligence").text = char.skills["Intelligence"]
                character.find("Agility").text = char.skills["Agility"]
                character.find("Luck").text = char.skills["Luck"]
                i = 0
                for e in return_history():
                    new_event = Element("event")
                    new_event.find("name").text = e.name
                    new_event.find("text").text = e.text
                    new_event.find("events").text = e.events
                    i += 1




