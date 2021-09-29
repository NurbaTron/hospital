from django.urls import path
from .views import detail, index, AddDoctors, AddNurses, AddPatients, register, signin, signout


urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:pk>', detail, name='detail'),
    path('doctor/registration', AddDoctors.as_view(), name='addDoctor'),
    path('nurse/registration', AddNurses.as_view(), name="addNurses"),
    path('patient/registration', AddPatients.as_view(), name="addPatients"),
    path('register/', register, name='register'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout')
]