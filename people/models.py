from django.db import models

class Label(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    labels = models.ManyToManyField('Label', related_name='people', blank=True)

    def __str__(self):
        return self.name

class Link(models.Model):
    person = models.ForeignKey(Person, related_name='links', on_delete=models.CASCADE)
    url = models.URLField()
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.description or 'No description'} - {self.url}"

