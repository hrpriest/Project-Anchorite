from random import randint
from game.util.entity_types import EntityTypes
from game.models.character import Character
from game.models.item import Item
from game.models.mob import Mob
from game.models.spell import Spell
from game.models.condition import Condition

import toml

class EntitySystem:

  def __init__(self):
    # load all entities into our system
    self.entities = {}

    for types in EntityTypes:
      self.entities[types.value] = toml.load(f'./game/assets/{types.value}.toml')   

    self.loaders = {
      EntityTypes.CHARACTERS.value : lambda key : Character(key),
      EntityTypes.ITEMS.value : lambda key : Item(key),
      EntityTypes.MOBS.value : lambda key : Mob(key),
      EntityTypes.SPELLS.value : lambda key : Spell(key),
      EntityTypes.CONDITIONS.value : lambda key : Condition(key)
    }

  def spawn_random_entity(self, entity_type):
    # spawn a random entity of certain type
    max_rand_index = len(self.entities[entity_type.value].keys()) - 1
    rand_entity_index = randint(0, max_rand_index)
    entity_name = list(self.entities[entity_type.value].keys())[rand_entity_index]
    return self.loaders[entity_type.value](entity_name)
