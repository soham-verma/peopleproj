from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name='index'),
    path('people/', person_list_view, name='person_list'),
    path('people/add/', person_create_view, name='person_add'),
    path('people/<int:pk>/', person_detail_view, name='person_detail'),
    path('people/<int:pk>/edit/', person_update_view, name='person_edit'),
    path('people/<int:pk>/delete/', person_delete_view, name='person_delete'),
    # path('people/<int:pk>/links/<int:link_id>/delete/', link_confirm_delete_view, name='link_confirm_delete'),
    
    path('labels/', label_list_view, name='label_list'),
    path('labels/<int:pk>/', label_detail_view, name='label_detail'),
]
