from main.nieuwsbrief import Nieuwsbrief
import unittest

class TestNieuwsbrief(unittest.TestCase):
    
  def test_empty(self):
    nieuwsbrief = Nieuwsbrief()
    self.assertTrue(False)



if __name__ == '__main__':
    unittest.main()