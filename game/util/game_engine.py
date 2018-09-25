from game.models.character import Character
from game.util.gamestate import Gamestate
from game.util.entity_system import EntitySystem
from game.util.entity_types import EntityTypes
from game.util.gui import GUI

class GameEngine:
  current_gamestate = None
  player = None
  mobs = []

  def start(self):
    EntitySystem.initialize()
    GUI.initialize()
    self.current_gamestate = Gamestate.RUNNING

    # ask to create a character
    self.player = GUI.create_character_view()

    while(self.current_gamestate == Gamestate.RUNNING):
        self.main_loop()    
    

  def main_loop(self):
    # spawn mobs
    GUI.mobs_view(self.mobs)

    action = GUI.action_view(self.player)

    GUI.combat_view(action, self.player, self.mobs)
    
    

