import unittest
from modules.items import Bag
from modules.items import Item

class InventoryBagAddAndLookTest(unittest.TestCase):
    def setUp(self):
        self.bag = Bag()

    def tearDown(self):
        self.bag = None

    def test_can_use_bag_to_hold_items_that_are_found(self):
        # Inara is curious to know if she is carrying any items. She checks her bag to see what is in her inventory
        self.assertIsNotNone(self.bag)

        # Her inventory bag is empty and contains no items
        self.assertTrue(self.bag.is_empty())
        self.assertEqual(self.bag.item_count(), 0)

        # Inara sees a pile of rocks nearby and lacking any other items decides to put them into her bag. She puts one rock into her bag.  Looking into her bag, it is no longer empty, she has one rock in it.
        rock = Item("rock")
        self.bag.add(rock)
        self.assertFalse(self.bag.is_empty())
        self.assertEqual(self.bag.item_count(), 1)

        # note perhaps this should be checking for look() rather than dump()
        seen = self.bag.look()
        self.assertIn("1 rock", seen)

        # She puts two more rocks into her bag. Looking into her bag, she sees that it now contains 3 rocks
        self.bag.add(rock)
        another_rock = Item("rock")
        self.bag.add(another_rock)
        self.assertEqual(self.bag.item_count(), 3)

        seen = self.bag.look()
        self.assertIn("3 rock", seen)

        # Inara, happy to have something in her bag, starts on her adventure.  Before long she stumbles on something in a dark shadow.  Picking it up she sees that it is a shiny dagger.  After putting it into her bag she checks her bag to ensure that it is safe inside.  She now has 3 rocks and a dagger in her bag.
        dagger = Item("dagger")
        self.bag.add(dagger)

        seen = self.bag.look()
        self.assertIn("1 dagger", seen)

class InventoryBagDumpTest(unittest.TestCase):
    def setUp(self):
        self.bag = Bag()

    def tearDown(self):
        self.bag = None
    # Items can be dumped into a pile and sorted through
    # This is a remnant of my inital version implementation of the InventoryBagAddAndLookTestCase which has since been converted to the look function.  Not sure if I should keep dump()

    def test_items_are_dumped_into_a_pile(self):
        rock = Item("rock")
        self.bag.add(rock)

        pile = self.bag.dump()
        item_list = pile.keys()
        self.assertEqual(len(item_list), 1)
        self.assertIn("rock", item_list)
        item = pile["rock"]
        self.assertEqual(item["name"], "rock")
        self.assertEqual(item["count"], 1)
if __name__ == '__main__':
    unittest.main(warnings='ignore')

