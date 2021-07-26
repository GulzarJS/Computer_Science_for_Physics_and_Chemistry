# #First year programmer, Python
# def Factorial(x):
#     res = 1
#     for i in xrange(2, x + 1):
#         res *= i
#     return res
# print Factorial(6)
#
#
# #Lazy Python programmer
# def fact(x):
#     return x > 1 and x * fact(x - 1) or 1
# print fact(6)
#
#
# #Lazier Python programmer
# f = lambda x: x and x * f(x - 1) or 1
# print f(6)
#
#
# #Python expert programmer
# import operator as op
# import functional as f
# fact = lambda x: f.foldl(op.mul, 1, xrange(2, x + 1))
# print fact(6)
#
#
# #Python hacker
# import sys
# @tailcall
# def fact(x, acc=1):
#     if x: return fact(x.__sub__(1), acc.__mul__(x))
#     return acc
# sys.stdout.write(str(fact(6)) + '\n')

