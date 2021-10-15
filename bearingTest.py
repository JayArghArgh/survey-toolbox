# Declare some constants.
from surveytoolbox.config import EASTING, NORTHING, ELEVATION

# Import functions

from surveytoolbox.SurveyPoint import NewSurveyPoint
from surveytoolbox.bdc import bearing_distance_from_coordinates
from surveytoolbox.fmt_dms import format_as_dms

point_1 = NewSurveyPoint("JRR")
point_2 = NewSurveyPoint("JayArghArgh")

point_1.set_vertex(
    {
        EASTING: 100,
        NORTHING: 100,
        ELEVATION: 30
    }
)

point_2.set_vertex(
    {
        EASTING: 200,
        NORTHING: 100,
        ELEVATION: 30
    }
)


# Calculate and print the bearing and distance between two points.
target_loc = bearing_distance_from_coordinates(point_1.get_vertex(), point_2.get_vertex())
print(
    f"Bearing: {format_as_dms(target_loc[0])}"
    f"\nDistance (2d): {target_loc[1]}"
    # f"\nDistance (3d): {target_loc[2]}"
)

