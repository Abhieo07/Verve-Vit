from django.db import models
import uuid

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=100)
    profile_img = models.ImageField(upload_to='profile_pic', default='default.png', blank=True)

    def __str__(self):
        return f'{self.name}'

class Guest(models.Model):
    guest_name = models.CharField(max_length=255)
    affiliation = models.CharField(max_length=255)
    profile_img = models.ImageField(upload_to='profile_pic', default='default.png', blank=True)

    def __str__(self):
        return f'{self.guest_name}'

class Event(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(blank=True, max_length=255)
    date = models.DateField()
    location = models.CharField(max_length=255)
    price = models.IntegerField(default=0, blank=True)
    description = models.TextField()
    participant_count = models.IntegerField(default=0)
    img = models.ImageField(upload_to='events_img', default='default.png', blank=True)
    vid = models.FileField(upload_to='events_video', default='default.mp4', blank=True)
    incharge = models.ForeignKey(Contact, on_delete=models.CASCADE)
    guest = models.ManyToManyField(
        Guest,
        related_name='events'  # Explicit reverse relationship name
    )

    def increment_participant_count(self):
        self.participant_count += 1
        self.save()

    def __str__(self):
        return f'{self.title}'

class Activities(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='activities')
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='activity/', blank=True)
    video = models.FileField(upload_to='activity/', blank=True)

    def __str__(self):
        return f'{self.title}'

class Testimonial(models.Model):
    author_name = models.CharField(max_length=255)
    author_role = models.CharField(max_length=255)
    content = models.TextField()
    profile_img = models.ImageField(upload_to='profile_pic', default='default.png', blank=True)

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

    def save(self, *args, **kwargs):
        is_new = self.pk is None  # Check if this is a new object
        super().save(*args, **kwargs)
        if is_new:
            self.event.increment_participant_count()

    def __str__(self):
        return f'{self.participant_id}'

