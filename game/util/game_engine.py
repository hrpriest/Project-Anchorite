from game.models.character import Character
from game.util.gamestate import Gamestate
from game.util.entity_system import EntitySystem
from game.util.entity_types import EntityTypes
from game.util.gui import GUI

class GameEngine:
  current_gamestate = None
  player = None
  mobs = []

  def initialize(self):
    EntitySystem.initialize()
    GUI.initialize()
  
  def start(self):
    self.current_gamestate = Gamestate.RUNNING

    # ask to create a character
    self.player = GUI.create_character_view()

    while(self.current_gamestate == Gamestate.RUNNING):
        self.main_loop()
    
    play_again = input('You lost! Play again? yes/no')
    if play_again == 'yes' or play_again == 'y':
      self.start()
    else:
      print('Thanks for playing!')

  def main_loop(self):
    # spawn mobs
    GUI.mobs_view(self.mobs)
    GUI.players_view([self.player])

    action = GUI.action_view(self.player)

    GUI.combat_view(action, self.player, self.mobs)

    if self.player.is_dead():
      self.current_gamestate = Gamestate.END
    