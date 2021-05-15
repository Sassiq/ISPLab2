bool_variable = True
int_variable = 1234
float_variable = 12.34
string = "SomeLetters"
lst = [0, 23.4, "word", False]
dct = {"Word": 111, "Word2": 222}


def func_simple(a, b):
    return a + b


def func_with_default(a=9, b=8):
    return a - b


def func_recursive(n):
    if n > 0:
        return func_recursive(n - 1)
    else:
        return 1


class Class1:
    string1 = "aa"

    def class_method(self):
        print(self.string1)
