from django.db import models

# Create your models here.
class MyCourse(models.Model):
    course_title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.description
