import sys
import pytest
import os
sys.path.append('./repositories')
sys.path.append('./tools')
from VCRepository import VCRepository
from VerificationCodeGenerator import VerificationCodeGenerator

@pytest.fixture
def environment():
    os.environ['database_type'] = 'SQLITE'
    os.environ['database_connection_string'] = 'Testing2.db'

def test_generate_newcode():
    code=VerificationCodeGenerator.generate_verification_code()
    count_before=VCRepository.count_of_unused()
    VCRepository.save_verification_code(code)
    count_after=VCRepository.count_of_unused()
    assert count_after> count_before
def test_set_code_used():
    code=VerificationCodeGenerator.generate_verification_code()
    count_before=VCRepository.count_of_unused()
    VCRepository.save_verification_code(code)
    VCRepository.updateCode(str(code))
    count_after=VCRepository.count_of_unused()
    assert count_after== count_before

def test_is_code_taken_true():
    code=VerificationCodeGenerator.generate_verification_code()
    VCRepository.save_verification_code(code)
    VCRepository.updateCode(code)
    istaken=VCRepository.isCodeTaken(code)
    assert istaken[0]==1
def test_is_code_taken_false():
    code=VerificationCodeGenerator.generate_verification_code()
    VCRepository.save_verification_code(code)
    istaken=VCRepository.isCodeTaken(code)
    assert istaken[0]==0
