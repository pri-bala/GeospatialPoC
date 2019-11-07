
import random
import numpy as np

def GenerateWellConceptName():    

        
    
    #First Letter
    strName = chr(random.randrange(65,91))
    
    #Second letter?!
    if random.random() > 0.7:
        strName += chr(random.randrange(66,69)).lower()
        
    #Final numbers
    strName += "-" + str(random.randrange(0,23))
    
    return strName

def GenerateAxisValue(axis_min, axis_max):
    '''
    Function generates a random value between an axis min and max
    '''
 
    
    axis_range = axis_max - axis_min
    axis_val = axis_min + (random.random() * axis_range)
    return axis_val


def GenerateWellConcept(x_min , x_max , y_min , y_max):
    '''
    Function returns a Well Concept list: with name, x,y, and resoure
    '''
    

    
    wc_name = GenerateWellConceptName()
    wc_x = GenerateAxisValue(x_min, x_max)
    wc_y = GenerateAxisValue(y_min, y_max)
    wc_resource = np.random.exponential(10) * 8 
    return [wc_name, [wc_x, wc_y], wc_resource]
