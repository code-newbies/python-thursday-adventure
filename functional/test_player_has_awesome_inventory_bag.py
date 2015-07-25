import unittest
from modules.bag import Bag
from modules.item import Item

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

    def test_items_are_removed_from_bag(self):
        # Mary Poppins is summoned by the children to bring joy to their lives.  She is holding a bag.  It contains a hatrack, a carpet, two lollipops and 5 brooms.  It also contains medicine, a teaspoon and a few spoonfulls of sugar.
        self.bag.add(Item("hatrack"))
        self.bag.add(Item("carpet"))
        self.bag.add(Item("Thing 1"))
        self.bag.add(Item("Thing 2"))
        self.bag.add(Item("Cat"))
        self.bag.add(Item("Hat"))
        self.bag.add(Item("lollipop"))
        self.bag.add(Item("lollipop"))
        self.bag.add(Item("lollipop"))
        self.bag.add_many(Item("lollipop"), 5)
        self.bag.add(Item("medicine"))
        self.bag.add(Item("teaspoon"))
        self.bag.add_many(Item("spoonful of sugar"), 3)

        # Her bag contains at least 14 items.
        total_items = self.bag.item_count()
        self.assertTrue(total_items >= 14)

        # Mary enters the unhappy home with a messy room and tells the kids to tidy up.  The children don't want to tidy up so she starts searching through her bag.  She removes a hatrack but puts it back
        hatrack_count = self.bag.how_many("hatrack")
        self.bag.remove("hatrack")
        self.assertEqual(hatrack_count - 1, self.bag.how_many("hatrack"))
        self.bag.add(Item("hatrack"))
        self.assertEqual(hatrack_count, self.bag.how_many("hatrack"))

        # Mary then removes the medicine.
        med_count, medicine = self.bag.remove("medicine")
        self.assertEqual(med_count, 1)
        self.assertIsInstance(medicine, Item)
        self.assertEqual(medicine.name, "medicine")

        # She tries to remove two teaspoons but only has one. 
        # She removes the teaspoon
        teaspoon_count, teaspoon = self.bag.remove_many("teaspoon", 2)
        self.assertEqual(teaspoon_count, 1)
        self.assertEqual(self.bag.how_many("teaspoon"), 0)
        self.assertEqual(teaspoon.name, "teaspoon")

        # She removes one spoonful of sugar and begins to sing
        sugar_count, sugar = self.bag.remove("spoonful of sugar")
        self.assertEqual(1, sugar_count)

        # She removes another spoonful of sugar and continues to sing.
        sugar_count, sugar = self.bag.remove("spoonful of sugar")
        self.assertEqual(1, sugar_count)

        # She removes the third spoonful of sugar smiles to herself and takes her medicine. 
        sugar_count, sugar = self.bag.remove("spoonful of sugar")
        self.assertEqual(1, sugar_count)

        # Mary now has 5 less items in her bag
        new_total_items = self.bag.item_count()
        self.assertEqual(5, total_items - new_total_items)

        # She returns the medicine and spoon to her bag and with at least 12 items in her bag continues with her work
        self.bag.add(teaspoon)
        self.bag.add(medicine)
        self.assertTrue(self.bag.item_count() >= 12)

    def test_items_are_dumped_into_a_pile(self):

        # Items can be dumped into a pile and sorted through
        # This is a remnant of my inital version implementation of the InventoryBagAddAndLookTestCase which has since been converted to the look function.  Not sure if I should keep dump()
        # This may be useful in the future for saving the state of the bag
        rock = Item("rock")
        self.bag.add(rock)

        pile = self.bag.dump()
        item_list = pile.keys()
        self.assertEqual(len(item_list), 1)
        self.assertIn("rock", item_list)
        item = pile["rock"]
        self.assertEqual(item["name"], "rock")
        self.assertEqual(item["count"], 1)

#if __name__ == '__main__':
#    unittest.main(warnings='ignore')

