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

if __name__ == '__main__':
    unittest.main()
