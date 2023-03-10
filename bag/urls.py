from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('add-item', add_item, name='add-item'),
    path('update-item/<int:item_id>', update_item, name='update-item'),
    path('delete-item/<int:item_id>', delete_item, name='delete-item'),
]
