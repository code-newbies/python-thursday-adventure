import pytest
from modules.hp import HealthPoints
from modules.engine import Engine

@pytest.fixture
def player():
    player = HealthPoints(100)
    return player

@pytest.fixture
def player_with_bonus():
    player = HealthPoints(100)
    player.item_bonuses = 10
    player.other_bonuses = 15
    return player

def test_initalizing_base(player):
    assert player.base == 100

def test_item_bonuses_return_none(player):
    assert player.item_bonuses == 0

def test_other_bonuses_return_none(player):
    assert player.other_bonuses == 0

def test_calc_health_returns_total(player):
    player.item_bonuses = 10
    player.other_bonuses = 15
    total = player.calc_health()
    assert total == 125

def test_print_health_function(capsys, player_with_bonus):
    print(player_with_bonus)
    output, err = capsys.readouterr()
    assert "Current Health: 125 hp\n" == output
