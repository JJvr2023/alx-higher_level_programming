void print_python_list(PyObject *p) {
  if (!PyList_Check(p)) {
    printf("Error: p is not a valid PyListObject\n");
    return;
  }

  printf("Python list: \n");
  int i;
  for (i = 0; i < PyList_Size(p); i++) {
    PyObject *item = PyList_GetItem(p, i);
    print_python_object(item);
  }
}

void print_python_bytes(PyObject *p) {
  if (!PyBytes_Check(p)) {
    printf("Error: p is not a valid PyBytesObject\n");
    return;
  }

  printf("Python bytes: \n");
  size_t len = PyBytes_GET_SIZE(p);
  if (len > 10) {
    len = 10;
  }
  printf("  size: %zu\n", len);
  printf("  first %zu bytes: ", len);
  for (size_t i = 0; i < len; i++) {
    printf("%c", PyBytes_AS_STRING(p)[i]);
  }
  printf("\n");
}

void print_python_float(PyObject *p) {
  if (!PyFloat_Check(p)) {
    printf("Error: p is not a valid PyFloatObject\n");
    return;
  }

  printf("Python float: \n");
  double value = PyFloat_AS_DOUBLE(p);
  printf("  value: %g\n", value);
}
