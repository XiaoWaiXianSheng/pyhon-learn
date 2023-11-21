# from my_model01 import test
# from my_model02 import test
#
# test(1, 2)


"""__main__变量"""
from my_model01 import test_a

from my_model02 import test

"""__all__变量"""
from my_model01 import *

test_a(1, 2)

from my_model01 import test_b

test_b(1, 2)
