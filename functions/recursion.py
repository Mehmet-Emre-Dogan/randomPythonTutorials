from time import sleep

def foo():
    print("foo")
    sleep(0.5)
    bar()

def bar():
    print("bar")
    sleep(0.5)
    foo()

foo()
