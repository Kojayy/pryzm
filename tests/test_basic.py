import os
import sys
sys.path.append(os.path.normpath(os.path.join(os.path.dirname(__file__), "../")))

import pryzm

def test_basic_foreground():
    pz = pryzm.Pryzm()

    assert pz.red("test")    == '\x1b[31mtest\x1b[0m'
    assert pz.cyan("test")   == '\x1b[36mtest\x1b[0m'

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
