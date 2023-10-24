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
		Py_ssize_t size, allocated, i;
	PyObject *item;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
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
	Py_ssize_t size, i;
	char *str;

	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	printf("  first 10 bytes: ");
	for (i = 0; i < size && i < 10; i++)
	{
		printf("%02x ", (unsigned char)str[i]);
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
		fprintf(stderr, "[ERROR] Invalid Float Object\n");
		return;
	}

	printf("[.] float object info\n");
	printf("  value: %lf\n", PyFloat_AsDouble(p));
}

int main(void)
{
	PyObject *list, *bytes, *float_obj;

	Py_Initialize();

	list = PyList_New(0);
	bytes = PyBytes_FromString("Hello");
	float_obj = PyFloat_FromDouble(3.14);

	print_python_list(list);
	print_python_bytes(bytes);
	print_python_float(float_obj);

	Py_DECREF(list);
	Py_DECREF(bytes);
	Py_DECREF(float_obj);

	Py_Finalize();

	return (0);
}
