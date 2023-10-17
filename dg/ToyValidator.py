import datetime


# validates the fields of a toy object
class ToyValidator:

  # runs the main validate logic, various fields in the object will be evaluated
  def validate(self, obj):
    errors = {}

    if not self.valid_len(obj.get('name'), 1, 50):
      errors['name'] = 'Field must be provided'

    if not self.valid_len(obj.get('model'), 1, 50):
      errors['model'] = 'Field must be provided'

    try:
      pieces = int(obj.get('pieces'))

      if pieces is None:
        errors['pieces'] = 'Must be a valid number'
      elif pieces < 0:
        errors['pieces'] = 'Must be a valid number'
    except Exception:
      # print('Unable to verify pieces field: {}'.format(ex))
      errors['pieces'] = 'Must be a valid number'

    try:
      purchase_year = int(obj.get('purchaseYear'))

      if purchase_year is None:
        errors['purchaseYear'] = 'Must be a valid number'
      elif purchase_year < 1990 or purchase_year > datetime.datetime.now().year:
        errors['purchaseYear'] = 'Must be a valid number'
    except Exception:
      errors['purchaseYear'] = 'Must be a valid number'

    return errors

  # validates the min and max length of a value
  @staticmethod
  def valid_len(value, min_value, max_value):
    if value is None:
      return False
    elif len(value) < min_value:
      return False
    elif len(value) > max_value:
      return False
    else:
      return True
