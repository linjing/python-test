def test(args):
    print("Hello ,I'm Decorator!")
    print("args:",args)

    def impl(func):
        print("Hello ,I'm impl!")
        def inter(*args,**kwargs):

            print("my name:%s",func.__name__)
            ret = func(*args,**kwargs)
            return ret
        return inter

    return impl 

@test("my_test")
def run(a):
    print("run start")
    print("run(%s)" % (a))
    print("run end")

run("xx")
run("xx")
