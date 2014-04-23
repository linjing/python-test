#!/usr/bin/python

import os
import time
try:
    import json
except ImportError:
    import simplejson as json

class Pipe(object):
    def __init__(self, fn):
        self.fn = fn
    def __ror__(self, other):
        def generator():
            for obj in other:
                if obj is not None:
                    yield self.fn(obj)
        return generator()

def merged_and_alive_base(base_id, alive_base_ids):
    if alive_base_ids.count(base_id) != 0:
        return True
    return False

def with_merged_from_base_still_alive(alive_base_ids):
    def __base_with(base):
        for base_id in base.merged_from_base_ids:
            if merged_and_alive_base(base_id, alive_base_ids):
                return True
        return False

    @Pipe
    def find(base):
        return base if __base_with(base) else None

    @Pipe
    def ignore(base):
        return base if not __base_with(base) else None

    return {"finder" : find, "ignorer" : ignore}

def ignore_source_base(source_bases):
    @Pipe
    def filt(base):
        return base if source_bases.count(base.id) == 0 else None
    return filt


def force(xs):
    return [item for item in xs]

@Pipe
def echo(x):
    print "test, ", x
    return x
