from django.test import TestCase
from models import *

class TestQueue(TestCase):
  def test_choices(self):
    self.assertEquals(choices({}),[])
    self.assertEquals(
        choices({'a': 'alpha'}),
        [('a','alpha')])
    self.assertEquals(
        choices({'a': 'alpha', 'b': 'beta'}),
        [('a','alpha'),('b','beta')])
