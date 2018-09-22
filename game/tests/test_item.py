from game.item import Item

def test_item():
    bow = Item('strong_bow')

    print(repr(bow))

    assert bow.range != 0
    assert bow.name != ''
    assert bow.key == 'strong_bow'
