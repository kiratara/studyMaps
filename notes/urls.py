from django.contrib import admin
from django.urls import path
from . import views


# name-spacing, used by leaflaf.url ?
app_name = 'notes'
urlpatterns = [
    path('', views.topic_list, name='topic_list'),

    # .../subjec-name/ - user filtered by a category and wants products of that category
    path('<slug:subject_slug>/', views.topic_list, name='product_list_by_subject'),
    
    # path('/', views.add_subject, name='add_subject'),

    # ..../id/product-name/ - user requested for detail view of a specific product
    path('<int:id>/<slug:topic_slug>/', views.topic_detail, name='topic_detail')

]