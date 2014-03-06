#!/usr/bin/python

import cPickle as pickle

shoplist = ['apple', 'mango', 'carrot']

f = file("test", "w")
pickle.dump(shoplist, f)
shoplist = ['apple', 'mango', 'carrot', "bb"]
pickle.dump(shoplist, f)
pickle.dump(shoplist, f)
f.close()

del shoplist

f = file("test", "r")
xxx = pickle.load(f)
yyy = pickle.load(f)
f.close()

print xxx
print yyy

