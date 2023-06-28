from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from froala_editor.fields import FroalaField
from .helpers import *

# Create your models here.
class User(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.EmailField()
	mobile=models.PositiveIntegerField()
	profile_pic=models.ImageField(upload_to="profile_pic/",default="static 'img/user_default.jpg' ")
	password=models.CharField(max_length=100)
	usertype=models.CharField(max_length=100,default='user')

	def __str__(self):
		return self.fname+" - "+self.lname

class Workout(models.Model):
	trainer=models.ForeignKey(User,on_delete=models.CASCADE)
	w_type=models.CharField(max_length=100)
	w_name=models.CharField(max_length=100)
	w_description=models.TextField(default='null')
	w_difficulty=models.CharField(max_length=50)
	w_muscles_targeted=models.CharField(max_length=100)
	w_gif=models.ImageField(upload_to='workout_gifs/')

	def __str__(self):
		return self.trainer.fname+' - '+self.w_name

class BlogModel(models.Model):
	# trainer=models.ForeignKey(User,on_delete=models.CASCADE)
	title = models.CharField(max_length=1000)
	content = FroalaField()
	slug = models.SlugField(max_length=1000, null=True, blank=True)
	user = models.ForeignKey(User, blank=True, null=True,
							on_delete=models.CASCADE)
	image = models.ImageField(upload_to='blog')
	created_at = models.DateTimeField(auto_now_add=True)
	upload_to = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.user.fname+ ' - ' +self.title


	def save(self, *args, **kwargs):
		self.slug = generate_slug(self.title)
		super(BlogModel, self).save(*args, **kwargs)

class Exercise(models.Model):
	trainer=models.ForeignKey(User,on_delete=models.CASCADE)
	EXERCISE_TYPES= (
        ('barbell_workout', 'Barbell Workout'),
        ('dumbbell_workout', 'Dumbbell Workout'),
        ('band_workout', 'Band Workout'),
        ('cable_workout', 'Cable Workout'),
        ('bodyweight_workout', 'Bodyweight Workout'),
        ('kettlebell_workout', 'Kettlebell Workout'),
    	)
	e_name=models.CharField(max_length=100)
	Equipment= (
        ('Dumbbells', 'Dumbbells'),
        ('Kettlebells', 'Kettlebells'),
        ('Bands', 'Bands'),
        ('Bodyweight', 'Bodyweight'),
        ('Cables', 'Cables'),
    )
	EXERCISE_Difficulty= (
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    )
	e_type = models.CharField(default='dumbbell_workout',max_length=30, choices=EXERCISE_TYPES)
	equipment = models.CharField(default='Bodyweight',max_length=20, choices=Equipment)
	e_difficulty = models.CharField(default='Beginner',max_length=20, choices=EXERCISE_Difficulty)
	e_image=models.ImageField(upload_to='exercise_images/')
	# workout=Workout.objects.all()
	e_list=models.ManyToManyField(Workout)
	

	def __str__(self):
		return self.trainer.fname+" - "+self.e_name

