from django.contrib import admin
from django.urls import path, include
from users.views import index

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('notice/', include('notice.urls')),
    path('free/', include('free.urls')),
    path('anonymous/', include('anonymous.urls')),
    path('about/', include('about.urls')),
    path('calender/', include('calender.urls')),
    path('timetable/', include('timetable.urls')),
]
