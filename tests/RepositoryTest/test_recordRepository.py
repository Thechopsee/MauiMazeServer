import sys
import pytest

sys.path.append('./repositories')

from recordsRepository import RecordRepository


def test_login():
    ur=RecordRepository()
    assert 1==ur.loadRecordsbyMaze(5)

test_login()