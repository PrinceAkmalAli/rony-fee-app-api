from django.urls import path
from . import views
from studentapp.views import delete_student_by_roll_no

urlpatterns = [
    path('students/', views.student_details_list, name='student_details_list'),
    path('students/challan/<str:roll_no>/', views.get_challan_by_roll_no, name='get_challan_by_roll_no'),
    path('students/update/<str:roll_no>/', views.update_student_details, name='update_student_details'),
    path('students/details/', views.student_details_list, name='student_details_list'),
    path('students/delete/<str:roll_no>/', delete_student_by_roll_no, name='delete-student'),
]