# from surveytoolbox import cbd
from surveytoolbox import commonCalculations
from surveytoolbox import surveyPoint
from surveytoolbox import pointStore

my_point_store = pointStore.PointStore()
my_math = commonCalculations.CommonCalculations()

point_1 = surveyPoint.SurveyPoint("JRR")
point_2 = surveyPoint.SurveyPoint("JayArghArgh")

# point_1.set_point_name("justin")
# point_2.set_point_name("fred")

my_point_store.set_new_point(point_1)
my_point_store.set_new_point(point_2)

current_points = my_point_store.get_point_store()

# print("fred", current_points["fred"])

for k, v in current_points.items():
#     print(k)
    print(current_points[k].get_point_name())
    # print(current_points[x].get_status())
    # print(current_points[x].get_created_dtg())

print(my_math.get_bearing_distance_from_coordinates(point_1.get_vertex(), point_2.get_vertex()))
