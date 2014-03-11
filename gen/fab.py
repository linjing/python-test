#!/usr/bin/python

def fab(max):
  n, a, b = 0, 0, 1
  l = []
  while n < max:
    l.append(b)
    a, b = b, a + b
    n = n + 1
  return l

class Fab(object):
  def __init__(self, max):
    self.max = max
    self.n, self.a, self.b = 0, 0, 1

  def __iter__(self):
    return self

  def next(self):
    if self.n < self.max:
      r = self.b
      self.a, self.b = self.b, self.a + self.b
      self.n += 1
      return r
    raise StopIteration()

if __name__ == '__main__':
  print fab(5)
  for i in Fab (10):
    print i
