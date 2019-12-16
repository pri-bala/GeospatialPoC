

import random
import numpy as np
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from shapely.ops import cascaded_union
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
    strName += "-" + str(random.randrange(0,999))
    
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


def GenerateMultipleWellConceptsTEST(input_gdf_polygons, n_concepts = 100, lon_min = -60.45, lon_max = -60.30,                          lat_min = 10.00, lat_max = 10.20):

    '''Function generates a list of well concepts. Not that there is a slight workaround in this method, see below. Hence it has been labelled TEST
    
    Parameters
    ----------
    input_gdf_polygons
        GeoDataFrame with a polygon geometry column
    
    n_concepts
        Number of well concepts to return
        
    Returns
    -------
    list: [[WC Names], [WC Lat Lon], [WC Resource]]   - where len([WC Names, WC Lat Lon  and WC Resource 
    '''
    l = []
    #BUG WORKAROUND FIX- Some polygons are invalid since first and last points are the same - they must not be.
    for p in input_gdf_polygons.polygon.values:
        if p.is_valid == True:
            l.append(p)

    # Union of all polygons
    targ_poly_union = cascaded_union(l)
    
    
    #Generate a polygon bounding box from the min and max of lon and lat
    bbox = Polygon([[lon_min,lat_min], [lon_min,lat_max], [lon_max, lat_max], [lon_max, lat_min]])
    
    # Get all polygons within bbx
    bbox = bbox.intersection(targ_poly_union)
    
    #Generate Well Concepts
    WellConcepts = [GenerateWellConcept(bbox)  for i in range(n_concepts)]

    return list(zip(*WellConcepts))