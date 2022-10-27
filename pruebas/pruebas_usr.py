import pytest
from negocio import *


def func(x):
    return x + 1

def test_register():
    assert registrar("samu","1234") == True

def test_answer():
    assert ingreso("samu","1234") == True 