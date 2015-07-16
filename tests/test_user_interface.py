import pytest
from modules.world import CommandLineInterface
from os import getcwd
from os.path import join

@pytest.mark.usefixtures("prepare_ui")
class TestKnot:
    @pytest.fixture()
    def prepare_ui(self):
        pass
 
    def test_knot_will_accept_story_path(self):
        pass
