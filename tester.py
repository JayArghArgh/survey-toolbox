from surveytoolbox import surveyPoint as surveyPoint
from surveytoolbox import pointStore as pointStore
from surveytoolbox import cbd as cbd
from surveytoolbox import bdc as bdc
from surveytoolbox import dec as dec
from surveytoolbox import dms as dms
from surveytoolbox import fmt_dms as fmt_dms


# Declare some constants.
EASTING = surveyPoint.EASTING
NORTHING = surveyPoint.NORTHING
ELEVATION = surveyPoint.ELEVATION

# Start a point store so you can track your points.
pointStore = pointStore.PointStore()

# Create some points and add to point store.
point_1 = surveyPoint.SurveyPoint("JRR")
pointStore.set_new_point(point_1)

point_2 = surveyPoint.SurveyPoint("JayArghArgh")
pointStore.set_new_point(point_2)

# Start playing
point_1.set_vertex(
    {
        EASTING: 100,
        NORTHING: 200.123,
        ELEVATION: 56.123
    }
)

point_2.set_vertex(
    {
        EASTING: 180,
        NORTHING: 300.070,
        ELEVATION: 56.123
    }
)

# Uncomment this for an example of listing specific information for all points.
# current_points = pointStore.get_point_store()
# for k, v in current_points.items():
#     print(current_points[k].get_point_name())
#     print(current_points[k].get_status())
#     print(current_points[k].get_created_dtg())
#     print(current_points[k].get_vertex())


# Calculate and print the bearing and distance between two points.
target_loc = bdc.bearing_distance_from_coordinates(point_1.get_vertex(), point_2.get_vertex())
print(
    f"Bearing: {fmt_dms.format_as_dms(target_loc[0])}"
    f"\nDistance (2d): {target_loc[1]}"
    f"\nDistance (3d): {target_loc[2]}"
)

# Create a new point using the provided bearing and distance (it shoudl duplicate point 2)
point_3 = surveyPoint.SurveyPoint("JRR2110141000")
pointStore.set_new_point(point_3)

point_3.set_vertex(
    cbd.coordinates_from_bearing_distance(
        point_1.get_vertex(),
        target_loc[0],
        target_loc[1]
    )
)

print(f"p1: {point_1.get_vertex()}")
print(f"p2: {point_2.get_vertex()}")
print(f"p3: {point_3.get_vertex()}")

# TODO returning back-bearing for some reason.
