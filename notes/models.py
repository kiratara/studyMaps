from django.db import models
from django.urls import reverse


class Subject(models.Model):
    '''Define a Subject model
    Subject 
    '''

    name = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated  = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200,
                            unique=True) # creation of index by unique

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"Subject: {self.name}"

    def get_absolute_url(self):
        '''return url for the subject object'''
        val = reverse('notes:product_list_by_subject',
                       args=[self.slug])
        print (f"\n absolute url for subject is: {val}")
        return val


class Topic(models.Model):
    '''Define Topic entity
    Each subject will have many topics that will then contain the notes
    '''

    CONFIDENCE_CHOICES = [
        ('0', 'Nada'), 
        ('1', 'So-so'),
        ('2', 'I am Good'),
        ('4', 'Got this!')]
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # subject-to-topic is one-to-many relationship. One subject will have many topics
    subject = models.ForeignKey(Subject, 
                                on_delete=models.CASCADE, 
                                related_name='topics')
    slug = models.SlugField(max_length=200, db_index=True)
    confidence = models.CharField(max_length=10, choices=CONFIDENCE_CHOICES)
    notes = models.TextField(blank=True)

    def __str__(self):
        '''String representation of topic'''
        return self.title

    def get_absolute_url(self):
        ''' return url of the object'''
        return reverse('notes:topic_detail',
                    args=[self.id, self.slug])


class Question(models.Model):
    '''Define questions class 
    '''
    title = models.TextField(blank=True)
    resolved = models.BooleanField(default=False)
    # slug = models.SlugField(max_length=200, db_index=True)
    topic = models.ForeignKey(Topic, 
                            on_delete=models.CASCADE,
                            related_name='question')

    # def get_absolute_url(self):
    #     ''' return url of the object'''
    #     return reverse('question:question_detail',
    #                 args=[self.id, self.slug])

    def __str__(self):
        '''String representation of Question'''
        return self.title
