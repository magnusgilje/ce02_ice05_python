import sys
import pytest
sys.path.insert(0,"..")
import circle


def test_circle_with_radius_minus_1():

    with pytest.raises(Exception) as error_info:
        myC = circle.Circle(-1)

