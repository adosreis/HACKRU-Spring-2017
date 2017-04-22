import xml.etree.ElementTree as ET
from character import character
from game import Event, getHistory


file = "save_data.xml"
root = None

def open():
    tree = ET.parse(file)
    root = tree.getroot()
def get_characters():
    if root:
        for character in root.findall("character"):
            print(character.get('name'))
    else:
        open()
        get_characters()

# loads a character (if it exists) and his history
def load(character_name):
    character_attributes = {"name": character_name, "Strength": 0, "Perception": 0, "Endurance": 0, "Charisma": 0, "Intelligence": 0, "Agility": 0, "Luck":0}
    for character in root.findall("character"):
        if character_name is character.get('name'):
            character_attributes["Strength"] = character.get("Strength")
            character_attributes["Perception"] = character.get("Perception")
            character_attributes["Endurance"] = character.get("Endurance")
            character_attributes["Charisma"] = character.get("Charisma")
            character_attributes["Intelligence"] = character.get("Intelligence")
            character_attributes["Agility"] = character.get("Agility")
            character_attributes["Luck"] = character.get("Luck")
            loaded_history = []
            for event in character.findall("event"):
                name = event.get("name")
                enemies = event.get("enemies")
                text = event.get("text")
                events = event.get("events")
                e = Event(name, enemies, text, events)
                loaded_history.append(e)
            getHistory(loaded_history)
        else:
            print("Character not found")
def save():
    print("nothing yet")
