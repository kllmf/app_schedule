from django.urls import path

from .views import DepartmentView, SingleDepartmentView

urlpatterns = [
    path('departments/', DepartmentView.as_view()),
    path('departments/<int:pk>', SingleDepartmentView.as_view()),
]
