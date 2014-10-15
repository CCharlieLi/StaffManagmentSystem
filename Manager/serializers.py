from django.contrib.auth.models import User, Group
from rest_framework import serializers
from Manager.models import *


class UserAuthSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','url','username','password', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GroupName
        fields = ('id','url','Name','GroupMaster')


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ('id','url','UserID','UserName','Picture','GroupName','Levelname','SalaryPoint','Score','Tel','Email','QQ','Other')

class AnnouncementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Announcement
        fields = ('id','url','Title','Publisher','Datetime','Content')

class LevelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Level
        fields = ('id','url','Levelname')

class CalendarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Calendar
        fields = ('id','UserID','title','start','end','content','allday')

class SalarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Salary
        fields = ('id','UserID','Score','Event')
