import os
import random
from django.db import models
from datetime import date

# Create your models here.
def upload_image_path(instance, filename):
    new_filename = random.randint(1, 9996666666)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(
        new_filename=new_filename, ext=ext)
    return "meals/{new_filename}/{final_filename}".format(
        new_filename=new_filename,
        final_filename=final_filename
    )
    
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, 
class Info(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=14)
    age=models.IntegerField()
    city=models.CharField(max_length=100)
    degre=models.CharField(max_length=100)
    def my_age(self):
        return date.today().year-2001
class Skills(models.Model):
    skill=models.CharField(max_length=100)
    perce=models.FloatField()

class Portfolio(models.Model):
    FILTER_CHOICES = [
    ('web', 'web'),
    ('rest', 'rest'),
    ('design', 'design'),
]
    titel=models.CharField(max_length=220)
    category=models.CharField(max_length=100)
    client=models.CharField(max_length=100)
    project_date=models.DateTimeField()
    project_url=models.CharField(max_length=300)
    description=models.TextField()
    category_filter=models.CharField(max_length=100,choices=FILTER_CHOICES,default='web')
    image=models.ImageField(upload_to=upload_image_path)

    def __str__(self):
        return self.titel
    
class Images(models.Model):
    portfolio=models.ForeignKey(Portfolio,on_delete=models.CASCADE)
    image=models.ImageField(upload_to=upload_image_path)
    def get_category(self):
        return self.portfolio.category_filter
    def get_portfolio_id(self):
        return self.portfolio.id
    def __str__(self):
        return self.portfolio.titel
class Service(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    bootstrap_icon=models.CharField(max_length=100)   

class Message(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=200)
    message=models.TextField()   