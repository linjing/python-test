#!/usr/bin/python

import unittest
import roman

class KnownValues(unittest.TestCase):
  knownValues = ((1, 'I'),
      (2, 'II'),
      (3, 'III'),
      (4, 'IV'),
      (5, 'V'),
      (6, 'VI'),
      (7, 'VII'),
      (8, 'VIII'),
      (9, 'IX'),
      (10, 'X'),
      (50, 'L'),
      (100, 'C'),
      (500, 'D'),
      (1000, 'M'),
      (31, 'XXXI'),
      (148, 'CXLVIII'),
      (294, 'CCXCIV'),
      (312, 'CCCXII'),
      (421, 'CDXXI'),
      (528, 'DXXVIII'),
      (621, 'DCXXI'),
      (782, 'DCCLXXXII'),
      (870, 'DCCCLXX'),
      (941, 'CMXLI'),
      (1043, 'MXLIII'),
      (1110, 'MCX'),
      (1226, 'MCCXXVI'),
      (1301, 'MCCCI'),
      (1485, 'MCDLXXXV'),
      (1509, 'MDIX'),
      (1607, 'MDCVII'),
      (1754, 'MDCCLIV'),
      (1832, 'MDCCCXXXII'),
      (1993, 'MCMXCIII'),
      (2074, 'MMLXXIV'),
      (2152, 'MMCLII'),
      (2212, 'MMCCXII'),
      (2343, 'MMCCCXLIII'),
      (2499, 'MMCDXCIX'),
      (2574, 'MMDLXXIV'),
      (2646, 'MMDCXLVI'),
      (2723, 'MMDCCXXIII'),
      (2892, 'MMDCCCXCII'),
      (2975, 'MMCMLXXV'),
      (3051, 'MMMLI'),
      (3185, 'MMMCLXXXV'),
      (3250, 'MMMCCL'),
      (3313, 'MMMCCCXIII'),
      (3408, 'MMMCDVIII'),
      (3501, 'MMMDI'),
      (3610, 'MMMDCX'),
      (3743, 'MMMDCCXLIII'),
      (3844, 'MMMDCCCXLIV'),
      (3888, 'MMMDCCCLXXXVIII'),
      (3940, 'MMMCMXL'),
      (3999, 'MMMCMXCIX'))
  def test_to_roman(self):
    for integer, numeral in self.knownValues:
      result = roman.to_roman(integer)
      self.assertEqual(result, numeral)
  def test_from_rmona(self):
    for integer, numeral in self.knownValues:
      result = roman.from_roman(numeral)
      self.assertEqual(result, integer)

class to_roman_badinput(unittest.TestCase):
  def test_toolarge(self):
    self.assertRaises(roman.OutOfRangeError, roman.to_roman, 4000)
  def test_zeor(self):
    self.assertRaises(roman.OutOfRangeError, roman.to_roman, 0)

  def testNegative(self):
    self.assertRaises(roman.OutOfRangeError, roman.to_roman, -1)
  def testNonInteger(self):
    self.assertRaises(roman.NotIntegerError, roman.to_roman, 0.5)

class from_roman_badinput(unittest.TestCase):
  def testTooManyRepeatedNumerals(self):
    for s in ('MMMM', 'DD', 'CCCC', 'LL', 'XXXX', 'VV', 'IIII'):
      self.assertRaises(roman.InvalidRomanNumeralError, roman.from_roman, s)
  def testRepeatedPairs(self):
    for s in ('CMCM', 'CDCD', 'XCXC', 'XLXL', 'IXIX', 'IVIV'):
      self.assertRaises(roman.InvalidRomanNumeralError, roman.from_roman, s)
  def testMalformedAntecedent(self):
    for s in ('IIMXCC', 'VX', 'DCM', 'CMM', 'IXIV',
        'MCMC', 'XCX', 'IVI', 'LM', 'LD', 'LC'):
      self.assertRaises(roman.InvalidRomanNumeralError, roman.from_roman, s)

class SanityCheck(unittest.TestCase):
  def testSanity(self):
    for integer in range(1, 4000):
      numeral = roman.to_roman(integer)
      result = roman.from_roman(numeral)
      self.assertEqual(integer, result)

class CaseCheck(unittest.TestCase):
  def testto_romanCase(self):
    for integer in range(1, 4000):
      numeral = roman.to_roman(integer)
      self.assertEqual(numeral, numeral.upper())
  def testfrom_romanCase(self):
    for integer in range(1, 4000):
      numeral = roman.to_roman(integer)
      roman.from_roman(numeral.upper())
      self.assertRaises(roman.InvalidRomanNumeralError,
          roman.from_roman, numeral.lower())

if __name__ == "__main__":
  unittest.main()


