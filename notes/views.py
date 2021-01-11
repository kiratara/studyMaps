from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Subject, Topic, Question


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

    return render(request,
                'notes/list.html',
                {'subject': subject,
                'subjects': subjects,
                'topics': topics})

def topic_detail(request, id, topic_slug):
    '''
    '''
    topic = get_object_or_404(Topic, id=id, slug=topic_slug)

    return render(request, 
                    'notes/detail.html',
                    {
                        'topic': topic
                    })

def add_subject(request):
    '''Hanldes adding new subject
    Form submission
    '''
    return render('notes/add_subject.html')