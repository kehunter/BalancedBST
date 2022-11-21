class Fraction:

  def __init__(self, numerator, denominator):
    if denominator == 0:
      raise ZeroDivisionError
    self.__n = numerator
    self.__d = denominator
    self.__reduce()

  @staticmethod
  def gcd(n, d):
    while d != 0:
      t = d
      d = n % d
      n = t
    return n

  def __reduce(self):
    if self.__n < 0 and self.__d < 0:
      self.__n = self.__n * -1
      self.__d = self.__d * -1

    divisor = Fraction.gcd(self.__n, self.__d)
    self.__n = self.__n // divisor
    self.__d = self.__d // divisor

  def __add__(self, addend):
    num = self.__n * addend.__d + self.__d * addend.__n
    den = self.__d * addend.__d
    return Fraction(num, den)

  def __sub__(self, subtrahend):
    num = self.__n * subtrahend.__d - self.__d * subtrahend.__n
    den = self.__d * subtrahend.__d
    return Fraction(num, den)

  def __mul__(self, multiplicand):
    num = self.__n * multiplicand.__n
    den = self.__d * multiplicand.__d
    return Fraction(num, den)

  def __truediv__(self, divisor):
    if divisor.__n == 0:
      raise ZeroDivisionError
    num = self.__n * divisor.__d
    den = self.__d * divisor.__n
    return Fraction(num, den)

  def __lt__(self, other):
    first = self.to_float()
    second = other.to_float()
    if first < second:
      return True
    else:
      return False

  def __gt__(self, other):
    first = self.to_float()
    second = other.to_float()
    if first > second:
      return True
    else:
      return False

  def __eq__(self, other):
    if (self.__n == other.__n) and (self.__d == other.__d):
      return True
    else:
      return False

  def to_float(self):
    #this is safe because we don't allow a
    #zero denominator
    return self.__n / self.__d

  def __str__(self):
    return str(self.__n) + '/' + str(self.__d)

  def __repr__(self):
    return str(self)

if __name__ == '__main__':
  #TODO create a bunch of fraction objects and store them in an array.
  #Then insert each item from the array into a balanced BST.
  #Then get the in-order array representation of the BST using
  #the new to_list() method, which you must implement.
  #print the original and in-order traversal arrays to show that
  #the fractions have been sorted.
  from Binary_Search_Tree import Binary_Search_Tree
  array = [Fraction(2,3), Fraction(5,8), Fraction(27,5), Fraction(7,6), \
  Fraction(8,17),Fraction(9,11), Fraction(66,33), Fraction(3,114), Fraction(7,66),\
  Fraction(5,9), Fraction(1,8), Fraction(2,5), Fraction(0,7),Fraction(9,18), Fraction(88,89),\
  Fraction(-4,7), Fraction(-9,10)]
  sort_tree = Binary_Search_Tree()
  for frac in array:
    sort_tree.insert_element(frac)
  print('Original array:')
  print(array)
  print()
  print('Sorted array:')
  print(sort_tree.to_list())
