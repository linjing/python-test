#!/usr/bin/python2.7

class Pipe(object):
    def __init__(self, fn):
        self.fn = fn
    def __ror__(self, other):
        def generator():
            for obj in other:
                if obj is not None:
                    yield self.fn(obj)
        return generator()

def inc(x):
    def incx(y):
        print x # 2
        print y # 3
        return x+y
    return incx

inc2 = inc(2)
print inc2(3)

def too_small(bench):
    def too_small_than(input):
        return input < bench
    return too_small_than

lt = too_small(6)
print lt(4)

def too_small_x(bench):
    @Pipe
    def too_small_than_x(input):
        return input < bench
    return too_small_than_x

def force(xs):
    for item in xs:
        pass
@Pipe
def echo(x):
    print x
    return x
nums = [1,2,3,4, 5, 6]
too_small_than_x4 = too_small_x(4)
print 'xxxxxxxxxxxxxxxxxxxx'
force(nums | too_small_than_x4 | echo)

def xxyy():
    for i in range(5):
        yield i
t = xxyy()
for i in t:
    print "x,", i

y = [x for x in xxyy()]
print y
