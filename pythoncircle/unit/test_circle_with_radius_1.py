import sys
sys.path.insert(0,"..")
import circle

def test_circle_with_radius_1_2dp():
    myC = circle.Circle(1)
    assert round(myC.area(),2) == 3.14
    assert round(myC.perimeter(),2) == 6.28

