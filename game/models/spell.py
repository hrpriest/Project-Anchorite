from game.util.resource_loader import resource

@resource('./game/assets/spells.toml')
class Spell:
    name = ''
    description = ''
    target_damage = 0 
    self_damage = 0
    self_heal = 0
    action_point_cost = 0 
    crit_chance = 0.0
    damage_type = ''
    miss_chance = 0.0
    target_conditions = []

    def __str__(self):
        return 'name'
        
    def use(self, caster, targets):
        pass