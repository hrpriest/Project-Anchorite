from game.util.resource_loader import resource

@resource('./game/assets/conditions.toml')
class Condition:
    name = ''
    description = ''
    damage = 0 
    duration = 0
