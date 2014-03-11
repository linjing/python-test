#!/usr/bin/python

def fab(max):
  n, a, b = 0, 0, 1
  l = []
  while n < max:
    l.append(b)
    a, b = b, a + b
    n = n + 1
  return l



if __name__ == '__main__':
  print fab(5)
