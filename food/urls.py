from . import views
from django.urls import path
app_name = 'food'
urlpatterns = [
    #/food/
    path('',views.IndexClassView.as_view(),name='index'),
    #/food/home
    path('home',views.index,name='indexT'),
    
    #/food/1
    path('<int:pk>',views.FoodDetail.as_view(),name="detail"),
    path('<int:pass_data>',views.detail,name="detailT"),

    #add item
    path('add/',views.CreateItem.as_view(),name='create_item'),
    path('add/',views.create_item,name='create_itemT'),
    
    #edit items
    path('item/',views.item,name='item'),
    path('update/<int:id>/',views.update_item,name='update_item'),
    #delete item
    path('delete/<int:id>/',views.delete_item,name='delete_item'),
]