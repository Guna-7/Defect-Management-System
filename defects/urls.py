from django.urls import path
from defects import views

urlpatterns = [
    path('', views.defectList, name='alldefects'),
    path('<int:id>', views.desc, name='desc'),
    path('edit/<int:id>/', views.edit_defect, name='edit'),
    path('add', views.add_defect, name='add_d'),
    path('filter_dev', views.filter_dev, name='filter_defects'),
    path('completed_defects', views.completed_defects, name='completed_defects'),
    path('pending_defects', views.pending_defects, name='pending_defects'),
]
