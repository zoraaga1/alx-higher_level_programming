#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints information about a Python list object.
 * @p: A pointer to the Python list object.
 *
 * It also lists the types of elements within the list.
 */
void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);

		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - Prints information about a Python bytes object.
 * @p: A pointer to the Python bytes object.
 *
 */
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);
	Py_ssize_t i;

	printf("[.] Size: %ld\n", size);
	printf("[.] trying string: %s\n", PyBytes_AsString(p));
	printf("[ERROR] Invalid Bytes Object\n");

	if (size > 10)
	{
		size = 10;
	}

	printf("[.]\n[.]\n[.] first %ld bytes: ", size);

	for (i = 0; i < size; i++)
	{
		printf("%02x", (unsigned char)PyBytes_AsString(p)[i]);

		if (i < size - 1)
			printf(" ");
	}

	printf("\n");
}

/**
 * print_python_float - Prints information about a Python float object.
 * @p: A pointer to the Python float object.
 *
 */
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		printf("[ERROR] Invalid Float Object\n");
		return;
	}

	printf("[.] float object info\n");
	printf("[.] value: %f\n", ((PyFloatObject *)p)->ob_fval);
}
