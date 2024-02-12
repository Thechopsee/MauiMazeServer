import sys
import pytest
sys.path.append('./repositories')
from userRepository import UserRepository
database_string="testing.db"

def test_login_false():
    assert -1==UserRepository.trytoLoginDatabase("nevim","nevim",database_string)[0]
def test_login_true():
    assert -1!=UserRepository.trytoLoginDatabase("lalgate5@prweb.com","mfransewich5",database_string)[0]

def test_delete_user():
    name="bgoodayrr@reference.com"
    password="gkayesrr"
    UserRepository.deleteUser(name,password,database_string)
    assert -1==UserRepository.trytoLoginDatabase(name,password,database_string)[0]

def test_register_user():
    name="bgoodayrr@reference.com"
    password="gkayesrr"
    UserRepository.registerUser(name,password,database_string)
    assert -1!=UserRepository.trytoLoginDatabase(name,password,database_string)[0]
