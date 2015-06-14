import unittest
from modules.items import Bag

class BagTest(unittest.TestCase):
    def setUp(self):
        self.bag = Bag()

    def tearDown(self):
        self.bag = None

    def test_can_check_bag_to_see_if_empty(self):
        self.assertTrue(self.bag.isEmpty())


if __name__ == '__main__':
    unittest.main()
