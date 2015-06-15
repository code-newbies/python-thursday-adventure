import unittest
from modules.items import Bag
from modules.items import Item

class InventoryBagTest(unittest.TestCase):
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
        
        pile = self.bag.dump()
        item_list = pile.keys()
        self.assertEqual(len(item_list), 1)
        self.assertIn("rock", item_list)
        item = pile["rock"]
        self.assertEqual(item["name"], "rock")
        self.assertEqual(item["count"], 1)

        # She puts two more rocks into her bag
        self.fail('Finish the test')

        # Looking into her bag, she sees that it now contains 3 rocks

        # Inara, happy to have something in her bag, starts on her adventure.  Before long she stumbles on something in a dark shadow.  Picking it up she sees that it is a shiny dagger.  After putting it into her bag she checks her bag to ensure that it is safe inside.  She now has 3 rocks and a dagger in her bag.

if __name__ == '__main__':
    unittest.main(warnings='ignore')

