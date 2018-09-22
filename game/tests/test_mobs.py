from game.models.mob import Mob

def test_mobs():
    orc = Mob('orc')

    print(repr(orc))

    assert orc.total_health != 0
    assert orc.current_health != 0
    assert orc.name != ''
    assert orc.key == 'orc'
