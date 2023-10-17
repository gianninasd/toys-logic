from dg.ToyValidator import ToyValidator

import unittest


# unit tests for the ToyValidator class
class TestToyValidator(unittest.TestCase):

  val = ToyValidator()

  def test_AllGood(self):
    obj = {
      'name': 'Rick Hunter',
      'model': 'Technic',
      'pieces': '55',
      'purchaseYear': '2020'
    }

    errors = self.val.validate(obj)
    self.assertEqual(len(errors), 0)

  def test_MissingName(self):
    obj = {}

    errors = self.val.validate(obj)
    self.assertEqual(errors['name'], 'Field must be provided')

  def test_EmptyPieces(self):
    obj = {
      'name': 'Rick Hunter',
      'model': 'Technic',
      'pieces': ' ',
      'purchaseYear': '2020'
    }

    errors = self.val.validate(obj)
    self.assertEqual(errors['pieces'], 'Must be a valid number')

  def test_NonNumericPieces(self):
    obj = {
      'name': 'Rick Hunter',
      'model': 'Technic',
      'pieces': 'abc',
      'purchaseYear': '2020'
    }

    errors = self.val.validate(obj)
    self.assertEqual(errors['pieces'], 'Must be a valid number')

  def test_BadYear(self):
    obj = {
      'name': 'Rick Hunter',
      'model': 'Technic',
      'pieces': 'abc',
      'purchaseYear': '1981'
    }

    errors = self.val.validate(obj)
    self.assertEqual(errors['pieces'], 'Must be a valid number')


if __name__ == '__main__':
  unittest.main()
