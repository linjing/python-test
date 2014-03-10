import time

def consume_cal(weight, height, age):
  return 655.096 + 9.563 * weight + 1.85 * height - 4.676 * age


class name():
  def __init__(self, func):
    self.__name = "linjing"
    self.__func = func
  def __call__(self):
    print self.__name,
    return self.__func

def add_time(func):
  def wrap_arg(*arg):
    print "%s," % time.strftime("%Y%m%d"),
    func(*arg)
  return wrap_arg

def add_name(name):
  def wrap_fun(func):
    def wrap_arg(*arg):
      print "%s, " % name,
      func (*arg)
    return wrap_arg
  return wrap_fun


def show_bmi_info(func):
  def wrap(weight, height):
    t = func(weight, height)
    print "your bmi = %s," % t,
    if t > 27:
      print "too fat"
    elif t > 23.9:
      print "too heavy"
    elif t > 18.5:
      print "normal"
    else:
      print "too light"
  return wrap

@add_time
@add_name("linjing")
@show_bmi_info
def bmi(weigth, height):
  return 1.0 * weigth / (height ** 2)

w=86.9
h=1.72
a=28

bmi(w, h)
print consume_cal(w, h, a)

