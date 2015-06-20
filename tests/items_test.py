import unittest
from modules.items import Bag
from modules.items import Item

class ItemTest(unittest.TestCase):
    def test_item_accepts_name_on_init(self):
        item = Item("dragonglass")
        self.assertEqual(item.name, "dragonglass")

class BagTest(unittest.TestCase):
    def setUp(self):
        self.bag = Bag()

    def tearDown(self):
        self.bag = None

    def test_can_check_bag_to_see_if_empty(self):
        self.assertTrue(self.bag.is_empty())

    def test_can_return_item_count_when_empty(self):
        self.assertEqual(self.bag.item_count(), 0)
    
    def test_after_adding_item_bag_is_no_longer_empty(self):
        item = Item("rock")
        self.bag.add(item)
        self.assertFalse(self.bag.is_empty())

    def test_can_add_item_to_bag(self):
        self.assertEqual(self.bag.item_count(), 0)
        item = Item("thing")
        self.bag.add(item)
        self.assertEqual(self.bag.item_count(), 1)
       
    def bag_n_dump(self, name):
        item = Item(name)
        self.bag.add(item)
        return self.bag.dump()

    def test_dumped_pile_has_count(self):
        pile = self.bag_n_dump('fuzz')

        self.assertEqual(len(pile), 1)
        fuzz = pile['fuzz']
        self.assertEqual(fuzz["count"], 1)

    def test_dumped_pile_has_name(self):
        pile = self.bag_n_dump('cheese')

        cheese = pile['cheese']
        self.assertEqual(cheese["name"], "cheese")

    def test_dumped_pile_has_item(self):
        pile = self.bag_n_dump('Amulet of Wendor')

        amulet = pile['Amulet of Wendor']
        item = amulet['item']
        self.assertIsInstance(item, Item)

    def test_can_look_in_bag(self):
        stick = Item("stick")
        self.bag.add(stick)
        seen = self.bag.look()
        self.assertIn("1 stick", seen)
    
    def test_can_fund_how_many_of_an_item_are_in_bag(self):
        planet = Item("planet")
        self.bag.add(planet)
        self.bag.add(planet)
        self.assertEqual(2, self.bag.how_many("planet"))

    def test_how_many_handles_no_items_of_type(self):
        self.assertEqual(0, self.bag.how_many("jabberwocky"))

    def test_adding_multiple_of_the_same_item_increases_item_count(self):
        butter = Item("butter")
        self.bag.add(butter)
        self.bag.add(butter)
        self.assertEqual(2, self.bag.item_count())
        self.bag.add(butter)
        self.assertEqual(3, self.bag.item_count())

    def test_can_add_many(self):
        turtle = Item("turtle")
        self.bag.add_many(turtle, 5)
        self.assertEqual(5, self.bag.how_many("turtle"))
        self.assertEqual(5, self.bag.item_count())

    def test_can_remove_an_item(self):
        self.bag.add(Item("cheezburger"))
        removed_count, item = self.bag.remove("cheezburger")
        self.assertEqual(1, removed_count)
        self.assertEqual("cheezburger", item.name)
        self.assertIsInstance(item, Item)
        self.assertEqual(0, self.bag.how_many("cheezburger"))
    
    def test_cannot_remove_an_item_that_is_not_there(self):
        removed_count, item = self.bag.remove("Kaiser Soze")
        self.assertEqual(0, removed_count)
        self.assertIsNone(item)
        self.assertEqual(0, self.bag.how_many("Kaiser Soze"))

    def test_removed_items_behave_like_items_that_never_existed(self):
        self.bag.add(Item("smoke"))
        removed_count, item = self.bag.remove("smoke")
        self.assertEqual(1, removed_count)

        removed_count, item = self.bag.remove("smoke")
        self.assertEqual(0, removed_count)
        self.assertIsNone(item)
        self.assertEqual(0, self.bag.how_many("smoke"))
        self.assertEqual(0, self.bag.item_count())
        
    def test_remove_many_items_from_bag_at_once(self):
        self.bag.add_many(Item("blind mouse"), 5)
        removed_count, item = self.bag.remove_many("blind mouse", 3)
        self.assertEqual(3, removed_count)
        self.assertEqual(2, self.bag.how_many("blind mouse"))
        self.assertEqual("blind mouse", item.name)

    def test_remove_many_items_will_remove_only_as_many_as_exist(self):
        self.bag.add_many(Item("rhymes"), 5)
        removed_count, item = self.bag.remove_many("rhymes", 7)
        self.assertEqual(5, removed_count)
        self.assertEqual(0, self.bag.how_many("rhymes"))
        self.assertEqual("rhymes", item.name)
        self.assertTrue(self.bag.isEmpty())

    def test_adding_multiple_of_the_same_item_increases_item_count(self):
        butter = Item("butter")
        self.bag.add(butter)
        self.bag.add(butter)
        self.assertEqual(2, self.bag.item_count())
        self.bag.add(butter)
        self.assertEqual(3, self.bag.item_count())

    def test_can_remove_an_item(self):
        self.bag.add(Item("cheezburger"))
        removed_count, item = self.bag.remove("cheezburger")
        self.assertEqual(1, removed_count)
        self.assertEqual("cheezburger", item.name)
        self.assertIsInstance(item, Item)
        self.assertEqual(0, self.bag.how_many("cheezburger"))
    
    def test_cannot_remove_an_item_that_is_not_there(self):
        removed_count, item = self.bag.remove("Kaiser Soze")
        self.assertEqual(0, removed_count)
        self.assertIsNone(item)
        self.assertEqual(0, self.bag.how_many("Kaiser Soze"))

    def test_removed_items_behave_like_items_that_never_existed(self):
        self.bag.add(Item("smoke"))
        removed_count, item = self.bag.remove("smoke")
        self.assertEqual(1, removed_count)

        removed_count, item = self.bag.remove("smoke")
        self.assertEqual(0, removed_count)
        self.assertIsNone(item)
        self.assertEqual(0, self.bag.how_many("smoke"))
        self.assertEqual(0, self.bag.item_count())
        
    def test_remove_many_items_from_bag_at_once(self):
        self.bag.add_many(Item("blind mouse"), 5)
        removed_count, item = self.bag.remove_many("blind mouse", 3)
        self.assertEqual(3, removed_count)
        self.assertEqual(2, self.bag.how_many("blind mouse"))
        self.assertEqual("blind mouse", item.name)

    def test_remove_many_items_will_remove_only_as_many_as_exist(self):
        self.bag.add_many(Item("rhymes"), 5)
        removed_count, item = self.bag.remove_many("rhymes", 7)
        self.assertEqual(5, removed_count)
        self.assertEqual(0, self.bag.how_many("rhymes"))
        self.assertEqual("rhymes", item.name)


if __name__ == '__main__':
    unittest.main()
