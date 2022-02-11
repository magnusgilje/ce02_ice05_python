import sys
import pytest
sys.path.insert(0,"..")
import circle

def test_circle_valid_params():
    myC = circle.Circle(1)
    assert round(myC.area(),2) == 3.14
    assert round(myC.perimeter(),2) == 6.28    
    assert myC.summary() == 'area=3.14, perimeter=6.28'
