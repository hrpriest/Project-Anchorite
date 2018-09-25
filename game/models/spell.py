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
        if self.self_damage != 0:
            print(f'{caster.name} took {self.self_damage} damage')
            caster.current_health += self.self_damage
            
        if self.self_heal != 0:
            print(f'{caster.name} healed for {self.self_heal}')
            caster.current_health += self.self_heal
        
        
        
        for target in targets:
            if self.target_damage != 0:
                print(f'{target.name} took {self.target_damage} damage')
                target.current_health -= self.target_damage
