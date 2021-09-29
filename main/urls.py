from django.urls import path
from .views import detail, index, AddDoctors, AddNurses, AddPatients, AddMainDoctors


urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:pk>', detail, name='detail'),
    path('doctor/registration', AddDoctors.as_view(), name='addDoctor'),
    path('nurse/registration', AddNurses.as_view(), name="addNurses"),
    path('patient/registration', AddPatients.as_view(), name="addPatients"),
    path('maindoctor/registration', AddMainDoctors.as_view(), name="addMaindoctors"),
]