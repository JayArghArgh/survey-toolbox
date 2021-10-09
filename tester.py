# from surveytoolbox import cbd

from surveytoolbox import surveyPoint
from surveytoolbox import pointStore

my_point_store = pointStore.PointStore()

point_1 = surveyPoint.SurveyPoint()
point_2 = surveyPoint.SurveyPoint()

point_1.set_point_name("justin")
point_2.set_point_name("fred")

my_point_store.set_new_point(point_1)
my_point_store.set_new_point(point_2)

current_points = my_point_store.get_point_store()

for x in current_points:
    print(current_points[x].get_point_name())
    print(current_points[x].get_status())
    print(current_points[x].get_created_dtg())