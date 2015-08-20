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

def test_take_damage(player):
    player.take_damage(10)
    assert player.calc_health() == 90

@pytest.fixture
def player_with_bonus(player):
    player.item_bonuses = 10
    player.other_bonuses = 15
    return player

def test_calc_health_returns_total(player_with_bonus):
    assert player_with_bonus.calc_health() == 125
    player_with_bonus.take_damage(31)
    assert player_with_bonus.calc_health() == 94

def test_print_health_function(capsys, player_with_bonus):
    print(player_with_bonus.show_health())
    output, err = capsys.readouterr()
    assert "Current Health: 125 hp\n" == output
