import os
import sys
import unittest
import string
import random

from bling.ring import Sing

class MyTest(unittest.TestCase):

   def test_anything(self):
       s = Sing()
       s.f()
       assert True

if __name__ == '__main__':
    unittest.main()
