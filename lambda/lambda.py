
def make_repeater(n):
  return lambda s : s*n

twice = make_repeater(2)

print twice("xx")
print twice(9)

y = "xx"
a = lambda y : y * 2
print a(9)


b = lambda x, y : x * y * 2

print b(2, 9)
