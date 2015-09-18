from django.db import models

# Create your models here.
class News(models.Model):
	Title = models.CharField(max_length=100)
	Publsh_Date = models.DateField(auto_now=True)
	Image = models.ImageField('Image(700x240)',upload_to = 'website/images',null=True,blank=True)
	Content = models.TextField(null=True,blank=True)
	def __str__(self):
		return self.Title
	class Meta:
		ordering = ['-id']

class Announce(models.Model):
	Title = models.CharField(max_length=100)
	Publsh_Date = models.DateField(auto_now=True)
	Image = models.ImageField('Image(700x240)',upload_to = 'website/images',null=True,blank=True)
	Content = models.TextField(null=True,blank=True)
	def __str__(self):
		return self.Title
	class Meta:
		ordering = ['-id']

class Policy(models.Model):
	Name = models.CharField(max_length=100)
	File = models.FileField(upload_to = 'website/file',null=True,blank=True)
	Publsh_Date = models.DateField(auto_now=True)
	keyword = models.CharField(max_length=100,null=True,blank=True)
	def __str__(self):
		return self.Name
	class Meta:
		ordering = ['-id']

class Magazine(models.Model):
	Name = models.CharField(max_length=100)
	File = models.FileField(upload_to = 'website/file',null=True,blank=True)
	Publsh_Date = models.DateField(auto_now=True)
	keyword = models.CharField(max_length=100,null=True,blank=True)
	def __str__(self):
		return self.Name
	class Meta:
		ordering = ['-id']

class PeopleType(models.Model):  #Greatleader,Member,College,Company
	Name = models.CharField("Type",max_length=100)
	def __str__(self):
		return self.Name
	class Meta:
		ordering = ['-id']


class Partnership(models.Model):
	Name = models.CharField(max_length=100)
	Image = models.ImageField('Image(700x240)',upload_to = 'website/images',null=True,blank=True)
	Link = models.CharField(max_length=255,null=True,blank=True)
	PeopleType = models.ForeignKey(PeopleType)
	def __str__(self):
		return self.Name
	class Meta:
		ordering = ['id']

class Group(models.Model):
	Name = models.CharField(max_length=100,default="")
	def __str__(self):
		return self.Name
	class Meta:
		ordering = ['id']

class People(models.Model):
	Name = models.CharField(max_length=100)
	Level = models.CharField(max_length=200)
	PeopleType = models.ForeignKey(PeopleType)
	GroupName = models.ForeignKey(Group,null=True,blank=True)
	Content = models.TextField(null=True,blank=True)
	Image = models.ImageField('Image(220x220/220x140)',upload_to = 'website/images',null=True,blank=True)
	def __str__(self):
		return self.Name
	class Meta:
		ordering = ['id']
