import sys
import pytest
import os

sys.path.append('./repositories')
sys.path.append('./databaseServices')

from mazeRepository import MazeRepository
from sqliteAdapter import SqliteAdapter

@pytest.fixture
def environment():
    os.environ['database_type'] = 'SQLITE'
    os.environ['database_connection_string'] = 'Testing2.db'

def test_add_maze():
    count_bef =MazeRepository.countMazes()
    id=MazeRepository.saveMazetoDatabase(5,'Classic',1,10,10)
    count_aft =MazeRepository.countMazes()
    assert count_bef<count_aft

def test_load_maze_for_user():
    MazeRepository.saveMazetoDatabase(5,'Classic',1,10,10)
    mazes=MazeRepository.getMazeList(5)
    assert len(mazes)>0

def test_save_edges():
    edges=[(5,2,5),(5,7,5),(5,4,5)]
    count_bef=len(MazeRepository.getMaze(5)['edges'])
    MazeRepository.saveEdgeToDatabase(edges)
    count_aft =len(MazeRepository.getMaze(5)['edges'])
    assert count_bef<count_aft

def test_load_edghes_by_maze():
    edges=MazeRepository.getMaze(5)['edges']
    assert len(edges)>0

