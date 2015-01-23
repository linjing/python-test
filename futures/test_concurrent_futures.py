#!/usr/bin/env python2.6

import concurrent.futures
import threading
import Queue

import time
import random
import sys
def debug(s):
    print >> sys.stderr, (str(s)+"\n")

class Task():
    def __init__(self, sleep):
        self.sleep = sleep
        self.record = "\tTask %s create: %s \n" % (id(self), time.asctime())

    def run(self):
        if self.sleep > 3:
            time.sleep(self.sleep)
            raise Exception("%s\tTask %s cost too long: %s\n" %
                            (self.record, id(self), time.asctime()))
        self.record += "\t Task %s run: %s \n" % (id(self), time.asctime())
        time.sleep(self.sleep)
        self.record += "\t Task %s done: %s \n" % (id(self), time.asctime())

        return self.record 

class RunBg(threading.Thread):
    def __init__(self, queue, concurrent_number = 10):
        threading.Thread.__init__(self)
        self.queue = queue
        self.concurrent_number = concurrent_number

    def run(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers = self.concurrent_number) as executor:
            running_tasks = {}
            
            while True:
                this_batch_has_new_task = self.add_tasks(executor, running_tasks)
                self.deal_tasks(running_tasks)
                if not this_batch_has_new_task and len(running_tasks) == 0:
                    time.sleep(1)

    def add_tasks(self, executor, running_tasks):
        new_task = False
        while len(running_tasks) < self.concurrent_number:
            try:
                task = self.queue.get_nowait()
                running_tasks[executor.submit(task.run)] = task
                new_task = True
            except Queue.Empty:
                break
        return new_task

    def deal_tasks(self, running_tasks):
        if len(running_tasks) > 0:
            try:
                for f in concurrent.futures.as_completed(running_tasks, timeout = 1):
                    try:
                        res = f.result ()
                        debug (res)
                    except Exception, ex:
                        debug (ex)
                    finally:
                        running_tasks.pop(f)
                    if len(running_tasks) == 0:
                        break
            except concurrent.futures._base.TimeoutError, ex:
                debug ("Timeout")

def test():
    task_queue = Queue.Queue()
    bg_thread = RunBg(task_queue)
    bg_thread.start()

    for i in range(50):
        task = Task(int(random.random() * i) % 5)
        task_queue.put(task)

    time.sleep(100)

if __name__ == "__main__":
    test()
