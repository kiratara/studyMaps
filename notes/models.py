from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Subject(models.Model):
    '''Define a Subject model
    Subject 
    '''
    name = models.CharField(max_length=250, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    updated  = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200,
                            unique=True) # creation of index by unique
    owner = models.ForeignKey(User, 
                                on_delete=models.CASCADE, 
                                related_name='subjects')
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        '''return url for the subject object'''
        val = reverse('notes:topic_list_by_subject',
                       args=[self.slug])
        return val

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value)
        super().save(*args, **kwargs)

class Topic(models.Model):
    '''Define Topic entity
    Each subject will have many topics that will then contain the notes
    '''

    CONFIDENCE_CHOICES = [
        ('0', 'Nada'), 
        ('1', 'So-so'),
        ('2', 'I am Good'),
        ('4', 'Got this!')]
    title = models.CharField(max_length=250, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # subject-to-topic is one-to-many relationship. One subject will have many topics
    subject = models.ForeignKey(Subject, 
                                on_delete=models.CASCADE, 
                                related_name='topics')
    slug = models.SlugField(max_length=200, unique=True)
    confidence = models.CharField(max_length=10, choices=CONFIDENCE_CHOICES)
    notes = models.TextField(blank=True, db_index=True)

    def __str__(self):
        '''String representation of topic'''
        return self.title

    def get_absolute_url(self):
        ''' return url of the object'''
        return reverse('notes:topic_detail',
                    args=[self.id, self.slug])

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value)
        super().save(*args, **kwargs)


class Question(models.Model):
    '''Define questions class 
    '''
    title = models.CharField(max_length=150, db_index=True)
    resolved = models.BooleanField(default=False)
    slug = models.SlugField(max_length=200, unique=True)
    topic = models.ForeignKey(Topic, 
                            on_delete=models.CASCADE,
                            related_name='question')

    def get_absolute_url(self):
        ''' return url of the object'''
        return reverse('notes:topic_detail',
                    args=[self.topic.id, self.topic.slug])

    def __str__(self):
        '''String representation of Question'''
        return self.title

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value)
        super().save(*args, **kwargs)
