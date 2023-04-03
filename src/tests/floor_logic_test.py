import unittest
from logic.floor_logic import create_floor

class TestCreate_floor(unittest.TestCase):
    def setUp(self):
        pass

    def test_min_floor(self):
        self.w = 1
        self.h = 1

        self.floor = create_floor(self.w, self.h)

        self.assertNotEqual(self.floor, '#')
    
    def test_small_room(self):
        self.w = 5
        self.h = 5

        self.floor = create_floor(self.w, self.h)

        self.assertNotEqual(self.floor, '#####\n#===#\n#=-=#\n#===#\n#####')