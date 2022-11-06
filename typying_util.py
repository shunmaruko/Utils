from __future__ import annotations
from contextlib import contextmanager
import time

@contextmanager
def timer():
    t = time.perf_counter()
    yield None
    print('Elapsed:', time.perf_counter() - t)

def _str_to_type(annotation_type):
    # TODO better implimention
    if annotation_type == "int":
        return int
    elif annotation_type == "float":
        return float
    else :
        RuntimeError("{} cannot be converted".format(annotation_type)) 

def check_argument_types(func, values: dict):
    for value_name, annotation_type in func.__annotations__.items():
        value = values[value_name]
        if not isinstance(value, _str_to_type(annotation_type)):
            raise ValueError("local variable {} of function {} must be a type of {}".format(value_name, func.__name__, annotation_type))

if __name__ == "__main__":
    def f(a: int):
        return a
    check_argument_types(f, {'a': 10})

    class TestClass:

        def __init__(self):
            pass 

        def test_method(self, a: int, b: float):
            check_argument_types(self.test_method, locals())

    test = TestClass()
    test.test_method(10, 2.0)
    test.test_method(10, "2.0")
