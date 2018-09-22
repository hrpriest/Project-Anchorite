from game.util.resource_loader import resource

@resource('./game/assets/items.toml')
class Item:
    name = ''
    description = ''

    def __repr__(self):
        return f'''
\nName: {self.name}
==========================
Description: {self.description}\n'''

    def __str__(self):
        return name
