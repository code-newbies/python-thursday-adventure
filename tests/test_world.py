import pytest
from modules.world import initial_narration

def test_world_has_initial_narration_method():
    intro = initial_narration()
    assert "bacon" in  intro

def test_world_initial_narration_returns_a_long_description():
    intro = initial_narration()
    assert 250 < len(intro)


