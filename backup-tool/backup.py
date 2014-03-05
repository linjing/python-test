#!/usr/bin/python

import os
import time

import config

target = config.to_dir + os.sep + time.strftime("%Y%m%d-%H%M%S") + ".zip"

zip_cmd = "zip -qr '%s' %s " % (target, " ".join(config.from_dirs))

if os.system(zip_cmd) == 0:
  print 'Successful backup to', target
else:
  print 'Backup FAILED'
