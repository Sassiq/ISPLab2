import unittest
from fabric import Fabric
import test_objects as test

serializer = Fabric.create_serializer("Json")


class TestSerializer(unittest.TestCase):
    def test_bool(self):
        self.assertEqual(test.bool_variable, serializer.loads(serializer.dumps(test.bool_variable)))

    def test_int(self):
        self.assertEqual(test.int_variable, serializer.loads(serializer.dumps(test.int_variable)))

    def test_float(self):
        self.assertEqual(test.float_variable, serializer.loads(serializer.dumps(test.float_variable)))

    def test_string(self):
        self.assertEqual(test.string, serializer.loads(serializer.dumps(test.string)))

    def test_list(self):
        self.assertEqual(test.lst, serializer.loads(serializer.dumps(test.lst)))

    def test_dict(self):
        self.assertEqual(test.dct, serializer.loads(serializer.dumps(test.dct)))

    def test_simple_function(self):
        self.assertEqual(test.func_simple.__code__, serializer.loads(serializer.dumps(test.func_simple.__code__)))
        self.assertEqual(test.func_simple(1, 2), serializer.loads(serializer.dumps(test.func_simple(1, 2))))

    def test_recursive_function(self):
        self.assertEqual(test.func_recursive.__code__, serializer.loads(serializer.dumps(test.func_recursive.__code__)))
        self.assertEqual(test.func_recursive(3), serializer.loads(serializer.dumps(test.func_recursive(3))))

    def test_function_with_defaults(self):
        self.assertEqual(test.func_with_default.__code__,
                         serializer.loads(serializer.dumps(test.func_with_default.__code__)))
        self.assertEqual(test.func_with_default(),
                         serializer.loads(serializer.dumps(test.func_with_default())))

    def test_class_method(self):
        self.assertEqual(test.Class1.class_method.__code__,
                         serializer.loads(serializer.dumps(test.Class1.class_method.__code__)))
