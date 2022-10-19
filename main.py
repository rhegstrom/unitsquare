# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 02:56:45 2022

@author: Roger Hegstrom(rhegstrom@avc.edu)

Find the radius of the circle inside the unit square
   that has the property that the average distance of points inside the circle to the center of the square  
   is the same as the average distance of points outside the circle to the nearest edge of the square.  
   
   For this problem, set up a repo in your GitHub account, work the problem, push the python code to GitHub and turn in the URL

    To grade this I will select 1000 points inside your circle and 1000 points outside your circle and compute the average distances indicated above.   
    Score 100 points if the averages are within 0.01 of each other! 
"""

import numpy as np
import time


def findDistance(start, end):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    
    return np.sqrt(dx**2 + dy**2)


def findNearestEdge(coord):
    x = coord[0]
    y = coord[1]
           
    x_edge = -0.5 if x < 0 else 0.5
    y_edge = -0.5 if y < 0 else 0.5
    
    # distance to nearest y edge
    dy = abs(y_edge - y)
    
    # distance to nearest x edge
    dx = abs(x_edge - x)
    
    return [x_edge, y] if dx < dy else [x, y_edge]

  

prog_start_time = time.time()   
# Generate 1000 random coordinates 
points = np.random.default_rng().uniform(-0.5, 0.5, size=(1000,2))



for circle_radius in np.arange(0, 0.5, step=0.0001):
    di = []  # distances of points in circle(to origin)
    do = []  # distances of points outside circle(to nearest edge)
    
    for point in points:       
        dist_origin = findDistance(start=[0,0], end=point)
        
        if  dist_origin < circle_radius: # point is in circle
            di.append(dist_origin) 
        else:
            do.append(findDistance(point, findNearestEdge(point)))
    mdi = np.mean(di) if len(di) > 0 else 0
    mdo = np.mean(do) if len(do) > 0 else 0
    
#    print(f'Average distance to origin for points in circle = {np.mean(di):.4f}')
#    print(f'Average distance to nearest edge for points outside circle = {np.mean(do):.4f}')
    
    if abs(mdi - mdo) < 0.001:
        print(f"Found match: mdi={mdi:.4f} mdo={mdo:.4f}\n")
        print(f"circle radius is {circle_radius:.4f}\n")
        
        prog_end_time = time.time()
        print(f"Script took {prog_end_time-prog_start_time:.2f} sec to execute..")
        
        break

    