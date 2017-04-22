history = [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]

class Event:
    name = ""
    enemies = []
    text = {}
    events = {}

    def __init__(self, name, enemies, text, events):
        self.name = name
        self.enemies = enemies
        self.text = text
        self.events = events

def getHistory(loaded_history):
    current_history = loaded_history


