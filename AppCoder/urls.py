from django.urls import path

from AppCoder.views import curso, inicio

urlpatterns = [
    path('', inicio, name='AppCoder_Inicio'),
    path('curso/', curso, name='AppCoder_Curso')
]