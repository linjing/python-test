#!/usr/bin/python

class RomanError(Exception): pass
class OutOfRangeError(RomanError): pass
class NotIntegerError(RomanError): pass
class InvalidRomanNumeralError(RomanError): pass


romanNumeralMap = (('M', 1000),
    ('CM', 900),
    ('D', 500),
    ('CD', 400),
    ('C', 100),
    ('XC', 90),
    ('L', 50),
    ('XL', 40),
    ('X', 10),
    ('IX', 9),
    ('V', 5),
    ('IV', 4),
    ('I', 1))

import types

def to_roman(n):
  ''' return 1~3999 roman number in upper case
  failed for input not a integer in [1~3999]
  '''
  if not (0 < n < 4000): raise OutOfRangeError, "%s" % n
  if type(n) != types.IntType: raise NotIntegerError

  result = ""
  for numeral, integer in romanNumeralMap:
    while n >= integer:
      result += numeral
      n -= integer

  return result


import re
romanNumeralPattern = '^M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)(IX|IV|V?I?I?I?)$'
compiledPattern = re.compile(romanNumeralPattern)

def from_roman(s):
  ''' return 1~3999 integer 
  failed for input not valid roman number in [1~3999] in upper case
  '''
  if not s: raise InvalidRomanNumeralError
  if not compiledPattern.search(str(s)): raise InvalidRomanNumeralError

  index = 0
  result = 0
  for numeral, integer in romanNumeralMap:
    while s[index:index+len(numeral)] == numeral:
      index += len(numeral)
      result += integer

  if index != len(s): raise InvalidRomanNumeralError
  return result
