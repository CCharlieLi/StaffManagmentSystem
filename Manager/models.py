from django.db import models

# Create your models here.
class GroupName(models.Model):
	Name = models.CharField(max_length=20)
	GroupMaster = models.CharField(max_length=20,blank=True)

	def __str__(self):
		return self.Name
	class Meta:#organize meta data when read from db
		ordering = ['id']

class Notification(models.Model):
  Type = models.CharField(max_length=20)
  ToUser = models.CharField(max_length=20)
  Content = models.TextField(blank=True)
  class Meta:#organize meta data when read from db
    ordering = ['-id']

class Level(models.Model):
	Levelname = models.CharField(max_length=20)
	def __str__(self):
		return self.Levelname
	class Meta:#organize meta data when read from db
		ordering = ['id']

class Employee(models.Model):
	UserID = models.CharField(max_length=20)
	#basic information
	UserName = models.CharField(default="",max_length=20)
	Picture = models.ImageField(upload_to = 'head',null=True,blank=True)
	Levelname = models.ForeignKey(Level,null=True)
	GroupName = models.ForeignKey(GroupName,null=True)
	Tel = models.CharField(default="",max_length=11,null=True,blank=True)
	Email = models.EmailField(default="",null=True,blank=True)
	QQ = models.CharField(default="",max_length=20,null=True,blank=True)
	Other = models.TextField(null=True,blank=True)

	SalaryPoint = models.CharField(default="0",max_length=5,null=True,blank=True)
	Score = models.CharField(default="0",max_length=5,null=True,blank=True)
	def __str__(self):
		return self.UserID
	class Meta:#organize meta data when read from db
		ordering = ['id']

class Announcement(models.Model):
	Title = models.CharField(max_length=100)
	Publisher = models.ForeignKey(Employee,blank=True)
	Datetime = models.CharField(max_length=20)
	Content = models.TextField(blank=True)
	Namelist = models.TextField(default="",blank=True)
	def __str__(self):
		return self.Title
	class Meta:#organize meta data when read from db
		ordering = ['-id']


class Plan(models.Model):
	UserID = models.CharField(max_length=20)
	UserName = models.CharField(max_length=20,default="")
	Datetime = models.CharField(max_length=20)
	planlevel = models.CharField(default="person",max_length=20)
	plantitle = models.CharField(max_length=100,default="")
	Content = models.TextField(blank=True)
	Progress = models.CharField(max_length=20,null=True,blank=True)
	Estimate = models.CharField(max_length=20,null=True,blank=True)
	Advertisement = models.TextField(default="",blank=True)
	def __str__(self):
		return self.userID
	class Meta:#organize meta data when read from db
		ordering = ['-id']

class Calendar(models.Model):
	UserID = models.CharField(max_length=20,default="charlie")
	title = models.CharField(max_length=100,default="My Event")
	content = models.TextField(null=True,blank=True)
	start = models.CharField(max_length=100,null=True,blank=True)
	end = models.CharField(max_length=100,null=True,blank=True)
	allday = models.BooleanField(default=False)

	def __str__(self):
		return self.userID
	class Meta:#organize meta data when read from db
		ordering = ['id']

class Salary(models.Model):
	UserID = models.CharField(max_length=20)
	Score = models.CharField(default="0",max_length=5,null=True,blank=True)
	SalaryPoint = models.CharField(default="0",max_length=5,null=True,blank=True)
	Event = models.CharField(max_length=400)
	def __str__(self):
		return self.userID
	class Meta:#organize meta data when read from db
		ordering = ['-id']

class Salarybase(models.Model):
	Base = models.CharField(default="0",max_length=20,null=True,blank=True)
	Publisher = models.CharField(max_length=20,default="")
	Datetime = models.CharField(max_length=20,default="")
	def __str__(self):
		return self.Base
	class Meta:#organize meta data when read from db
		ordering = ['-id']
		