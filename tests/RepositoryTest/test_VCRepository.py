import sys
import pytest
sys.path.append('./repositories')
sys.path.append('./tools')
from VCRepository import VCRepository
from VerificationCodeGenerator import VerificationCodeGenerator
database_string="testing.db"

def test_generate_newcode():
    code=VerificationCodeGenerator.generate_verification_code()
    count_before=VCRepository.count_of_unused(database_string)
    VCRepository.save_verification_code(code,database_string)
    count_after=VCRepository.count_of_unused(database_string)
    assert count_after> count_before

def test_set_code_used():
    code=VerificationCodeGenerator.generate_verification_code()
    count_before=VCRepository.count_of_unused(database_string)
    VCRepository.save_verification_code(code,database_string)
    VCRepository.updateCode(code,database_string)
    count_after=VCRepository.count_of_unused(database_string)
    assert count_after== count_before

def test_is_code_taken_true():
    code=VerificationCodeGenerator.generate_verification_code()
    VCRepository.save_verification_code(code,database_string)
    VCRepository.updateCode(code,database_string)
    istaken=VCRepository.isCodeTaken(code,database_string)
    assert istaken==1
def test_is_code_taken_false():
    code=VerificationCodeGenerator.generate_verification_code()
    VCRepository.save_verification_code(code,database_string)
    istaken=VCRepository.isCodeTaken(code,database_string)
    assert istaken==0
