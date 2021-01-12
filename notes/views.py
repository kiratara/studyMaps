from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import QuestionForm, SubjectForm, TopicForm
from .models import Question, Subject, Topic


def topic_list(request, subject_slug=None):
    '''Define view for subject list
    If subject_slug exists then filter by that subject only
    '''
    subject = None
    subjects = Subject.objects.all()
    topics = Topic.objects.all()

    if subject_slug:
        if subject_slug == 'add-subject':
            add_subject(request)
        subject = get_object_or_404(Subject, slug=subject_slug)
        topics = Topic.objects.filter(subject=subject)

    context = {'subject': subject,
                'subjects': subjects,
                'topics': topics,
                'addSubject': 'add-subject'}

    return render(request,
                'notes/list.html',
                context)


def topic_detail(request, id, topic_slug):
    '''
    '''
    topic = get_object_or_404(Topic, id=id, slug=topic_slug)
    context = {'topic': topic}
    return render(request, 
                    'notes/detail.html',
                    context)


def add_subject(request):
    '''Hanldes adding new subject to the db
    Form submission
    '''
    if request.method == 'POST':
        # is user submitted the form with input data
        form = SubjectForm(request.POST)
        if form.is_valid():
            cleanData = form.cleaned_data
            newSubject = Subject(**cleanData)
            # print(f"\n\n clean data: {newSubject}\n\n")
            # try:
            newSubject.save()
            return redirect('/')
            # except:
            #     context = {'form':form, 'error':'error'}
            #     return render(request, 'notes/add_subject.html', context)
    else:
        # when user clicks on the `add subject` button to request for form
        form = SubjectForm()
    context = {'form': form}
    return render(request, 'notes/add_subject.html', context)


def add_topic(request):
    '''Handle topic post method
    '''
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            cleanData = form.cleaned_data
            newTopic = Topic(**cleanData)
            newTopic.save()
            return redirect('/')
    else:
        form = TopicForm()
    context = {'form': form}
    return render(request, 'notes/add_topic.html', context)

def add_question(request, topic_id):
    '''Handle GET/POST request for the question resource
    '''
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            cleanData = form.cleaned_data
            newQuestion = Question(title=cleanData['title'],
                                    topic=cleanData['topic'])
            newQuestion.save()
            return redirect('/')
    else:
        form = QuestionForm()
    context = {'form': form,
                'topic_id':topic_id}
    return render(request, 'notes/add_question.html', context)