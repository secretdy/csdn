# 零基础掌握 Python 入门到实战
print('hello world')
# hello world
# >>> 3
# 3
# >>> a = 3
# >>> a
# 3
# >>> b = 4
# >>> b
# python特有的变量值交换
# >>> a, b = b, a
# >>> a
# 4
# >>> b
# 3
# >>> my_book = "learn python with Laoqi"
# >>> my_book
# 'learn python with Laoqi'
# >>> 2.5
# 2.5

a = 3
type(a)
# <class 'int'>
type(2.5)
# <class 'float'>
int(3.14)
# 3
float(3)
# 3.0
id(3)
# 8791276548416
id(3.0)
# 5014512
# >>> 5 % 2
# 1
# >>> 5 // 2
# 2
divmod(3, 2)
# (1, 1)
help(id)
# Help on built-in function id in module builtins:
#
# id(obj, /)
#     Return the identity of an object.
#
#     This is guaranteed to be unique among simultaneously existing objects.
#     (CPython uses the object's memory address.)
#
# >>> 0.1 + 0.4
# 0.5
# >>> 0.1 + 0.2
# 0.30000000000000004
# >>> round(0.2 + 0.3)
# 0
# >>> round(0.2 + 0.3, 2)
# 0.5
# >>> a = 1.23e3
# >>> a
# 1230.0
import math
math_list = dir(math)
print(math_list)
# ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh'
# , 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh',
# 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fm
# od', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'is
# inf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan'
# , 'pi', 'pow', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'ta
# u', 'trunc']
b = math.pi
print(b)
# 3.141592653589793
c = math.pow(2,3)
print(c)
# 8.0
# >>> help(math.pow)
# Help on built-in function pow in module math:
#
# pow(x, y, /)
#     Return x**y (x to the power of y).
#
import decimal
a = decimal.Decimal('0.1')
b = decimal.Decimal('0.2')
print(a + b)
# Decimal('0.3')
