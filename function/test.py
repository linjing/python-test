#!/usr/bin/python

from time import ctime, sleep

def ts_fun(func):
  def wrapped_fun(b):
    print '[%s] %s() called %s' % (ctime(), func.__name__, b)
    return func(b)
  return wrapped_fun


@ts_fun
def foo(a):
  print '[%s] enter foo %s' % (ctime(), a)
  print '[%s] exit foo %s' % (ctime(), a)

foo(1) # called ts_fun(foo)(1)
sleep(4)
