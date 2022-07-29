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
    area : the calculated area/s
    
    Examples
    --------
    >>> calculate_area(1)
    3.141592653589793
    """
    area = np.pi * radius ** 2
    return area


def calculate_circ(radius):
    """
    Calculates the circumference of a circle
    
    Parameters
    ----------
    radius : number or array
        The radius of a circle or many circles
    
    Returns 
    -------
    area : the calculated circumference/s
    
    Examples
    --------
    >>> calculate_circ(1)
    6.283185307179586
    """
    
    circ = 2 * np.pi * radius
    return circ