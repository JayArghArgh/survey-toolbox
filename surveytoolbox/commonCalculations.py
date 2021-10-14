import math

# TODO separate these so each method can be tweaked without tweaking the whole.


# Do the math

def get_deltas_from_coordinates(from_coordinates, to_coordinates):
    # difference between both sets of coordinates.
    delta_e = from_coordinates["e"] - to_coordinates["e"]
    delta_n = from_coordinates["n"] - to_coordinates["n"]
    delta_el = from_coordinates["el"] - to_coordinates["el"]
    return delta_e, delta_n, delta_el


def get_deltas_from_bearing_distance(bearing, distance_2d):
    # Creates deltas from bearing and distance
    delta_e = distance_2d * (math.sin(math.radians(bearing)))
    delta_n = distance_2d * (math.cos(math.radians(bearing)))
    delta_el = 0.0
    # TODO requires vertical bearing and distance for delta_el.
    return delta_e, delta_n, delta_el


def get_coordinates_from_deltas(from_coordinates, deltas):
    # Return new coords from deltas.
    return {
        "e": from_coordinates["e"] + deltas[0],
        "n": from_coordinates["n"] + deltas[1],
        "el": from_coordinates["el"] + deltas[2]
    }


def get_bearing_from_deltas(deltas):
    # A great big switch statement to determine the correct direction.
    delta_e = deltas[0]
    delta_n = deltas[1]
    delta_el = deltas[2]
    bearing = 0.0

    if delta_e == 0 and delta_n > 0:
        bearing = 0.0
    elif delta_e == 0 and delta_n < 0:
        bearing = 180.0
    elif delta_e > 0 and delta_n == 0:
        bearing = 90.0
    elif delta_e < 0 and delta_n == 0:
        bearing = 270.0

    # Check for 45 degree variations.
    elif abs(delta_e) == abs(delta_n):
        if delta_e > 0 and delta_n > 0:
            bearing = 45.0
        elif delta_e > 0 > delta_n:
            bearing = 135.0
        elif delta_e < 0 and delta_n < 0:
            bearing = 225.0
        elif delta_n > 0 > delta_e:
            bearing = 315.0

    # Compute it out.
    elif delta_e > 0:
        bearing = math.degrees(math.atan(delta_e / delta_n))
    elif delta_e < 0 and delta_n < 0:
        bearing = math.degrees(math.atan(delta_e / delta_n)) + 180
    elif delta_n > 0 > delta_e:
        bearing = math.degrees(math.atan(delta_e / delta_n)) + 360

    # The final piece.
    if bearing < 0:
        bearing += 180
    return bearing


def get_distance_2d_from_deltas(deltas):
    # Determine the distance. (2D)
    delta_e = deltas[0]
    delta_n = deltas[1]
    distance_2d = math.sqrt((delta_e ** 2 + delta_n ** 2))
    return distance_2d


def get_distance_3d_from_deltas(deltas):
    # Determine the distance. (3D)
    delta_e = deltas[0]
    delta_n = deltas[1]
    delta_el = deltas[2]
    distance_3d = math.sqrt(delta_e ** 2 + delta_n ** 2 + delta_el ** 2)
    return distance_3d

