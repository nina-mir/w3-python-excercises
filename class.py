class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

print(MyClass.__doc__)



class prob_1:
    """ 
    1. Write a Python class to convert an integer to a roman numeral.
    source: https://www.oreilly.com/library/view/python-cookbook/0596001673/ch03s24.html 
    """

    ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')

    def __init__(self, int_num):
        self.int = int_num
        self.roman = []    # creates a new empty list for each dog

    def convert(self):
        """ Convert an integer to a Roman numeral. """

        # if not isinstance(self.int, type(1)):
        #     raise TypeError, "expected integer, got %s" % type(self.int)
        # if not 0 < self.int < 4000:
        #     raise ValueError, "Argument must be between 1 and 3999"
        ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
        nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
        for i in range(len(ints)):
            count = int(self.int / ints[i])
            self.roman.append(nums[i] * count)
            self.int -= ints[i] * count
        return ''.join(self.roman)


x = prob_1(10)
print(x.convert())
print(x.__doc__)