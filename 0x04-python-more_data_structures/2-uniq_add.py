#!/usr/bin/python3
def uniq_add(my_list=[]):
  """Adds all unique integers in a list (only once for each integer).

  Args:
    my_list: The list of integers.

  Returns:
    The sum of all unique integers in the list.
  """

  seen = set()
  sum = 0
  for value in my_list:
    if value not in seen:
      seen.add(value)
      sum += value

  return sum
