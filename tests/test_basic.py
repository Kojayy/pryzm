import os
import sys
absp = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, absp)

import pryzm

def test_basic_foreground():
    pz = pryzm.Pryzm()

    assert pz.red("test")    == '\x1b[31mtest\x1b[0m'
    assert pz.cyan("test")   == '\x1b[36mtest\x1b[0m'
    assert pz.blue("test")   == '\x1b[34mtest\x1b[0m'

def test_basic_background():
    pz = pryzm.Pryzm()

    assert pz.RED("test")   == '\x1b[41mtest\x1b[0m'

def test_basic_fore_back_combination():
    pz = pryzm.Pryzm()

    assert pz.red().RED("test") == '\x1b[31;41mtest\x1b[0m'

def test_create_function():
    pz = pryzm.Pryzm()

    both_red = pz.red().RED
    assert both_red("test") == '\x1b[31;41mtest\x1b[0m'

def test_multiple_arguments():
    pz = pryzm.Pryzm()

    blue = pz.blue
    assert blue("This is", "also blue") == '\x1b[34mThis is also blue\x1b[0m'

def test_multiple_arguments_in_class():
    pz = pryzm.Pryzm()

    assert pz.blue("This is", "also blue") == '\x1b[34mThis is also blue\x1b[0m'

def test_composable_if_not_printing():
    pz = pryzm.Pryzm()

    blue = pz.blue
    red = pz.red

    assert blue("BLUE")+" "+red("DEMON") == '\x1b[34mBLUE\x1b[0m \x1b[31mDEMON\x1b[0m'

def test_convert_to_string():
    pz = pryzm.Pryzm(echo=True)
    blue = pz.blue

    assert pz.blue("This is", 1, "also blue") == '\x1b[34mThis is 1 also blue\x1b[0m'
    assert pz.blue("This is", {'key': 'val'}, "also blue") == '\x1b[34mThis is {\'key\': \'val\'} also blue\x1b[0m'

def test_second_use():
    pz = pryzm.Pryzm(echo=False, fixed=True)
    blue_bold = pz.blue()._bold

    assert blue_bold("Hello1") == '\x1b[34;1mHello1\x1b[0m'
    blue_bold("whatevs")
    blue_bold("this")
    blue_bold("that")
    blue_bold("and the other")

    assert blue_bold("Hello2") == '\x1b[34;1mHello2\x1b[0m'
