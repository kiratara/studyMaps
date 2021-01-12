from django.contrib import admin
from django.urls import path
from . import views


app_name = 'notes'
urlpatterns = [
    path('', views.topic_list, name='topic_list'),
    
    # supposed to be when user click on `add subject` button
    path('add-subject/', views.add_subject, name='add_subject'),

    # supposed to be when user click on `add Topic` button
    path('add-topic/', views.add_topic, name='add_topic'),
    
    # supposed to be when user click on `add Question` button
    path('<int:topic_id>/add-question/', views.add_question, name='add_question'),
    
    # .../subjec-name/ - user filtered by a category and wants products of that category
    path('<slug:subject_slug>/', views.topic_list, name='topic_list_by_subject'),
    
    # ..../id/product-name/ - user requested for detail view of a specific product
    path('<int:id>/<slug:topic_slug>/', views.topic_detail, name='topic_detail')

]