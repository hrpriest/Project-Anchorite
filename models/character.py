import random

class Character:
    
    strength = random.randint(250, 750)
    dexterity = random.randint(250, 750)
    magic = random.randint(250, 750)
    health_points = 2000
    mana = 100
    
    def __init__ (self, name, gender, class_type):

        self.name = name
        self.gender = gender
        self.class_type = class_type
        