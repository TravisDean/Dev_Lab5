# Travis Dean - tjd2qj
from helper import greeting
from other_rand import do_nothing
from random import do_something_weird

def run():
    do_nothing()
    greeting("Hello")
    do_something_weird()


if __name__=="__main__":
    run()
