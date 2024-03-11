import sys
import pytest
sys.path.append('./repositories')
from userRepository import UserRepository
import os
@pytest.fixture
def environment():
    os.environ['database_type'] = 'SQLITE'
    os.environ['database_connection_string'] = 'testing.db'

def test_login_false():
    os.environ['database_type'] = 'SQLITE'
    os.environ['database_connection_string'] = 'testing.db'
    assert -1==UserRepository.trytoLoginDatabase("nevim","nevim")['id']
def test_login_true():
    assert -1!=UserRepository.trytoLoginDatabase("lalgate5@prweb.com","mfransewich5")['id']

def test_delete_user():
    name="bgoodayrr@reference.com"
    password="gkayesrr"
    UserRepository.deleteUser(name,password)
    assert -1==UserRepository.trytoLoginDatabase(name,password)[0]

def test_register_user():
    name="bgoodayrr@reference.com"
    password="gkayesrr"
    UserRepository.registerUser(name,password)
    assert -1!=UserRepository.trytoLoginDatabase(name,password)[0]
