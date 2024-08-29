import pytest
from error_code import calculate_area

def test_calculate_area_valid():
    assert calculate_area(10) == 314.0  

#def test_calculate_area_invalid():
 #   assert calculate_area("twenty") == 628.0
