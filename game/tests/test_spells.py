from game.models.spell import Spell

def test_spell():
    spell = Spell('lightning_bolt')
    print(spell.name)