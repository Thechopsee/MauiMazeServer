import sys
import pytest
sys.path.append('../../repositories')
from userRepository import UserRepository


def test_login():
    ur=UserRepository()
    assert -1==ur.trytoLoginDatabase("nevim","nevim");
