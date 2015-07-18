import pytest
from modules.items import Item

class TestItem:
    def test_item_accepts_name_desc_on_init(self):
        item = Item("dragonglass", "seeing dragons")
        assert item.name == "dragonglass"
        assert item.description == "seeing dragons"
