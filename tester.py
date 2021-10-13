# from surveytoolbox import cbd
from surveytoolbox import commonCalculations
from surveytoolbox import surveyPoint
from surveytoolbox import pointStore

EASTING = surveyPoint.EASTING
NORTHING = surveyPoint.NORTHING
ELEVATION = surveyPoint.ELEVATION

my_point_store = pointStore.PointStore()
my_math = commonCalculations.CommonCalculations()

point_1 = surveyPoint.SurveyPoint("JRR")
point_2 = surveyPoint.SurveyPoint("JayArghArgh")

my_point_store.set_new_point(point_1)
my_point_store.set_new_point(point_2)

point_1.set_vertex(
    {EASTING: 100}
)

point_1.set_vertex({NORTHING: 200.123, ELEVATION: 56.123})

print(point_1.get_vertex())

current_points = my_point_store.get_point_store()

# for k, v in current_points.items():
#     print(current_points[k].get_point_name())
    # print(current_points[x].get_status())
    # print(current_points[x].get_created_dtg())

# print(my_math.get_bearing_distance_from_coordinates(point_1.get_vertex(), point_2.get_vertex()))
