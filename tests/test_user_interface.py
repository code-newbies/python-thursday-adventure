import pytest
from modules.command_line import CommandLine
from os import getcwd
from os.path import join

# Example of native py.test style test
@pytest.mark.usefixtures("prepare_ui")
class TestKnot:
    @pytest.fixture()
    def prepare_ui(self):
        pass

    def test_knot_will_accept_story_path(self):
        pass
