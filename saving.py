import xml.etree.ElementTree as ET
from character import character
from game import Event, getHistory, return_history
from utils import clear

file = "save_data.xml"

class XML:
    root = None
    tree = None
    def __init__(self):
        self.tree = ET.parse(file)
        self.root = self.tree.getroot()


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
                loaded_history = [None, None, None, None, None, None, None]
                i = 0
                for event in char.findall("event"):
                    name = event.find("name").text
                    text = event.find("text").text.split()
                    events = event.find("events").text.split()
                    attribute = event.find("attribute").text
                    e = Event(attribute, name, text, events)
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
            print("a")
            if char.name == character.find('name').text:
                print("b")
                character.find("Strength").text = str(char.skills["Strength"])
                character.find("Perception").text = str(char.skills["Perception"])
                character.find("Endurance").text = str(char.skills["Endurance"])
                character.find("Charisma").text = str(char.skills["Charisma"])
                character.find("Intelligence").text = str(char.skills["Intelligence"])
                character.find("Agility").text = str(char.skills["Agility"])
                character.find("Luck").text = str(char.skills["Luck"])
                i = 0
                history = return_history()
                for event in character.findall("event"):
                    print("c")
                    event.find("attribute").text = history[i].attribute_type
                    event.find("name").text = history[i].name
                    event.find("text").text = history[i].text
                    event.find("events").text = history[i].events
                    i += 1
                character.set('updated', 'yes')
                break
        else:
            print("d")
            new_char = ET.Element("character")
            e = ET.Element('name')
            e.text = str(char.name)
            new_char.append(e)
            e = ET.Element("Strength")
            e.text = str(char.skills["Strength"])
            new_char.append(e)
            e = ET.Element("Perception")
            e.text = str(char.skills["Perception"])
            new_char.append(e)
            e = ET.Element("Endurance")
            e.text = str(char.skills["Endurance"])
            new_char.append(e)
            e = ET.Element("Charisma")
            e.text = str(char.skills["Charisma"])
            new_char.append(e)
            e = ET.Element("Intelligence")
            e.text = str(char.skills["Intelligence"])
            new_char.append(e)
            e = ET.Element("Agility")
            e.text = str(char.skills["Agility"])
            new_char.append(e)
            e = ET.Element("Luck")
            e.text = str(char.skills["Luck"])
            new_char.append(e)
            i = 0
            h = ET.Element("history")
            for e in return_history():
                print("e")
                if e:
                    new_event = ET.Element("event")
                    a = ET.Element("name")
                    a.text = e.name
                    new_event.append(a)
                    a = ET.Element("text")
                    a.text = e.text
                    new_event.append(a)
                    a = ET.Element("events")
                    a.text = e.text
                    new_event.append(a)
                    i += 1
                    h.append(new_event)
            left = 7-i
            #for i in range (left):
               # h.append(Event(new_event))
            new_char.append(h)
            self.root.append(new_char)
        print("trying to write")
        self.tree.write(str(file))




