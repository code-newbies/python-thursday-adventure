import pytest
from modules.weapon import Weapon

@pytest.mark.usefixtures("setup")
class TestWeapon:
    @pytest.fixture()
    def setup(self):
        pass
 
    def test_weapon_has_damage_on_init(self):
        dagger = Weapon(10)
        assert dagger.damage == 10

    def test_if_weapon_item_attributes_are_accessible(self):
        dagger = Weapon(10)
        assert dagger.name == None
        assert dagger.description == None
        dagger.name, dagger.description = "sharp", "pointy"
        assert dagger.name == "sharp"
        assert dagger.description == "pointy"

