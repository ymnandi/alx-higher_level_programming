
/*
 * File: 103-python.c
 * Auth: Type Your Name Here
 */

#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_bytes - Prints info about Python bytes objects.
 * @p: A pointer to a PyObject bytes object.
 */
void print_python_bytes(PyObject *p)
{
  Py_ssize_t i, len, size;
  char *str;

  printf("[.] bytes object info\n");
  if (!PyBytes_Check(p))
    {
      printf("  [ERROR] Invalid Bytes Object\n");
      return;
    }

  size = ((PyVarObject *)p)->ob_size;
  str = ((PyBytesObject *)p)->ob_sval;
  len =  size + 1 > 10 ? 10 : size + 1;

  printf("  size: %ld\n", size);
  printf("  trying string: %s\n", str);
  printf("  first %ld bytes:", len);
  for (i = 0; i < len; i++)
    printf(" %02hhx", str[i]);
  printf("\n");
}

/**
 * print_python_list - Prints info about Python list objects.
 * @p: A pointer to a PyObject list object.
 */
void print_python_list(PyObject *p)
{
  Py_ssize_t i, size, alloc;
  PyObject *obj;

  size = ((PyVarObject *)p)->ob_size;
  alloc = ((PyListObject *)p)->allocated;

  printf("[*] Python list info\n");
  printf("[*] Size of the Python List = %ld\n", size);
  printf("[*] Allocated = %ld\n", alloc);

  for (i = 0; i < size; i++)
    {
      obj = ((PyListObject *)p)->ob_item[i];
      printf("Element %ld: %s\n", i, obj->ob_type->tp_name);
      if (PyBytes_Check(obj))
    print_python_bytes(obj);
    }
}

/**
 * print_python_float - Prints info about Python float objects.
 * @p: A pointer to a PyObject float object.
 */
void print_python_float(PyObject *p)
{
  char *str;
  double val;

  printf("[.] float object info\n");
  if (!PyFloat_Check(p))
    {
      printf("  [ERROR] Invalid Float Object\n");
      return;
    }

  val = ((PyFloatObject *)p)->ob_fval;
  str = PyOS_double_to_string(val, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
  printf("  value: %s\n", str);
  free(str);
}
