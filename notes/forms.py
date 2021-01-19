from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Question, Subject, Topic


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


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username',)
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
