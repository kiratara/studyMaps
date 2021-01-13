from django.contrib import admin
from django.urls import path

from . import views


app_name = 'notes'
urlpatterns = [
    path('', views.topic_list_view, name='topic_list'),
    path('<slug:subject_slug>/topics/', views.topic_list_view, name='topic_list_by_subject'),

    # Subject
    path('subject/add/', views.subject_add_view, name='subject_add'),
    path('subject/update/<int:subject_id>', views.subject_update_view, name='subject_update'),
    path('subject/delete/<int:subject_id>/', views.subject_delete_view, name='subject_delete'),

    # Topic
    path('<int:topic_id>/<slug:topic_slug>', views.topic_detail_view, name='topic_detail'),
    path('<int:subject_id>/topic/add', views.topic_add_view, name='topic_add'),
    path('topic/update/<int:topic_id>', views.topic_update_view, name='topic_update'),
    path('<int:topic_id>/topic_delete/', views.topic_delete, name='topic_delete'),

    # Question
    path('<int:topic_id>/question/', views.question_add_view, name='question_add'),
    path('<int:topic_id>/question/update/<int:question_id>', views.question_update_view, name='question_update'),
    path('<int:topic_id>/question/delete/<int:question_id>', views.question_delete_view, name='question_delete'),
]
