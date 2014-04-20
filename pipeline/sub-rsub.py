class test(object):
    def __rsub__(self,  other):
        print "yyy"
        return other if other != 1 else 666 
 
    def __sub__(self,  other):
        print "xxx"
        return other
 
t1 = test()
t2 = test()
t1-t2
