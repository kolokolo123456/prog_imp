#!/usr/bin/env python3

import random
import math

def point_aleatoire(c1,c2):
    return (random.uniform(c1[0],c1[1]),random.uniform(c2[0],c2[1]))

def triangle_aleatoire(c1,c2):
    triangle=[]
    for _ in range(3):
        triangle.append(point_aleatoire(c1,c2))
    return triangle 

def tourne_point_autour(point,centre,angle):
    return ((point[0]-centre[0])*math.cos(angle)-(point[1]-centre[1])*math.sin(angle)+centre[0],(point[0]-centre[0])*math.sin(angle)+(point[1]-centre[1])*math.cos(angle)+centre[1]) 

def tourne_triangle_autour(triangle, centre, angle):
    return (tourne_point_autour(triangle[0],centre,angle),tourne_point_autour(triangle[1],centre,angle),tourne_point_autour(triangle[2],centre,angle))
    