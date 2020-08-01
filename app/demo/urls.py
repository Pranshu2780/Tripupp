from django.urls import path
from . import views

urlpatterns=[
    path('',views.main,name='main'),
    path('exams/',views.exams,name='exams'),
     path('jeemains/',views.jeemains,name='jeemains'),
     path('jeeadvanced/',views.jeeadvanced,name='jeeadvanced'),
      path('pdf/',views.pdf,name='jeeadvanced'),
      path('tenth/',views.tenth,name='tenth'),
      path('twelveth/',views.twelveth,name='twelveth'),
]