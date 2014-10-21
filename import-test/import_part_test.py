#config
use_module_name = "m_b"

print "use __import__"
m = __import__(use_module_name, globals(), locals(),['f1', 'f2'])
print dir(m)
print m.f1(2,1)
