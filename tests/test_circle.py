import numpy as np
from geometry.circle import calculate_area

def test_calculate_area(): 
    assert np.isclose(calculate_area(1), 3.14)