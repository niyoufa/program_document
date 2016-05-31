#coding=utf-8
"""
python命名空间和作用域

"""

import os,sys,pdb
name_1 = "youfa"
name_2 = "xiaoyan"

def print_name(name1,name2):
	global name_1 
	name_1 = name1
	name_2 = name2

	print name_1
	print name_2

print_name("niyoufa","liuxiaoyan")
print name_1
print name_2

"""

>>> python_namespace.__builtins__
{'bytearray': <type 'bytearray'>, 'IndexError': <type 'exceptions.IndexError'>, 
'all': <built-in function all>, 
'help': Type help() for interactive help, or help(object) for help about object., 
'vars': <built-in function vars>,
'SyntaxError': <type 'exceptions.SyntaxError'>, 
'unicode': <type 'unicode'>, 
'UnicodeDecodeError': <type 'exceptions.UnicodeDecodeError'>, 
'memoryview': <type 'memoryview'>,
'isinstance': <built-in function isinstance>, 
'copyright': Copyright (c) 2001-2014 Python Software Foundation.
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved.,
'NameError': <type 'exceptions.NameError'>,
'BytesWarning': <type 'exceptions.BytesWarning'>, 
'dict': <type 'dict'>, 'input': <built-in function input>,
'oct': <built-in function oct>, 
'bin': <built-in function bin>, 
'SystemExit': <type 'exceptions.SystemExit'>, 
'StandardError': <type 'exceptions.StandardError'>, 
'format': <built-in function format>,
'repr': <built-in function repr>, 
'sorted': <built-in function sorted>, 
'False': False, 
'RuntimeWarning': <type 'exceptions.RuntimeWarning'>,
'list': <type 'list'>,
'iter': <built-in function iter>,
'reload': <built-in function reload>, 
'Warning': <type 'exceptions.Warning'>, 
'__package__': None,
'round': <built-in function round>, 
'dir': <built-in function dir>, 
'cmp': <built-in function cmp>,
'set': <type 'set'>,
'bytes': <type 'str'>, 
'reduce': <built-in function reduce>,
'intern': <built-in function intern>, 
'issubclass': <built-in function issubclass>, 
'Ellipsis': Ellipsis, 'EOFError': <type 'exceptions.EOFError'>,
'locals': <built-in function locals>,
'BufferError': <type 'exceptions.BufferError'>, 
'slice': <type 'slice'>,
'FloatingPointError': <type 'exceptions.FloatingPointError'>, 
'sum': <built-in function sum>,
'getattr': <built-in function getattr>,
'abs': <built-in function abs>,
'exit': Use exit() or Ctrl-D (i.e. EOF) to exit,
'print': <built-in function print>,
'True': True, 'FutureWarning': <type 'exceptions.FutureWarning'>, 
'ImportWarning': <type 'exceptions.ImportWarning'>, 
'None': None, 'hash': <built-in function hash>,
'ReferenceError': <type 'exceptions.ReferenceError'>,
'len': <built-in function len>, 'credits':     Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
for supporting Python development.  See www.python.org for more information., 
'frozenset': <type 'frozenset'>,
'__name__': '__builtin__', 
'ord': <built-in function ord>, 
'super': <type 'super'>, '_': None, 
'TypeError': <type 'exceptions.TypeError'>, 
'license': Type license() to see the full license text,
'KeyboardInterrupt': <type 'exceptions.KeyboardInterrupt'>, 
'UserWarning': <type 'exceptions.UserWarning'>, 
'filter': <built-in function filter>, 
'range': <built-in function range>,
'staticmethod': <type 'staticmethod'>, 
'SystemError': <type 'exceptions.SystemError'>, 
'BaseException': <type 'exceptions.BaseException'>, 
'pow': <built-in function pow>,
'RuntimeError': <type 'exceptions.RuntimeError'>,
'float': <type 'float'>, 'MemoryError': <type 'exceptions.MemoryError'>, 
'StopIteration': <type 'exceptions.StopIteration'>, 
'globals': <built-in function globals>,
'divmod': <built-in function divmod>, 
'enumerate': <type 'enumerate'>,
'apply': <built-in function apply>, 
'LookupError': <type 'exceptions.LookupError'>, 
'open': <built-in function open>, 
'quit': Use quit() or Ctrl-D (i.e. EOF) to exit,
'basestring': <type 'basestring'>,
'UnicodeError': <type 'exceptions.UnicodeError'>,
'zip': <built-in function zip>,
'hex': <built-in function hex>,
'long': <type 'long'>,
'next': <built-in function next>,
'ImportError': <type 'exceptions.ImportError'>,
'chr': <built-in function chr>, 
'xrange': <type 'xrange'>,
'type': <type 'type'>,
'__doc__': "Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices.", 
'Exception': <type 'exceptions.Exception'>,
'tuple': <type 'tuple'>,
'UnicodeTranslateError': <type 'exceptions.UnicodeTranslateError'>,
'reversed': <type 'reversed'>,
'UnicodeEncodeError': <type 'exceptions.UnicodeEncodeError'>, 
'IOError': <type 'exceptions.IOError'>,
'hasattr': <built-in function hasattr>, 
'delattr': <built-in function delattr>, 
'setattr': <built-in function setattr>, 
'raw_input': <built-in function raw_input>, 
'SyntaxWarning': <type 'exceptions.SyntaxWarning'>,
'compile': <built-in function compile>, 
'ArithmeticError': <type 'exceptions.ArithmeticError'>, 
'str': <type 'str'>,
'property': <type 'property'>, 
'GeneratorExit': <type 'exceptions.GeneratorExit'>, 
'int': <type 'int'>, 
'__import__': <built-in function __import__>, 
'KeyError': <type 'exceptions.KeyError'>, 
'coerce': <built-in function coerce>,
'PendingDeprecationWarning': <type 'exceptions.PendingDeprecationWarning'>, 
'file': <type 'file'>,
'EnvironmentError': <type 'exceptions.EnvironmentError'>,
'unichr': <built-in function unichr>, 
'id': <built-in function id>, 
'OSError': <type 'exceptions.OSError'>,
'DeprecationWarning': <type 'exceptions.DeprecationWarning'>, 
'min': <built-in function min>,
'UnicodeWarning': <type 'exceptions.UnicodeWarning'>, 
'execfile': <built-in function execfile>,
'any': <built-in function any>,
'complex': <type 'complex'>, 
'bool': <type 'bool'>,
'ValueError': <type 'exceptions.ValueError'>,
'NotImplemented': NotImplemented,
'map': <built-in function map>,
'buffer': <type 'buffer'>, 
'max': <built-in function max>,
'object': <type 'object'>,
'TabError': <type 'exceptions.TabError'>,
'callable': <built-in function callable>, 
'ZeroDivisionError': <type 'exceptions.ZeroDivisionError'>,
'eval': <built-in function eval>,
'__debug__': True,
'IndentationError': <type 'exceptions.IndentationError'>,
'AssertionError': <type 'exceptions.AssertionError'>,
'classmethod': <type 'classmethod'>, 
'UnboundLocalError': <type 'exceptions.UnboundLocalError'>, 
'NotImplementedError': <type 'exceptions.NotImplementedError'>,
'AttributeError': <type 'exceptions.AttributeError'>,
'OverflowError': <type 'exceptions.OverflowError'>}

"""