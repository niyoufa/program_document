from ctypes import *
class PyObject(Structure):
	_fields_ = [('refcnt',c_size_t),
		    ('typeid',c_void_p)]

class PyInt(PyObject):
	_fields_ = [("val",c_long)]

class PyFloat(PyObject):
	_fields_ = [("val",c_double)]