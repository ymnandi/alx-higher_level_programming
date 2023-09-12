#include "Python.h"

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: PyObject
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
  PyListObject *list;
  Py_ssize_t size, i;
  PyObject *object;

  list = (PyListObject *)p;
  size = list->ob_base.ob_size;
  printf("[*] Size of the Python List = %ld\n", size);
  printf("[*] Allocated = %ld\n", list->allocated);
  for (i = 0; i < size; i++)
    {
      object = list->ob_item[i];
      printf("Element %ld: %s\n", i, object->ob_type->tp_name);
    }
}
