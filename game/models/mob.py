from game.util.resource_loader import resource

@resource('./game/assets/mobs.toml')
class Mob:
    name = ''
    description = ''
    total_health = 0
    current_health = 0

    def __repr__(self):
        return f'''
\nName: {self.name}
==========================
Description: {self.description}\n'''

    def __str__(self):
        return name
