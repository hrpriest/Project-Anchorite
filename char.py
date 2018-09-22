import random

class Character:
    
    strength = random.randint(250, 750)
    dexterity = random.randint(250, 750)
    magic = random.randint(250, 750)
    health_points = 2000
    
    def __init__ (self, u_name, u_gender, u_class):

        self.u_name = u_name
        self.gender = u_gender
        self.u_class = u_class