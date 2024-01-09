import helloworld as hl
import pytest

def test_hello_world():
    
    # Setup - none
    expected = "HelloWorld"
    # Exercise
    actual      = hl.hello_world()
    # Verify
    assert(actual, expected)
    # Cleanup - none