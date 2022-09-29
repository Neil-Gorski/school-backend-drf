
from .views import ExamView, TaskView
from rest_framework_extensions.routers import NestedRouterMixin
from rest_framework.routers import DefaultRouter


# geile scheiss

class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    pass

router = NestedDefaultRouter()
exams_router = router.register("exams", ExamView, basename="exams")
exams_router.register("tasks", TaskView, basename="exams-tasks", parents_query_lookups=['exam'])
urlpatterns = router.urls