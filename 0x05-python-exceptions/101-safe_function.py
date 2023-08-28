#!/usr/bin/python3
def safe_function(fct, *args):
  """
  Executes a function safely.

  Args:
    fct: The function to execute.
    *args: The arguments to pass to the function.

  Returns:
    The result of the function,
    Otherwise, returns None if something happens during the function and prints in stderr the error precede by Exception:
  """

  try:
    return fct(*args)
  except Exception as e:
    print(f"Exception: {e}", file=sys.stderr)
    return None
