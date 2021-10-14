# bfd
import math


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
