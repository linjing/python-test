#!/usr/bin/python

'''
try:
  __enter__()
  with_block()
finally:
  __exit__()
'''

class test_with:
  def __init__(self, i):
    self._i = i
  def __enter__(self):
    print "enter, ", id(self), type(self)
    return self._i
  def __exit__(self, *args):
    print "exit, ", id(self), type(self)
    not_reraise = False
    return  not_reraise # not re-raise

with test_with(9) as t:
  print t
  raise Exception('xx')

