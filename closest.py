import sys
import math

def bruteforce3D(points):
    p1Closest = {}
    p2losest = {}
    distClosest = sys.maxsize
    for i in points:
        for j in points:
            if i==j:
                break
            
            tempClosest = math.sqrt( (j[0]-i[0])**2 +  (j[1]-i[1])**2 + (j[2]-i[2])**2 )
            if(tempClosest<distClosest):
                distClosest=tempClosest
                p1Closest=i
                p2Closest=j
    
    return [p1Closest,p2Closest]         