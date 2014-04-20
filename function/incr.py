
def inc(x):
  def incx(y):
    return x+y
  return incx

inc2 = inc(2)
print inc2
print dir (inc2)
print inc2(5)
print inc2(6)
print inc2(7)

def inc_2(x,y):
  def inc_xy(z):
    return x+y+z
  return inc_xy

inc_xxx = inc_2(3,3)
print inc_xxx
print dir(inc_xxx)
print inc_xxx(3)
print inc_xxx(4)
print inc_xxx(5)
