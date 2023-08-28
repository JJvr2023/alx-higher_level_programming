#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
  """
  Divides element by element 2 lists.

  Args:
    my_list_1: The first list.
    my_list_2: The second list.
    list_length: The length of the new list.

  Returns:
    A new list (length = list_length) with all divisions.
  """

  new_list = []
  for i in range(list_length):
    try:
      a = my_list_1[i]
      b = my_list_2[i]
      if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        new_list.append(a / b)
      else:
        new_list.append(0)
    except (TypeError, ZeroDivisionError):
      print("wrong type")
      new_list.append(0)
    except IndexError:
      print("out of range")
      new_list.append(0)
  return new_list
