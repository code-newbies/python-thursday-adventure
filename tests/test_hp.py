import pytest
from modules.hp import Health_Points

def test_initalizing_base():
    player = Health_Points(100)
    assert player.base == 100

def test_item_bonuses_return_none():
    player = Health_Points(100)
    assert player.item_bonuses == None

def test_other_bonuses_return_none():
    player = Health_Points(100)
    assert player.other_bonuses == None
