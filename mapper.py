from db import *

wind_map = load('wind.direction.map')

def degreeToDirectionMapper(deg):
    for direction in wind_map.keys():
        for degree in wind_map[direction]:
            if deg == degree:
                return direction