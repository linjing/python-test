#config
use_module_name = "m_b"

print "use __import__"
m = __import__(use_module_name)
print dir(m)
print m.f1(2,1)


print "use importlib.import_module"
import importlib
m = importlib.import_module(use_module_name)
print dir(m)
print m.f1(2,1)
