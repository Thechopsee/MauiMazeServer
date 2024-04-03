import pytest
import os

@pytest.fixture
def environment():
    os.environ['database_type'] = 'SQLITE'
    os.environ['database_connection_string'] = 'Testing2'
