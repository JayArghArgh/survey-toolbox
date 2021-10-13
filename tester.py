# from surveytoolbox import cbd
from surveytoolbox import commonCalculations
from surveytoolbox import surveyPoint
from surveytoolbox import pointStore

EASTING = surveyPoint.EASTING
NORTHING = surveyPoint.NORTHING
ELEVATION = surveyPoint.ELEVATION

# Start a point store so you can track your points.
my_point_store = pointStore.PointStore()

# Import the common calculations.
my_math = commonCalculations.CommonCalculations()

# Create some points and add to point store.
point_1 = surveyPoint.SurveyPoint("JRR")
my_point_store.set_new_point(point_1)

point_2 = surveyPoint.SurveyPoint("JayArghArgh")
my_point_store.set_new_point(point_2)

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

current_points = my_point_store.get_point_store()
for k, v in current_points.items():
    print(current_points[k].get_point_name())
    print(current_points[k].get_status())
    print(current_points[k].get_created_dtg())
    print(current_points[k].get_vertex())

# Return bearing, distance 2d, distance 3d.
print(my_math.get_bearing_distance_from_coordinates(point_1.get_vertex(), point_2.get_vertex()))
# TODO currently returning back-bearing.
