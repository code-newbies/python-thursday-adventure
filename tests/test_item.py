import pytest
from modules.item import Item
from modules.locatable import Locatable

class TestItem:
    def test_item_accepts_name_desc_on_init(self):
        item = Item("dragonglass", "seeing dragons")
        assert item.name == "dragonglass"
        assert item.description == "seeing dragons"

    def test_item_is_locatable(self):
        assert Locatable in Item.__bases__
