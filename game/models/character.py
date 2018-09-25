from game.util.resource_loader import resource

@resource('./game/assets/characters.toml')
class Character:
  action_points = 0
  spells = {}
  items = {}
  total_health = 0
  current_health = 0

  def is_dead(self):
    return self.current_health <= 0