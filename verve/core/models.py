from django.db import models
import uuid

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class Event(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    location = models.CharField(max_length=255)
    price = models.IntegerField(default=0,blank=True)
    description = models.TextField()
    img = models.ImageField(upload_to='', default='default.png', blank=True)
    vid = models.FileField(upload_to='', default='default.mp4', blank=True)
    incharge = models.ForeignKey(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

class Highlight(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='highlights/', blank=True)
    video = models.FileField(upload_to='highlights/', blank=True)

    def __str__(self):
        return f'{self.title}'

class Testimonial(models.Model):
    author_name = models.CharField(max_length=255)
    author_role = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return f'{self.author_name}'

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')
    video = models.FileField(upload_to='gallery/', blank=True)
    year = models.DateField()

    def __str__(self):
        return f'{self.year}'

class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    participant_name = models.CharField(max_length=255)
    participant_id = models.UUIDField(default=uuid.uuid4, unique=True)
    college = models.CharField(max_length=255, default="VIT Mumbai")
    gender = models.CharField(max_length=10)
    department = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.participant_id}'

class Guest(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=255)
    affiliation = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.guest_name} + {self.event}'
