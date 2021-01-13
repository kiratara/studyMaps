from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView

from .forms import QuestionForm, SubjectForm, TopicForm
from .models import Question, Subject, Topic


def topic_list_view(request, subject_slug=None):
    '''Define view for subject list
    If subject_slug exists then filter by that subject only
    '''
    subject = None
    subjects = Subject.objects.all()
    topics = Topic.objects.all()

    if subject_slug:
        subject = get_object_or_404(Subject, slug=subject_slug)
        topics = Topic.objects.filter(subject=subject)

    context = {'subject': subject,
                'subjects': subjects,
                'topics': topics,
                'addSubject': 'add-subject'}

    return render(request,
                'notes/list.html',
                context)


## subject ##
def subject_add_view(request):
    '''View to handle adding new subject to the db
    Get - returns empty subject add form
    Post - add a new subject instance to the db
    '''
    template_name = 'notes/subject_form.html'
    existing_subject = None
    message = "Let's add a new subject"
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            new_subject = Subject(**clean_data)
            new_subject.save()
            return HttpResponseRedirect('/')
    else:
        form = SubjectForm()
    context = {'form': form,
                'message': message}
    return render(request, template_name, context)     
       
def subject_update_view(request, subject_id):
    '''View to handle update of subject model
    Get method returns form in previous data.
    Post updates the values of the existing object.
    '''
    template_name = 'notes/subject_form.html'
    existing_subject = None
    message = "Update your subject"
    if request.method == 'POST':
        if subject_id:
            existing_subject = Subject.objects.get(id=subject_id)
        form = SubjectForm(request.POST, instance=existing_subject)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        existing_subject = Subject.objects.get(id=subject_id)
    form = SubjectForm(instance=existing_subject)
    context = {'form': form,
                'message': message}
    return render(request, template_name, context)   

def subject_delete_view(request, subject_id):
    '''Delete a subject instance from the db
    '''
    instance = get_object_or_404(Subject, id=subject_id)
    instance.delete()
    return redirect('/')

## topic ##
def topic_detail_view(request, topic_id, topic_slug):
    '''View to handle topic detail
    Returns single topic item with its details, including questions
    '''
    topic = get_object_or_404(Topic, id=topic_id, slug=topic_slug)
    context = {'topic': topic, 'subject_slug':topic.subject.get_absolute_url()}
    return render(request, 
                    'notes/detail.html',
                    context)

def topic_add_view(request, subject_id):
    '''
        Handles GET and POST request for new Topic
        Get - return empty topic add form
        POST - Add/Updates Topic  
    '''
    print ("Greetings from topic add view")
    subject = get_object_or_404(Subject, id=subject_id)
    template_name = 'notes/topic_form.html'
    existing_subject = None
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            new_topic = Topic(**clean_data)
            new_topic.save()
            topic_url = new_topic.get_absolute_url()
            return HttpResponseRedirect(topic_url)
    else:
        form = TopicForm(initial={'subject':subject})
    context = {'form': form}
    return render(request, template_name, context)     
       
def topic_update_view(request, topic_id):
    '''updates topic
    GET - returns topic form with previous data filled
    POST - updatse the existing instance with  the new data in the db
    '''
    template_name = 'notes/topic_form.html'
    existing_topic = None
    if request.method == 'POST':
        if topic_id:
            existing_topic = Topic.objects.get(id=topic_id)
        form = TopicForm(request.POST, instance=existing_topic)
        if form.is_valid():
            form.save()
            topic_url = existing_topic.get_absolute_url()
            return HttpResponseRedirect(topic_url)
    else:
        existing_topic = Topic.objects.get(id=topic_id)
    form = TopicForm(instance=existing_topic)
    context = {'form': form}
    return render(request, template_name, context)   

def topic_delete(request, topic_id):
    '''Delete a topic instance with given id
    '''
    topic = get_object_or_404(Topic, id=topic_id)
    subject = topic.subject
    subject_url = subject.get_absolute_url()
    topic.delete()
    return redirect(subject_url)

## Question ###
def question_add_view(request, topic_id):
    '''
        Handles GET and POST request for new Topic
        Get - return empty topic add form
        POST - Add/Updates Topic  
    '''
    template_name = "notes/question_form.html"

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            new_question = Question(title=clean_data['title'],
                                    topic=clean_data['topic'])
            new_question.save()
            url = new_question.get_absolute_url()
            return redirect(new_question)
    else:
        topic = get_object_or_404(Topic, id=topic_id)
        form = QuestionForm(initial={'topic':topic})
    context = {'form': form,
                'topic_id':topic_id}
    return render(request, template_name, context)    
       
def question_update_view(request, topic_id, question_id):
    '''update question instance with given id
    GET - return form with fields filled with existing data to be updated
    POST - update the existing instance with the new data
    '''
    template_name = 'notes/question_form.html'
    existing_question = None

    if request.method == 'POST':
        if question_id:
            existing_question = Question.objects.get(id=question_id)
        form = QuestionForm(request.POST, instance=existing_question)
        if form.is_valid():
            form.save()
            question_url = existing_question.get_absolute_url()
            return HttpResponseRedirect(question_url)
    else:
        existing_question = Question.objects.get(id=question_id)
    form = QuestionForm(instance=existing_question)
    context = {'form': form}
    return render(request, template_name, context)   


def question_delete_view(request, topic_id,  question_id):
    '''Delete a question resource
    '''
    question = get_object_or_404(Question, id=question_id)
    topic = question.topic
    topic_url = topic.get_absolute_url()
    question.delete()
    return redirect(topic_url)



## class based views ##
# class TopicDetailView(DetailView):
#     ''' '''
#     model = Topic
#     template_name = 'notes/detail.html'

#     def get_context_data(self, **kwargs):
#         '''Returns context data for displaying the object.'''
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         topic_id = kwargs['id']
#         topic_slug = kwargs['topic_slug']
#         # print (f"Topic SLUGS: {}")
#         topic = get_object_or_404(Topic, id=topic_id)
#         subject_slug = topic.subject.get_absolute_url()

#         # set context variables
#         context['topic'] = topic
#         context['subject_slug'] = subject_slug
    
#         return context


# class HomeView(ListView):
#     model = Topic
#     template_name = 'notes/list.html'

#     def get_context_data(self, **kwargs):
#         '''Returns context data for displaying the object.'''
#         # Call the base implementation first to get a context
#         subject = None
#         context = super().get_context_data(**kwargs)
#         topics = Topic.objects.all()
#         context['subjects'] = Subject.objects.all()
#         subject_slug = self.kwargs.get('subject_slug')
#         if subject_slug:
#             subject = get_object_or_404(Subject, slug=subject_slug)
#             context['subject'] = subject
#             context['topics'] = Topic.objects.filter(subject=subject)
#         else:
#             context['topics'] = topics

#         return context


# class TopicFormView(View):
#     '''
#     '''
#     form_class = TopicForm
#     template_name = 'notes/topic_form.html'
#     def get(self, request, *args, **kwargs):
#         '''
#         '''
#         print (f"\n From TopicFormView \n  args: {args} \n  kwargs: {kwargs}")
#         subject = get_object_or_404(Subject, id=kwargs['subject_id'])
#         form = TopicForm(initial={'subject':subject})
#         context = {'form': form, "subject": subject}
#         return render(request, self.template_name, context)

#     def post(self, request, *args, **kwargs):
#         '''
#         '''
#         form = TopicForm(request.POST)
#         if form.is_valid():
#             clean_data = form.cleaned_data
#             newTopic = Topic(**clean_data)
#             newTopic.save()
#             topic_url = newTopic.get_absolute_url()
#             return HttpResponseRedirect(topic_url)


# class QuestionFormView(View):
#     '''Class Based view to handle GET-ing the questionForm
#     and POST-ing the the question when user `adds` it. 
#     '''
#     form_class = QuestionForm
#     # initial = {'key':'value'}
#     template_name = 'notes/question_form.html'

#     def get(self, request, *args, **kwargs):
#         '''GET Question form when user clicks on
#         `Add Question` button
#         '''
#         form = self.form_class()
#         context = {'form':form}
#         return render(request, self.template_name, context)

#     def post(self, request, *args, **kwargs):
#         '''Receive the POST data from a Question Form, validate
#         the data and add the new Question model object to the database.
#         '''
#         # print (f"This is value of *args from post in questionFORMview: {kwargs}")
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             clean_data = form.cleaned_data
#             title = clean_data['title']
#             topic = clean_data['topic']
#             topic_url = topic.get_absolute_url()
#             newQuestion = Question(title=title,
#                                     topic=topic)
#             newQuestion.save()
#             return HttpResponseRedirect(topic_url)
    

# class SubjectFormView(View):
#     '''
#     '''
#     form_class = TopicForm
#     template_name = 'notes/subject_form.html'
#     def get(self, request, *args, **kwargs):
#         '''
#         '''
#         existing_subject = None
#         print (f"From SubjectFormView GET: {request} \n {kwargs}")
#         subject_id = kwargs.get('subject_id')
#         if subject_id:
#             existing_subject = Subject.objects.get(id=subject_id)
#         form = SubjectForm(instance=existing_subject)
#         context = {'form': form}
#         return render(request, self.template_name, context)

#     def post(self, request, *args, **kwargs):
#         '''
#         '''
#         existing_subject = None
#         subject_id = kwargs.get('subject_id')
#         if subject_id:
#             existing_subject = Subject.objects.get(id=subject_id)
#         form = SubjectForm(request.POST, instance=existing_subject)
#         if form.is_valid():
#             clean_data = form.cleaned_data
#             newSubject = Subject(**clean_data)
#             newSubject.save()
#             return HttpResponseRedirect('/')

