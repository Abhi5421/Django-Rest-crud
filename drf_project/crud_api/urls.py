from django.urls import path
from . import views


urlpatterns = [
    path('', views.ApiOverview, name='home'),

    # method based url
    path('create/', views.add_items, name='add-items'),
    path('update/<int:pk>', views.update_delete_item, name='update-delete-item'),

    # class based url
    path('get-create-class/', views.ItemListClass.as_view(), name='add-items-class'),

    # generic url
    path('get-create-generic/', views.ItemList.as_view(), name='add-items-generic'),
    path('get-update-delete-generic/<int:pk>', views.ItemDetail.as_view(), name='get-update-delete-generic')
]
