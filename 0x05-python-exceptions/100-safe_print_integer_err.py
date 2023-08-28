#!/usr/bin/python3
def safe_print_integer_err(value):
  """
  Prints an integer.

  Args:
    value: The value to print.

  Returns:
    True if value has been correctly printed (it means the value is an integer)
    Otherwise, returns False and prints in stderr the error precede by Exception:
  """

  try:
    print("{:d}".format(value))
    return True
  except (TypeError, ValueError):
    print(f"Exception: {sys.exc_info()[0]}", file=sys.stderr)
    return False
