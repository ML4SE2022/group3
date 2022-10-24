import math

def arc_length(r, angleA, angleB):
    return (360.0 - abs(angleB - angleA)) * math.pi * r / 180.0