from django.forms import ModelForm
from .models import Subject, Topic, Question


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
        fields = ['title', 'topic']