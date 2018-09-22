from enum import Enum

class Gamestate(Enum):
    READY = 1
    RUNNING = 2
    DONE = 3

    def __init__(self, gamestate = Gamestate.INITIAL):
        self.current_gamestate = gamestate