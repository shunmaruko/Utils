from __future__ import annotations
from contextlib import contextmanager

import time

"""
Todo:
    * _str_to_type is under construction
"""

@contextmanager
def timer():
    """Measure time of function call 

    Examples:
        >>> def foo(bar: int):
        >>>     return bar 
        >>> with timer():
        >>>     foo(1)
        Elapsed: 1.082999999998946e-06

    """
    t = time.perf_counter()
    try :
        yield None 
    finally :
        print('Elapsed:', time.perf_counter() - t)


def check_argument_types(func, values: dict):
    """Check argument type of given function 
    Aimed for the helper functinon called in class method.

    Args:
        func: function object 
        values (dict): arguments to be checked  

    Examples:
        >>> def f(a: int):
        >>>     return a
        >>> check_argument_types(f, {'a': 10})

        >>> class TestClass:
        >>>     def __init__(self):
        >>>         pass 
        >>>     def test_method(self, a: int, b: float):
        >>>         check_argument_types(self.test_method, locals())
        >>> test = TestClass()
        >>> test.test_method(10, 2.0)  #OK! 
        >>> test.test_method(10, "2.0") # raise error 
        ValueError: local variable b of function test_method must be a type of float

    """
    def _str_to_type(annotation_type):
        """ convert string to type
        Args:
            anntation_type (str): name of type like "int", "float"  etc..  
        Returns: 
            <class "annotation_type"> object  
        """
        if annotation_type == "int":
            return int
        elif annotation_type == "float":
            return float
        else :
            RuntimeError("{} cannot be converted".format(annotation_type)) 
    for value_name, annotation_type in func.__annotations__.items():
        value = values[value_name]
        if not isinstance(value, _str_to_type(annotation_type)):
            raise ValueError("local variable {} of function {} must be a type of {}".format(value_name, func.__name__, annotation_type))

