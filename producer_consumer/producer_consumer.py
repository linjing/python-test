#!/bin/env python

import Queue
import time
import threading

class Task (object):
    def __init__ (self):
        self.name = "task"

    # need deal function to deal with task, and save result
    def deal (self):
        print self.name

class Consumer (threading.Thread):
    def __init__ (self, queue, daemon):
        threading.Thread.__init__ (self)
        self._queue = queue
        self.daemon = daemon

    def run (self):
        while True:
            try:
                if self.daemon:
                    task = self._queue.get ()
                else:
                    task = self._queue.get_nowait ()
                task.deal ()
                self._queue.task_done ()
            except Queue.Empty:
                #print "all task is done"
                break

class Producer (object):
    def __init__ (self, queue, tasks = []):
        self._queue = queue
        for task in tasks:
            self._queue.put (task)

    def put (self, task):
        self._queue.put (task)

# test code below
class SleepTask (Task):
    def __init__ (self, n):
        Task.__init__ (self)
        self.name = "sleep task"
        self.n = n
    def deal (self):
        print "start: ", self.name, self.n
        time.sleep (self.n/10 + 1)
        print "end: ", self.name, self.n

if __name__ == "__main__":
    tasks_data = range (20)
    tasks = []
    for td in tasks_data:
        tasks.append (SleepTask (td))

    task_queue = Queue.Queue ()
    producer = Producer (task_queue, tasks)
    consumers = [ Consumer (task_queue, False) for i in range (5) ]
    for c in consumers:
        c.start ()
    task_queue.join ()
