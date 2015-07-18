import pytest
from modules.world import World

class TestWorld:
    def setup_method(self, method):
        self.world = World()

    def test_world_has_initial_narration_method(self):
        intro = self.world.initial_narration()
        assert "bacon" in  intro

    def test_world_initial_narration_returns_a_long_description(self):
        intro = self.world.initial_narration()
        assert 250 < len(intro)


