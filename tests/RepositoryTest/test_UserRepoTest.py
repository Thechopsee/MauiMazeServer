import sys
import pytest
sys.path.append('./repositories')
from userRepository import UserRepository
import os
@pytest.fixture
def environment():
    os.environ['database_type'] = 'SQLITE'
    os.environ['database_connection_string'] = 'Testing2.db'

def test_login_false():
    os.environ['database_type'] = 'SQLITE'
    os.environ['database_connection_string'] = 'Testing2.db'
    assert -1==UserRepository.trytoLoginDatabase("nevim","nevim")['id']
def test_login_true():
    assert -1!=UserRepository.trytoLoginDatabase("arase2@devhub.com","3")['id']

def test_delete_user():
    name="kludgate3@hugedomains.com"
    password="4"
    UserRepository.deleteUser(name,password)
    assert -1==UserRepository.trytoLoginDatabase(name,password)['id']

def test_register_user():
    name="kludgate3@hugedomains.com"
    password="4"
    UserRepository.registerUser(name,password)
    assert -1!=UserRepository.trytoLoginDatabase(name,password)['id']
