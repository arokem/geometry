import numpy as np

def calculate_area(radius):
    
    """ 
    Calculates the area of a circle
    
    Parameters
    ----------
    radius : number or array
        The radius of a circle or many circles
    
    Returns 
    -------
    area : the calculate area/s
    
    Examples
    --------
    >>> calculate_area(1)
    3.141592653589793
    """
    area = np.pi * radius ** 2
    return area


def calculate_circ(radius):
    circ = 2 * np.pi * radius
    return circ