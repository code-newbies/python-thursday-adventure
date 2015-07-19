import pytest
from modules.cockroach import Cockroach

def test_roach_knows_that_it_is_a_roach():
    roach = Cockroach()
    assert roach.name == "cockroach"
