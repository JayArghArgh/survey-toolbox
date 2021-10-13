# bdc
from .commonCalculations import get_deltas_from_coordinates
from .commonCalculations import get_bearing_from_deltas
from .commonCalculations import get_distance_2d_from_deltas
from .commonCalculations import get_distance_3d_from_deltas


def bearing_distance_from_coordinates(from_coordinates, to_coordinates):
    # Return bearing and distance(s) from two sets of coordinates.
    # print(from_coordinates, to_coordinates)
    deltas = get_deltas_from_coordinates(from_coordinates, to_coordinates)
    bearing = get_bearing_from_deltas(deltas)
    dist_2d = get_distance_2d_from_deltas(deltas)
    dist_3d = get_distance_3d_from_deltas(deltas)
    return [bearing, dist_2d, dist_3d]
