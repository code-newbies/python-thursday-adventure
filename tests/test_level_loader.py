import pytest
from modules.level_loader import LevelLoader, hydrate
from tests.helpers import locations

@pytest.fixture
def loader():
    return LevelLoader(None, None)

def test_level_loader_has_content_list(loader):
    assert len(loader.contents) == 0

def test_reset_resets_content_list(loader):
    loader.contents.append("lions and tigers and bears")
    loader.reset()
    assert len(loader.contents) == 0

def test_reset_resets_exit_text(loader):
    loader.exit_text = "and they all lived happily ever after"
    loader.reset()
    assert None == loader.exit_text

def test_reset_resets_description(loader):
    loader.description = "filled with unicorns and daisies"
    loader.reset()
    assert None == loader.description

def test_reset_resets_name(loader):
    loader.name = "foo"
    loader.reset()
    assert None == loader.name

def test_reset_resets_next_level(loader):
    loader.next_level = "7th level"
    loader.reset()
    assert None == loader.next_level

def test_hydrate_creates_locatables(locations):
    contents = hydrate(locations)
    assert len(contents) == 5

def test_loader_passes_target_if_applicable(locations):
    contents = hydrate(locations)
    
    exit = list(filter( lambda x : x.name == "exit" , contents))[0]
    roach = list(filter( lambda x : x.name == "cockroach", contents))[0]
    sword = list(filter( lambda x : x.name == "excalibur", contents))[0]
    assert roach.target.coords == exit.locate()
    assert sword.damage == 20
