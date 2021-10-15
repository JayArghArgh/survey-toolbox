# Declare some constants.
from surveytoolbox.config import EASTING, NORTHING, ELEVATION

# Import functions.
from surveytoolbox.PointStore import NewPointStore
from surveytoolbox.SurveyPoint import NewSurveyPoint

from surveytoolbox.bdc import bearing_distance_from_coordinates
from surveytoolbox.cbd import coordinates_from_bearing_distance
from surveytoolbox.fmt_dms import format_as_dms

# Start a point store so you can track your points.
pointStore = NewPointStore()

# Create some points and add to point store.
point_1 = NewSurveyPoint("JRR")
pointStore.set_new_point(point_1)

point_2 = NewSurveyPoint("JayArghArgh")
pointStore.set_new_point(point_2)

# Start playing
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
    f"\nDistance (3d): {target_loc[2]}"
)

# Create a new point using the provided bearing and distance (it shoudl duplicate point 2)
point_3 = NewSurveyPoint("JRR2110141000")
pointStore.set_new_point(point_3)

point_3.set_vertex(
    coordinates_from_bearing_distance(
        point_1.get_vertex(),
        target_loc[0],
        target_loc[1]
    )
)

# Uncomment this for an example of listing specific information for all points.
current_points = pointStore.get_point_store()
for k, v in current_points.items():
    print(
        f"{current_points[k].get_point_name()}: {current_points[k].get_vertex()}"
    )

# TODO returning back-bearing for some reason.
