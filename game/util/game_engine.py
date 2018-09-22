from game.models.character import Character
from game.util.gamestate import Gamestate
from game.util.entity_system import EntitySystem
from game.util.entity_types import EntityTypes

class GameEngine:
  entity_system = None
  current_gamestate = None
  player = None
  mobs = []

  def start(self):
    self.entity_system = EntitySystem()
    self.current_gamestate = Gamestate.RUNNING
    self.create_charcter()

    while(self.current_gamestate == Gamestate.RUNNING):
        self.main_loop()

  def create_charcter(self):
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
    player = Character('player')
    player.name = name

  def main_loop(self):
    # spawn mobs
    if len(self.mobs) <= 0:
      mob = self.entity_system.spawn_random_entity(EntityTypes.MOBS)
      print (f'{mob.description}, {mob.name} appears in front of you')
      self.mobs.append(mob)
    
    ui = input('What would you like to do? \n-> ')    

