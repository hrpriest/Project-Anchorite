from game.models.condition import Condition

def test_conditions():
    condition = Condition('burn')
    print(condition.name)
