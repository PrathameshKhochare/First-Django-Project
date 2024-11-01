from django.urls import path
from . import views

# localhost:8080/studyplanner/index
urlpatterns = [
    path('index',views.index),
    # path('monday',views.monday),
    # path('tuesday',views.tuesday)
    path('<day>',views.weekly_timetable)
]

