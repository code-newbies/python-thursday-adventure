import pytest
from modules.item import Item
from modules.bag import Bag

class TestBag:
    def setup_method(self, method):
        self.bag = Bag()

    def teardown_method(self, method):
        self.bag = None

    def bag_n_dump(self, name):
        item = Item(name)
        self.bag.add(item)
        return self.bag.dump()

    def test_check_if_bag_object(self):
        assert type(self.bag) is Bag

    def test_check_if_item_object(self):
        assert Item in Bag.__bases__

    def test_check_if_name_description_can_be_assigned(self):
        self.bag.name = "The Bag"
        self.bag.description = "for carrying"
        assert self.bag.name == "The Bag"
        assert self.bag.description, "for carrying"

    def test_can_check_bag_to_see_if_empty(self):
        assert self.bag.is_empty()

    def test_can_return_item_count_when_empty(self):
        assert self.bag.item_count() == 0
    
    def test_after_adding_item_bag_is_no_longer_empty(self):
        item = Item("rock")
        self.bag.add(item)
        assert not self.bag.is_empty()

    def test_can_add_item_to_bag(self):
        assert self.bag.item_count() == 0
        item = Item("thing")
        self.bag.add(item)
        assert self.bag.item_count() == 1
       
    def test_dumped_pile_has_count(self):
        pile = self.bag_n_dump('fuzz')

        assert len(pile) == 1 
        fuzz = pile['fuzz']
        assert fuzz["count"] == 1

    def test_dumped_pile_has_name(self):
        pile = self.bag_n_dump('cheese')

        cheese = pile['cheese']
        assert cheese["name"] == "cheese"

    def test_dumped_pile_has_item(self):
        pile = self.bag_n_dump('Amulet of Wendor')

        amulet = pile['Amulet of Wendor']
        item = amulet['item']
        assert type(item) is Item

    def test_can_look_in_bag(self):
        stick = Item("stick")
        self.bag.add(stick)
        seen = self.bag.look()
        assert "1 stick" in seen
    
    def test_can_fund_how_many_of_an_item_are_in_bag(self):
        planet = Item("planet")
        self.bag.add(planet)
        self.bag.add(planet)
        assert 2 == self.bag.how_many("planet")

    def test_how_many_handles_no_items_of_type(self):
        assert self.bag.how_many("jabberwocky") == 0

    def test_adding_multiple_of_the_same_item_increases_item_count(self):
        butter = Item("butter")
        self.bag.add(butter)
        self.bag.add(butter)
        assert 2 == self.bag.item_count()
        self.bag.add(butter)
        assert 3 == self.bag.item_count()

    def test_can_add_many(self):
        turtle = Item("turtle")
        self.bag.add_many(turtle, 5)
        assert 5 == self.bag.how_many("turtle")
        assert 5 == self.bag.item_count()

    def test_can_remove_an_item(self):
        self.bag.add(Item("cheezburger"))
        removed_count, item = self.bag.remove("cheezburger")
        assert 1 == removed_count
        assert "cheezburger" == item.name
        assert type(item) is Item
        assert 0 == self.bag.how_many("cheezburger")
    
    def test_cannot_remove_an_item_that_is_not_there(self):
        removed_count, item = self.bag.remove("Kaiser Soze")
        assert 0 == removed_count
        assert item == None
        assert 0 == self.bag.how_many("Kaiser Soze")

    def test_removed_items_behave_like_items_that_never_existed(self):
        self.bag.add(Item("smoke"))
        removed_count, item = self.bag.remove("smoke")
        assert 1 == removed_count

        removed_count, item = self.bag.remove("smoke")
        assert 0 == removed_count
        assert item == None
        assert 0 == self.bag.how_many("smoke")
        assert 0 == self.bag.item_count()
        
    def test_remove_many_items_from_bag_at_once(self):
        self.bag.add_many(Item("blind mouse"), 5)
        removed_count, item = self.bag.remove_many("blind mouse", 3)
        assert 3 == removed_count
        assert 2 == self.bag.how_many("blind mouse")
        assert "blind mouse" == item.name

    def test_remove_many_items_will_remove_only_as_many_as_exist(self):
        self.bag.add_many(Item("rhymes"), 5)
        removed_count, item = self.bag.remove_many("rhymes", 7)
        assert 5 == removed_count
        assert 0 == self.bag.how_many("rhymes")
        assert "rhymes" == item.name
        assert self.bag.isEmpty()

    def test_adding_multiple_of_the_same_item_increases_item_count(self):
        butter = Item("butter")
        self.bag.add(butter)
        self.bag.add(butter)
        assert 2 == self.bag.item_count()
        self.bag.add(butter)
        assert 3 == self.bag.item_count()

    def test_can_remove_an_item(self):
        self.bag.add(Item("cheezburger"))
        removed_count, item = self.bag.remove("cheezburger")
        assert 1 == removed_count
        assert "cheezburger" == item.name
        assert type(item) is Item
        assert 0 == self.bag.how_many("cheezburger")
    
    def test_cannot_remove_an_item_that_is_not_there(self):
        removed_count, item = self.bag.remove("Kaiser Soze")
        assert 0 == removed_count
        assert item == None
        assert 0 == self.bag.how_many("Kaiser Soze")

    def test_removed_items_behave_like_items_that_never_existed(self):
        self.bag.add(Item("smoke"))
        removed_count, item = self.bag.remove("smoke")
        assert 1 == removed_count

        removed_count, item = self.bag.remove("smoke")
        assert 0 == removed_count
        assert item == None
        assert 0 == self.bag.how_many("smoke")
        assert 0 == self.bag.item_count()
        
    def test_remove_many_items_from_bag_at_once(self):
        self.bag.add_many(Item("blind mouse"), 5)
        removed_count, item = self.bag.remove_many("blind mouse", 3)
        assert 3 == removed_count
        assert 2 == self.bag.how_many("blind mouse")
        assert "blind mouse" == item.name 

    def test_remove_many_items_will_remove_only_as_many_as_exist(self):
        self.bag.add_many(Item("rhymes"), 5)
        removed_count, item = self.bag.remove_many("rhymes", 7)
        assert 5 == removed_count
        assert 0 == self.bag.how_many("rhymes")
        assert "rhymes" == item.name

