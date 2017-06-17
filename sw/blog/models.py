import os
from django import forms
from django.core.urlresolvers import reverse
from django.conf import settings
from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=100)
	content= models.TextField()
	photo = models.ImageField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering =['-id']

	def __str__(self):
		return self.title
# This is for free bulletin board.

class Comment(models.Model):
	post = models.ForeignKey(Post)
	author = models.ForeignKey(settings.AUTH_USER_MODEL)
	message = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering =['-id']

	def get_edit_url(self):
		return reverse('blog:comment_edit', args=[self.post.pk, self.pk])

	def get_delete_url(self):
		return reverse('blog:comment_delete', args=[self.post.pk, self.pk])
# This is for the reply of free bulletin board.

class Question(models.Model):
    title = models.CharField(max_length=30)
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
    	ordering=['id']
# This is for Q&A board

class question_Comment(models.Model):
	question = models.ForeignKey(Question)
	author = models.ForeignKey(settings.AUTH_USER_MODEL)
	message = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def get_question_edit_url(self):
		return reverse('blog:question_comment_edit', args=[self.question.pk, self.pk])

	def get_question_delete_url(self):
		return reverse('blog:question_comment_delete', args=[self.question.pk, self.pk])

# This is for the reply of Q&A board

class Call(models.Model):
    title = models.CharField(max_length=30)
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
    	ordering=['id']

# This is for request board

class call_Comment(models.Model):
	call = models.ForeignKey(Call)
	author = models.ForeignKey(settings.AUTH_USER_MODEL)
	message = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def get_call_edit_url(self):
		return reverse('blog:call_comment_edit', args=[self.call.pk, self.pk])

	def get_call_delete_url(self):
		return reverse('blog:call_comment_delete', args=[self.call.pk, self.pk])
# This is for the reply of request board

class Upload(models.Model):
	photo = models.FileField()

	class Meta:
		ordering=['-id']
# This is for implementing uploading pixel file

class Search(models.Model):
	title = models.CharField(max_length=30)
	font_file = models.CharField(max_length = 100)

class Font(models.Model):
	title = models.CharField(max_length=100)
	font = models.FileField()

	class Meta:
		ordering=['-id']

 

# Create your models here.
