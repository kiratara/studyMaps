from django.contrib import admin
from .models import Subject, Topic, Question


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    '''
    Register Subject model with the admin.
    Define the view for Subject. 
    '''
    list_display = ['name', 'slug']
    # automatically set using the value of other fields, slug with name
    prepopulated_fields = {'slug': ('name',)} 


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    '''
    Register Topic model with the admin.
    Define the view for Topic. 
    '''
    list_display = ['subject', 'title', 'confidence', 'slug']
    prepopulated_fields = {'slug': ('title',)} 


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    '''
    Register Question model with the admin.
    Define the view for Question. 
    '''
    list_display = ['title', 'topic', 'slug']
    prepopulated_fields = {'slug': ('title',)} 
