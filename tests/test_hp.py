import pytest
from modules.hp import HealthPoints

@pytest.fixture
def player():
    player = HealthPoints(100)
    return player

def test_initalizing_base(player):
    assert player.base == 100

def test_item_bonuses_return_none(player):
    assert player.item_bonuses == None

def test_other_bonuses_return_none(player):
    assert player.other_bonuses == None

def test_calc_health_returns_total(player):
    player.item_bonuses = 10
    player.other_bonuses = 15
    total = player.calc_health()
    assert total == 125
