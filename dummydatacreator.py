

import random
import numpy as np
from shapely.geometry import Point
def GenerateWellConceptName():    
    '''Creates a well concept name, using random characters and digits
    
    
    Parameters
    ----------
    None
    
    
    Returns
    -------
    str
        Well Concept Name
    
    '''
    # First Letter
    strName = chr(random.randrange(65,91))
    
    #Second letter if needed
    if random.random() > 0.7:
        strName += chr(random.randrange(66,69)).lower()
        
    #Final numbers
    strName += "-" + str(random.randrange(0,23))
    
    return strName


def GenerateAxisValue(axis_min: float, axis_max: float):
    '''Function generates a random value between two numbers (axis_min <= x < axis_max)
    
    Parameters
    ----------
    axis_min
        Lower bound of the axis, inclusive
    
    axis_max
        Upper bound of the axis, exclusive
        
    Returns
    -------
    float
    '''
 
    #Calculate range
    axis_range = axis_max - axis_min
    
    #Produce a random value within range
    axis_val = axis_min + (random.random() * axis_range)
    return axis_val


def GenerateWellConcept(poly):
    '''Function returns a Well Concept list: with name, x,y, and resurce
    
    Parameters
    ----------
    x_min
        Lower bound of x axis, inclusive
    x_max
        Upper bound of x axis, exclusive
    y_min
        Lower bound of y axis, inclusive
    y_max
        Upper bound of y axis, exclusive

        
    Returns
    -------    
    [str, [float,float], float]    
        [Well Concept Name, [x,y], Resource]
    
    '''
    x_min, y_min, x_max, y_max = poly.bounds


    
    wc_name = GenerateWellConceptName()
    
    
    wc_resource = np.random.exponential(10) * 8 
    #Loop until random point within the polygon is found
    
    while True:
        wc_x = GenerateAxisValue(x_min, x_max)
        wc_y = GenerateAxisValue(y_min, y_max)
        if Point(wc_x, wc_y).within(poly) == True:
            break
    
    return [wc_name, [wc_x, wc_y], wc_resource]
