from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Question, Subject, Topic
from django import forms


class LoginForm(forms.Form):
    '''Login form used by users to login to be
    authenticated
    '''
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class SubjectForm(ModelForm):
    '''
    Form to add a new subject.
    User will be able to add title only.
    dates added automatically.
    '''
    class Meta:
        model = Subject
        fields = ['name']


class TopicForm(ModelForm):
    '''Form for model Topic
    Used to add new Topic
    '''
    class Meta:
        model = Topic
        fields = ['title', 'subject', 'confidence', 'notes']


class QuestionForm(ModelForm):
    '''Form for model Question
    '''
    class Meta:
        model = Question
        fields = ['title', 'topic', 'resolved']
