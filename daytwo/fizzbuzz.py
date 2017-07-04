def fizz_buzz(integer):
  if type(integer) != int:
    return 'invalid input'
  elif integer <= 0:
    return 'invalid input'
  elif (integer%3 == 0) and (integer%5 == 0):
    return 'fizzBuzz'
  elif integer%3 == 0:
    return 'fizz'
  elif integer%5 == 0:
    return 'buzz'
  else:
    return integer