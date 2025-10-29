import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from main import helloWorld

def test_hello_world():
    assert type(helloWorld()) == str
