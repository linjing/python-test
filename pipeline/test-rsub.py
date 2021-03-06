class Left1(int):
    """
        >>> print Left1(3) - Right(8)
        call Left1.__sub__: 3 8
        call Right.__rsub__: 8 3
        -5
    """
    def __sub__(self, other):
        print 'call Left1.__sub__:', self, other
        return NotImplemented
 
 
class Left2(int):
    """
        >>> print Left2(3) - Right(8)
        call Left2.__sub__: 3 8
        -5
    """
    def __sub__(self, other):
        print 'call Left2.__sub__:', self, other
        return int.__sub__(self, other)
 
 
class Right(int):
    def __rsub__(self, other):
        print 'call Right.__rsub__:', self, other
        return int.__rsub__(self, other)

l1 = Left1(3)
l2 = Left2(3)
r  = Right(8)
print l1 - r
print l2 - r
