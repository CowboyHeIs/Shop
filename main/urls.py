from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.show_main, name='show_main'),
    path('xml/', views.all_objects_xml, name='all_objects_xml'),  # XML view for all products
    path('json/', views.all_objects_json, name='all_objects_json'),  # JSON view for all products
    path('xml/<str:id>/', views.object_by_id_xml, name='object_by_id_xml'),  # XML view by ID
    path('json/<str:id>/', views.object_by_id_json, name='object_by_id_json'),  # JSON view by ID
    path('add/', views.add_product, name='add_product'),  # New route for adding product
]
