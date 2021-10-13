# from surveytoolbox import cbd
# from surveytoolbox import commonCalculations as commonCalculations
from surveytoolbox import surveyPoint as surveyPoint
from surveytoolbox import pointStore as pointStore
from surveytoolbox import cbd as cbd
from surveytoolbox import bdc as bdc

# Declare some constants.
EASTING = surveyPoint.EASTING
NORTHING = surveyPoint.NORTHING
ELEVATION = surveyPoint.ELEVATION

# Start a point store so you can track your points.
pointStore = pointStore.PointStore()

# Setup the calculations short name for ease of use.
# calcs = commonCalculations.CommonCalculations()

# Create some points and add to point store.
point_1 = surveyPoint.SurveyPoint("JRR")
pointStore.set_new_point(point_1)

point_2 = surveyPoint.SurveyPoint("JayArghArgh")
pointStore.set_new_point(point_2)

# Start playing
point_1.set_vertex(
    {EASTING: 100}
)

point_1.set_vertex(
    {
        NORTHING: 200.123,
        ELEVATION: 56.123
    }
)

current_points = pointStore.get_point_store()
for k, v in current_points.items():
    print(current_points[k].get_point_name())
    print(current_points[k].get_status())
    print(current_points[k].get_created_dtg())
    print(current_points[k].get_vertex())

# Return bearing, distance 2d, distance 3d.
# print(calcs.get_bearing_distance_from_coordinates(point_1.get_vertex(), point_2.get_vertex()))
# TODO currently returning back-bearing.

print("running cbd")
target_loc = bdc.bearing_distance_from_coordinates(point_1.get_vertex(), point_2.get_vertex())
print(f"Bearing: {target_loc[0]}\nDistance (2d): {target_loc[1]}\nDistance (3d): {target_loc[2]}")
