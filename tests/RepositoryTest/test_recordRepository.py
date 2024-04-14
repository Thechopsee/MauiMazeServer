import sys
import pytest

sys.path.append('./repositories')

from recordsRepository import RecordRepository
from GameRecord import GameRecord
from MoveRecord import MoveRecord


def test_load_records():
        assert 0<len(RecordRepository.loadRecordsbyMaze(5))
def test_load_record_moves():
        gameRecords=RecordRepository.loadRecordsbyMaze(7)
        assert len(gameRecords[0].records)>0
def test_load_records_byuser():
        gameRecords=RecordRepository.loadRecordsbyUser(7)
        assert 0<len(gameRecords)
def test_save_record_with_moves():
        gr=GameRecord(0,7,7,100,10,"1->2")
        id=RecordRepository.saveRecordtoDatabase(gr.to_dict())
        record=RecordRepository.loadRecordByID(id)[0]
        assert gr.mazeID==record.mazeID
        assert gr.userID==record.userID
        assert len(record.records)==0

        formated=[]
        formated.append((0.56,0.47,1,100,id,1))
        formated.append((0.56,0.47,1,100,id,2))
        formated.append((0.56,0.47,1,100,id,3))
        RecordRepository.saveMovesToDatabase(formated)
        record=RecordRepository.loadRecordByID(id)[0]
        assert gr.mazeID==record.mazeID
        assert gr.userID==record.userID
        assert len(record.records)==3




        
