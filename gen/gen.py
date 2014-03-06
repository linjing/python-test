

rows = [1,4,10]
def cols1():
  yield 3
  yield 2

gen = ((i,j) for i in rows for j in cols1())
print gen

for p in gen:
  print p


l = [(i,j) for i in rows for j in cols1()]
print l


