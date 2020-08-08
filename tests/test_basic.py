import os
import sys
absp = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, absp)

import pryzm

def test_basic_foreground():
    pz = pryzm.Pryzm(echo=True)

    assert pz.red("test")    == '\x1b[31mtest\x1b[0m'
    assert pz.cyan("test")   == '\x1b[36mtest\x1b[0m'

def test_basic_background():
    pz = pryzm.Pryzm(echo=True)

    assert pz.RED("test")   == '\x1b[41mtest\x1b[0m'

def test_basic_fore_back_combination():
    pz = pryzm.Pryzm(echo=True)

    assert pz.red().RED("test") == '\x1b[31;41mtest\x1b[0m'

def test_create_function():
    pz = pryzm.Pryzm(echo=True)

    both_red = pz.red().RED
    assert both_red("test") == '\x1b[31;41mtest\x1b[0m'

def test_multiple_arguments():
    pz = pryzm.Pryzm(echo=True)

    blue = pz.blue
    assert blue("This is", "also blue") == '\x1b[34mThis is also blue\x1b[0m'

def test_multiple_arguments_in_class():
    pz = pryzm.Pryzm(echo=True)

    assert pz.blue("This is", "also blue") == '\x1b[34mThis is also blue\x1b[0m'
