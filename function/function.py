#!/usr/bin/python

def powersum(power, *args, **kw):
  total = 0
  for i in args:
    total += pow(power, i)
  if kw.has_key("msg"):
    print kw["msg"]
  return total

print powersum (1,2,3, msg="powersum (1,2,3)")
print powersum (2,3,4)

