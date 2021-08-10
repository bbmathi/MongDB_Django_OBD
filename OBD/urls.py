from django.urls import path
from OBD import views
 
urlpatterns = [ 
    path('api/obddata', views.obd_list),
    path('api/obddata/<int:pk>', views.obd_detail),
    path('api/obddata/published', views.obd_list_published),
    path('table', views.TableView),
    path('map', views.MapView),
    path('dashboard', views.ChartView),
]
