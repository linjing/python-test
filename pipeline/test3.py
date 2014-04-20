class Pipe(object):
  def __init__(self, func):
    self.func = func
  def __ror__(self, other):
    def generator():
      for obj in other:
        if obj is not None:
          yield self.func(obj)
    return generator()

@Pipe
def even_filter(num):
  return num if num % 2 == 0 else None

@Pipe
def multiply_by_three(num):
  return num*3

@Pipe
def convert_to_string(num):
  return 'The Number: %s' % num

@Pipe
def echo(item):
  print item
  return item

def force(sqs):
  for item in sqs: pass

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = range(1,3) | even_filter
print x, dir(x)
force(range(1,3) | even_filter | echo)
force(nums | even_filter | multiply_by_three | convert_to_string | echo)


for item in [1,2,3] | even_filter:
  print item
