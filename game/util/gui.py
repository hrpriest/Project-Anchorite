from game.util.entity_system import EntitySystem
from game.util.entity_types import EntityTypes
from game.models.spell import Spell
from game.models.character import Character

import sys

class GUI:
  commands = {}
  
  @classmethod
  def initialize(cls):
    cls.commands = {
      '@attack': cls.attack_view,
      '@items' : cls.item_view,
      '@quit': cls.quit_view
    }
    
  @classmethod
  def commands_view(cls):

    print('\ncommands   ')
    print('---------------')

    for key in cls.commands:
      print(key)

  @classmethod
  def quit_view(cls, player):
    print('Goodbye!')
    sys.exit(0)
  
  @classmethod
  def create_character_view(cls):
    welcome_message = '''
    Welcome to

   ___           _           _       _              _                _ _       
  / _ \_ __ ___ (_) ___  ___| |_    /_\  _ __   ___| |__   ___  _ __(_) |_ ___ 
 / /_)/ '__/ _ \| |/ _ \/ __| __|  //_\\\\| '_ \ / __| '_ \ / _ \| '__| | __/ _ \\
/ ___/| | | (_) | |  __/ (__| |_  /  _  \ | | | (__| | | | (_) | |  | | ||  __/
\/    |_|  \___// |\___|\___|\__| \_/ \_/_| |_|\___|_| |_|\___/|_|  |_|\__\___|
              |__/                                                             
                                                           
    '''
    print (welcome_message)  
    name = input('Enter your characters name: \n-> ')
    
    spells = {}
    print('\n\nChoose your first three spells: ')
    print('------------------------------------')
    cls.all_spells_view()
    while len(spells) < 3:
      spell = input('-> ')
      if spell not in EntitySystem.entities[EntityTypes.SPELLS.value]:
        print('Spell does not exist!')
        continue
      spells[spell] = Spell(spell)
    
    player = Character('player')
    player.name = name
    player.spells = spells
    return player
  
  @classmethod
  def mobs_view(cls, mobs):
    if len(mobs) <= 0:
      mob = EntitySystem.spawn_random_entity(EntityTypes.MOBS)
      print (f'\n{mob.description}, {mob.name} appears in front of you')
      mobs.append(mob)
    else:
      for mob in mobs:
        print(f'{mob.name} has {mob.current_health} hp')
        
  @classmethod
  def players_view(cls, players):
    for player in players:
      if player.is_dead():
        print(f'{player.name} died!')
      else:
        print(f'{player.name} has {player.current_health} hp')
      
  @classmethod
  def action_view(cls, player):
    action = None
    print('\nWhat would you like to do?')
    cls.commands_view()

    while action == None:
      command = input('-> ')
      if command in cls.commands:
        action = cls.commands[command](player)
      
      if action == "@back":
        print('\nWhat would you like to do?')
        action = None
    
    return action

  @classmethod
  def attack_view(cls, player):
    for spell_key, spell in player.spells.items():
      print(f'{spell_key} - {spell.name}')
    print('@back')

    spell = None
    while spell == None:  
      spell_choice = input('-> ')
      if spell_choice in player.spells:
        spell = player.spells[spell_choice]
      elif spell_choice == '@back':
        spell = spell_choice
      else:
        print('Spell not recognized.')
        spell = None
  
    return spell

  @classmethod
  def item_view(cls, player):
    if len(player.items) == 0:
      print('You have no items!')
      return '@back'
    
    for item_key, item in player.items.items():
      print(f'{item.key} - {item.name}')
    print('@back')

    item = None
    while item == None:
      item_choice = input('-> ')
      if item_choice in player.items:
        item = player.items[item_choice]
      elif item_choice == '@back':
        item = item_choice
      else:
        print('Item not recognized')
        item = None
    
    return item

  @classmethod
  def combat_view(cls, action, player, mobs):
    print(f'\n**********')
    mobs_spell = EntitySystem.spawn_random_entity(EntityTypes.SPELLS)
    for mob in mobs:
      print(f'{mob.name} used {mobs_spell.name}')
      mobs_spell.use(mob, [player])

    print(f'{player.name} used {action.name}')
    action.use(player, mobs)

    for mob in mobs[:]:
      if mob.current_health <= 0:
        print(f'{mob.name} died!')
        mobs.remove(mob)
    print(f'**********\n')

  @classmethod
  def all_spells_view(cls):
    spells = EntitySystem.get_all_entities_by_type(EntityTypes.SPELLS)
    for spell in spells:
      print(f'{spell.key} - {spell.name}')

  @classmethod
  def all_items_view(cls):
    items = EntitySystem.get_all_entities_by_type(EntityTypes.ITEMS)
    for item in items:
      print(f'{item.key} - {item.name}')