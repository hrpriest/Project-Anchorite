from random import randint
from game.util.entity_types import EntityTypes
from game.models.character import Character
from game.models.item import Item
from game.models.mob import Mob
from game.models.spell import Spell
from game.models.condition import Condition

import toml

class EntitySystem:
  entities = {}

  def initialize():
    # load all entities into our system
    for types in EntityTypes:
      EntitySystem.entities[types.value] = toml.load(f'./game/assets/{types.value}.toml')   

    EntitySystem.loaders = {
      EntityTypes.CHARACTERS.value : lambda key : Character(key),
      EntityTypes.ITEMS.value : lambda key : Item(key),
      EntityTypes.MOBS.value : lambda key : Mob(key),
      EntityTypes.SPELLS.value : lambda key : Spell(key),
      EntityTypes.CONDITIONS.value : lambda key : Condition(key)
    }

  @staticmethod
  def spawn_random_entity(entity_type):
    # spawn a random entity of certain type
    max_rand_index = len(EntitySystem.entities[entity_type.value].keys()) - 1
    rand_entity_index = randint(0, max_rand_index)
    entity_name = list(EntitySystem.entities[entity_type.value].keys())[rand_entity_index]
    return EntitySystem.loaders[entity_type.value](entity_name)

  @staticmethod
  def get_all_entities_by_type(entity_type):
    entities = []
    for key in EntitySystem.entities[entity_type.value].keys():
      entities.append(EntitySystem.loaders[entity_type.value](key))
    return entities