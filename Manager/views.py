#!/usr/bin/python
#-*-coding:utf-8-*-
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.models import User, Group
from django.contrib import auth
from django.core.paginator import Paginator,InvalidPage,EmptyPage
from django.contrib import messages
from PIL import Image
from rest_framework import viewsets

from Manager.models import *
from Manager.serializers import *
import time


#################  REST viewset  ######################
class UserAuthViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserAuthSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = GroupName.objects.all()
    serializer_class = GroupSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class CalendarViewSet(viewsets.ModelViewSet):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer

class SalaryViewSet(viewsets.ModelViewSet):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer

class SalaryBaseViewSet(viewsets.ModelViewSet):
    queryset = Salarybase.objects.all()
    serializer_class = SalaryBaseSerializer
###############################################

#################  login logout #####################
# Create your views here.
def login(request):
    title = "Login"
    #auth.logout(request)
    if request.method == "POST":
        u_username = request.POST['username']
        u_password = request.POST['password']
        user = auth.authenticate(username=u_username, password=u_password)

        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect("index")
        else:
            # Show an error massage
            messages.add_message(request, messages.ERROR, 'Account or Password wrong!')
            return HttpResponseRedirect('login',locals())
        #if form.is_valid():

    else:
        #username = u_username
        if request.user.is_authenticated():
            return HttpResponseRedirect("index")

    return render_to_response('login.html',locals(),context_instance = RequestContext(request))

def logout(request):
    auth.logout(request)

    title = "Login"
    return render_to_response('login.html',locals(),context_instance = RequestContext(request))

######################################################
def pageGenerator(request,objs):
    paginator = Paginator(objs,5)
    try:
        page = int(request.GET.get("page",'1'))
    except ValueError:
        page = 1
    try:
        objs = paginator.page(page)
    except (InvalidPage,EmptyPage):
        objs = paginator.page(paginator.num_pages)
    return objs

@login_required
def changepassword(request):
    title = "Change Password"
    username = request.user
    
    notifications = Notification.objects.filter(ToUser=username)

    if request.method == "POST":
        user = auth.authenticate(username=username, password=request.POST['oldpass'])
        if user is not None and user.is_active:
            newpassword = request.POST['newpass']
            print(user.set_password(newpassword))
            user.save()
        return HttpResponseRedirect('changepassword',locals())

    return render_to_response('profile/change-password.html',locals(),context_instance = RequestContext(request))



#########################   index   ######################
@login_required
def index(request):
    username = request.user
    title = "Index"

    groups = GroupName.objects.all()
    notifications = Notification.objects.filter(ToUser=username)

    announces = Announcement.objects.all()
    if announces.count() > 0:
        first_announce = announces[0]
        Namelist = first_announce.Namelist.split(",")[:-1]

    announces = pageGenerator(request,announces)

    if 'annid' in request.GET:
        first_announce = Announcement.objects.get(id=int(request.GET.get("annid",'1')))
        Namelist = first_announce.Namelist.split(",")[:-1]

    return render_to_response('index.html',locals(),context_instance = RequestContext(request))

@login_required
@permission_required('Manager.add_announcement')
def addannounce(request):
    title = "Announcement"
    username = request.user
    
    #binding
    groups = GroupName.objects.all()
    notifications = Notification.objects.filter(ToUser=username)

    if request.method == "POST":
        u_userid = username
        u_username = Employee.objects.get(UserID=username)
        u_datetime = request.POST['datetime']
        u_title = request.POST['title']
        u_content = request.POST['content']

        #############################
        namelist = ""
        for each in Employee.objects.all():
            namelist = namelist + each.UserName + ","

        ann = Announcement(Publisher=u_username,Title=u_title,
            Datetime=u_datetime,Content=u_content,Namelist=namelist)
        ann.save()

        #success message
        messages.add_message(request, messages.SUCCESS, 'Publish announcement successfully!')
        
        #Notification
        for each in Employee.objects.all():
            notification = Notification(Type="Announcement",ToUser=each.UserID,Content="/manage/index?annid="+str(ann.id))
            notification.save()

        return HttpResponseRedirect('index',locals())

    return render_to_response('Announce/new-announce.html',locals(),context_instance = RequestContext(request))

@login_required
@permission_required('Manager.change_announcement')
def editannounce(request):
    title = "Announcement"
    username = request.user

    groups = GroupName.objects.all()
    notifications = Notification.objects.filter(ToUser=username)

    if request.method == "POST":
        u_id = request.POST['id']
        u_datetime = request.POST['datetime']
        u_title = request.POST['title']
        u_content = request.POST['content']

        #############################

        ann = Announcement.objects.get(id=u_id)
        ann.Datetime = u_datetime
        ann.Title = u_title
        ann.Content = u_content
        ann.save()

        messages.add_message(request, messages.SUCCESS, 'Edit announcement successfully!')
        return HttpResponseRedirect('index',locals())

    if 'annid' in request.GET:
        announce = Announcement.objects.get(id=int(request.GET.get("annid",'1')))
        return render_to_response('Announce/edit-announce.html',locals(),context_instance = RequestContext(request))
    else:
        return HttpResponseRedirect('index',locals())

@login_required
@permission_required('Manager.delete_announcement')
def delannounce(request):
    if 'annid' in request.GET:
        Announcement.objects.get(id=int(request.GET.get("annid",'1'))).delete()
        messages.add_message(request, messages.SUCCESS, 'Delete announcement successfully!')
    return HttpResponseRedirect('index',locals())

@login_required
def readannounce(request):
    username = request.user

    if 'annid' in request.GET:
        announce = Announcement.objects.get(id=int(request.GET.get("annid",'1')))
        namelist = ""
        for each in announce.Namelist.split(",")[:-1]:
            if each == Employee.objects.get(UserID=username).UserName:
                pass
            else:
                namelist = namelist + each + ","

        announce.Namelist = namelist
        announce.save()
        messages.add_message(request, messages.INFO, 'You have read the announcement.')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

##########################################################

######################   notification ####################
@login_required
def clicknotification(request):
  url ="/"
  if 'notifid' in request.GET:
    nid = request.GET.get("notifid",'1')
    notif = Notification.objects.get(id=nid)
    url = notif.Content
    notif.delete()
  return HttpResponseRedirect(url)

##########################################################

######################   personal profile ################
@login_required
def profilepage(request):
    title = "Profile"
    username = request.user

    notifications = Notification.objects.filter(ToUser=username)

    user = Employee.objects.get(UserID=username)

    return render_to_response('profile/personal-info.html',locals(),context_instance = RequestContext(request))

@login_required
def profileedit(request):
    title = "Profile"
    username = request.user

    notifications = Notification.objects.filter(ToUser=username)

    if request.method == "POST" and username.username == request.POST['userid']:
        user = Employee.objects.get(UserID=request.POST['userid'])

        user.UserName = request.POST['username']
        user.Tel = request.POST['tel']
        user.Email = request.POST['email']
        user.Other = request.POST['introduce']
        user.QQ = request.POST['qq']

        try:
            reqfile = request.FILES["head"]
            img = Image.open(reqfile)
            img.thumbnail((167,179),Image.ANTIALIAS)
            img.save("Skyrover/static/img/head/"+username.username+".png","png")#保存图片

            user.Picture = username.username + ".png"
        except Exception as e:
            pass
        
        user.save()
        messages.add_message(request, messages.SUCCESS, 'Edit profile successfully!')
        return HttpResponseRedirect('profileedit',locals())

    user = Employee.objects.get(UserID=username)

    return render_to_response('profile/personal-edit.html',locals(),context_instance = RequestContext(request))

@login_required
def uploadhead(request):


    return render_to_response('profile/personal-edit.html',locals(),context_instance = RequestContext(request))



##########################################################

######################   calendar   ######################

@login_required
def calendar(request):
    username = request.user
    title = "Calendar"

    return render_to_response('calendar.html',locals(),context_instance = RequestContext(request))


###########################  User  #########################
@login_required
def userlist(request):
    title = "User"
    username = request.user

    groups = GroupName.objects.all()
    notifications = Notification.objects.filter(ToUser=username)

    if 'SearchName' in request.GET:
        users = Employee.objects.filter(UserID__icontains=request.GET.get("SearchName",'1'))
    else:
        users = Employee.objects.all()

    users = pageGenerator(request,users)

    return render_to_response('user/user-list.html',locals(),context_instance = RequestContext(request))


@login_required
@permission_required('Manager.add_employee')
def adduser(request):
    title = "User"
    username = request.user

    groups = GroupName.objects.all()
    notifications = Notification.objects.filter(ToUser=username)

    if request.method == "POST":
        u_userid = request.POST['userid']
        u_username = request.POST['username']
        u_groupname = request.POST['groupname']
        u_levelname = request.POST['levelname']
        u_tel = request.POST['tel']
        u_email = request.POST['email']
        u_introduce = request.POST['introduce']
        u_qq = request.POST['qq']
        u_password = request.POST['password']
        u_confpassword = request.POST['confpassword']
        u_gender = request.POST['gender']

        #############################
        employee = Employee(UserID=u_userid,UserName=u_username,
            GroupName=GroupName.objects.get(Name=u_groupname),
            Levelname=Level.objects.get(Levelname=u_levelname),
            Tel=u_tel,Email=u_email,QQ=u_qq,Other=u_introduce,Gender=u_gender)

        if u_levelname == "GroupLeader":
            gl = GroupName.objects.get(Name=u_groupname)
            gl.GroupMaster = u_username
            gl.save()

        user = User.objects.create_user(username=u_userid,password=u_password)
        user.save()
        employee.save()
        messages.add_message(request, messages.SUCCESS, 'Add user successfully!')
        return HttpResponseRedirect('userlist',locals())

    levels = Level.objects.all()

    return render_to_response('user/new-user.html',locals(),context_instance = RequestContext(request))

@login_required
@permission_required('Manager.change_employee')
def edituser(request):
    title = "User"
    username = request.user

    groups = GroupName.objects.all()
    notifications = Notification.objects.filter(ToUser=username)

    if request.method == "POST":
        user = Employee.objects.get(UserID=request.POST['userid'])

        user.UserName = request.POST['username']
        user.GroupName = GroupName.objects.get(Name=request.POST['groupname'])
        user.Levelname = Level.objects.get(Levelname=request.POST['levelname'])
        user.Tel = request.POST['tel']
        user.Email = request.POST['email']
        user.Other = request.POST['introduce']
        user.QQ = request.POST['qq']
        user.Gender = request.POST['gender']
        user.save()

        if user.Levelname.Levelname == "GroupLeader":
            gl = GroupName.objects.get(Name=user.GroupName.Name)
            gl.GroupMaster = user.UserName
            gl.save()
        messages.add_message(request, messages.SUCCESS, 'Edit user successfully!')
        return HttpResponseRedirect('userlist',locals())

    if 'editUID' in request.GET:
        user = Employee.objects.get(id=int(request.GET.get("editUID",'1')))

        levels = Level.objects.all()
        return render_to_response('user/edit-user.html',locals(),context_instance = RequestContext(request))

    return HttpResponseRedirect('userlist',locals())


@login_required
@permission_required('Manager.delete_employee')
def deluser(request):
    username = request.user
    title = "User"

    groups = GroupName.objects.all()
    notifications = Notification.objects.filter(ToUser=username)

    if 'delUID' in request.GET:
        uid = request.GET.get("delUID",'1')

        User.objects.get(username=uid).delete()
        Employee.objects.get(UserID=uid).delete()
        messages.add_message(request, messages.SUCCESS, 'Delete user successfully!')
        return HttpResponseRedirect('userlist',locals())

    return render_to_response('user/user-list.html',locals(),context_instance = RequestContext(request))

##################################################
#########################  Group  ###################

@login_required
def grouplist(request):
    title = "Group"
    username = request.user

    groups = GroupName.objects.all()
    notifications = Notification.objects.filter(ToUser=username)

    if 'SearchName' in request.GET:
        groups = GroupName.objects.filter(Name__icontains=request.GET.get("SearchName",'1'))
    else:
        groups = GroupName.objects.all()

    users = Employee.objects.all()
    #print(groups)

    return render_to_response('group/group-list.html',locals(),context_instance = RequestContext(request))

@login_required
@permission_required('Manager.add_groupname')
def addgroup(request):
    username = request.user
    title = "Group"

    groups = GroupName.objects.all()
    notifications = Notification.objects.filter(ToUser=username)

    if request.method == "POST":
        u_groupname = request.POST['groupname']

        #print (u_groupname,u_groupmaster)

        group = GroupName(Name=u_groupname)
        group.save()
        messages.add_message(request, messages.SUCCESS, 'Add group successfully!')
        return HttpResponseRedirect('grouplist',locals())

    return render_to_response('group/group-list.html',locals(),context_instance = RequestContext(request))

@login_required
@permission_required('Manager.change_groupname')
def editgroup(request):
    username = request.user
    title = "Group"

    groups = GroupName.objects.all()
    notifications = Notification.objects.filter(ToUser=username)

    if request.method == "POST":
        u_groupid = request.POST['groupid']
        u_groupname = request.POST['groupname']


        #print (u_groupid,u_groupname,u_groupmaster)

        group = GroupName.objects.get(id=u_groupid)
        group.Name = u_groupname

        #print (group.Name)
        group.save()
        messages.add_message(request, messages.SUCCESS, 'Edit group successfully!')
        return HttpResponseRedirect('grouplist',locals())

    return render_to_response('group/group-list.html',locals(),context_instance = RequestContext(request))


@login_required
@permission_required('Manager.delete_groupname')
def delgroup(request):
    username = request.user
    title = "Group"

    groups = GroupName.objects.all()
    notifications = Notification.objects.filter(ToUser=username)

    if 'delgroupID' in request.GET:
        groupid = int(request.GET.get("delgroupID",'1'))

        ####checke people in group
        GroupName.objects.get(id=groupid).delete()
        messages.add_message(request, messages.SUCCESS, 'Delete group successfully!')
        return HttpResponseRedirect('grouplist',locals())

    return render_to_response('group/group-list.html',locals(),context_instance = RequestContext(request))

#####################  Team Plan  ######################

@login_required
def planlist(request):
    title = "Plan"
    username = request.user

    groups = GroupName.objects.all()
    notifications = Notification.objects.filter(ToUser=username)

    subTitle = "Team"
    plans = Plan.objects.filter(planlevel="Team")

    if plans.count() > 0:
        first_plan = plans[0]
    plans = pageGenerator(request,plans)

    return render_to_response('plan/plan-list.html',locals(),context_instance = RequestContext(request))


@login_required
def plangrouplist(request):
    title = "Plan"
    username = request.user

    groups = GroupName.objects.all()
    notifications = Notification.objects.filter(ToUser=username)

    if 'planofgroup' in request.GET:
        plans = Plan.objects.filter(planlevel=request.GET.get("planofgroup",'1'))
        subTitle = request.GET.get("planofgroup",'1') + "'s"
        try:
            if 'SearchName' in request.GET:
                members = Employee.objects.filter(UserName__icontains=request.GET.get("SearchName",'1'))
            else:
                members = Employee.objects.filter(GroupName=GroupName.objects.get(Name=request.GET.get("planofgroup",'1')))

        except Exception as e:
            if 'SearchName' in request.GET:
                members = Employee.objects.filter(UserName__icontains=request.GET.get("SearchName",'1'))
            else:
                members = Employee.objects.filter(GroupName=Employee.objects.get(UserID=request.GET.get("planofgroup",'1')).GroupName)
        
    else:
        return HttpResponseRedirect('planlist',locals())

    if plans.count() > 0:
        first_plan = plans[0]
    plans = pageGenerator(request,plans)

    return render_to_response('plan/plan-group-list.html',locals(),context_instance = RequestContext(request))


@login_required
def addplan(request):
    title = "Plan"
    username = request.user

    groups = GroupName.objects.all()
    notifications = Notification.objects.filter(ToUser=username)

    planlevels = [username.username]

    ##################****************************************
    if Employee.objects.get(UserID=username).Levelname.Levelname == "Manager":
        planlevels.append("Team")
    if Employee.objects.get(UserID=username).Levelname.Levelname == 'GroupMember':
        planlevels = [username.username]
    if Employee.objects.get(UserID=username).Levelname.Levelname == 'GroupLeader':
        planlevels.append(Employee.objects.get(UserID=username).GroupName)
    ##################****************************************

    if request.method == "POST":
        u_userid = username
        u_username = Employee.objects.get(UserID=username).UserName
        u_datetime = request.POST['datetime']
        u_plantitle = request.POST['plantitle']
        u_planlevel = request.POST['planlevel']
        u_content = request.POST['content']

        #############################
        plan = Plan(UserID=u_userid,UserName=u_username,plantitle=u_plantitle,
            Datetime=u_datetime,planlevel=u_planlevel,Content=u_content,Progress="0")
        plan.save()
        messages.add_message(request, messages.SUCCESS, 'Add plan successfully!')
        return HttpResponseRedirect('planlist',locals())

    return render_to_response('plan/new-plan.html',locals(),context_instance = RequestContext(request))

@login_required
def plandetail(request):
    title = "Plan"
    username = request.user

    groups = GroupName.objects.all()
    notifications = Notification.objects.filter(ToUser=username)

    if 'planid' not in request.GET:
        return HttpResponseRedirect('planlist',locals())
    else:
        detail = Plan.objects.get(id=int(request.GET.get("planid",'1')))
        plans = Plan.objects.filter(planlevel=detail.planlevel)

        if detail.planlevel == "Team":
            rel = "Team"
            relates = GroupName.objects.all()
            if 'SearchName' in request.GET:
                relates = GroupName.objects.filter(Name__icontains=request.GET.get("SearchName",'1'))
        else:
            rel = ""
            relates = Employee.objects.filter(GroupName=Employee.objects.get(UserID=detail.UserID).GroupName)
            if 'SearchName' in request.GET:
                relates = Employee.objects.filter(GroupName=Employee.objects.get(UserID=detail.UserID).GroupName,UserName__icontains=request.GET.get("SearchName",'1'))
        return render_to_response('plan/plan-detail.html',locals(),context_instance = RequestContext(request))

@login_required
def editplan(request):
    title = "Plan"
    username = request.user

    groups = GroupName.objects.all()
    notifications = Notification.objects.filter(ToUser=username)

    if request.method == "POST":
        u_id = request.POST['id']
        plan = Plan.objects.get(id=u_id)

        plan.plantitle = request.POST['plantitle']
        plan.Datetime = request.POST['datetime']
        plan.planlevel = request.POST['planlevel']
        plan.Content = request.POST['content']
        plan.Progress = request.POST['progress']

        plan.save()
        messages.add_message(request, messages.SUCCESS, 'Edit plan successfully!')
        return HttpResponseRedirect('planlist',locals())


    if 'planid' not in request.GET:
        return HttpResponseRedirect('planlist',locals())
    else:
        if username.username != Plan.objects.get(id=int(request.GET.get("planid",'1'))).UserID:
            return HttpResponseRedirect('planlist',locals())
        else:
            edit = Plan.objects.get(id=int(request.GET.get("planid",'1')))
            return render_to_response('plan/edit-plan.html',locals(),context_instance = RequestContext(request))

@login_required
def delplan(request):
    username = request.user
    title = "Level"

    groups = GroupName.objects.all()
    notifications = Notification.objects.filter(ToUser=username)

    if 'planid' not in request.GET:
        return HttpResponseRedirect('planlist',locals())
    else:
        if username.username != Plan.objects.get(id=int(request.GET.get("planid",'1'))).UserID:
            return HttpResponseRedirect('planlist',locals())
        else:
            Plan.objects.get(id=int(request.GET.get("planid",'1'))).delete()
            messages.add_message(request, messages.SUCCESS, 'Delete plan successfully!')
            return HttpResponseRedirect('planlist',locals())

@login_required
def advertise(request):
    if request.method == "POST":
        u_id = request.POST['detailid']
        detail = Plan.objects.get(id=u_id)
        detail.Advertisement = request.POST['Advertisement']
        detail.save()

        notification = Notification(Type="Plan Advertisement",ToUser=detail.UserID,Content=request.META.get('HTTP_REFERER', '/'))
        notification.save()
        messages.add_message(request, messages.SUCCESS, 'Add advertisement successfully!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

###################Level#############################
@login_required
def levellist(request):
    title = "Level"
    username = request.user

    groups = GroupName.objects.all()
    notifications = Notification.objects.filter(ToUser=username)

    if 'SearchName' in request.GET:
        levels = Level.objects.filter(Levelname__icontains=request.GET.get("SearchName",'1'))
    else:
        levels = Level.objects.all()

    levels = pageGenerator(request,levels)
    users = Employee.objects.all()
    #print(groups)

    return render_to_response('level/level-list.html',locals(),context_instance = RequestContext(request))

@login_required
@permission_required('Manager.add_level')
def addlevel(request):
    username = request.user
    title = "Level"

    groups = GroupName.objects.all()
    notifications = Notification.objects.filter(ToUser=username)

    if request.method == "POST":
        u_levelname = request.POST['levelname']

        level = Level(Levelname=u_levelname)
        level.save()
        messages.add_message(request, messages.SUCCESS, 'Add level successfully!')
        return HttpResponseRedirect('levellist',locals())

    return render_to_response('level/level-list.html',locals(),context_instance = RequestContext(request))

@login_required
@permission_required('Manager.change_level')
def editlevel(request):
    username = request.user
    title = "Level"

    groups = GroupName.objects.all()
    notifications = Notification.objects.filter(ToUser=username)

    if request.method == "POST":
        u_levelid = request.POST['levelid']
        u_levelname = request.POST['levelname']

        #print (u_groupid,u_groupname,u_groupmaster)

        level = Level.objects.get(id=u_levelid)
        level.Levelname = u_levelname
        #print (group.Name)
        level.save()
        messages.add_message(request, messages.SUCCESS, 'Edit level successfully!')
        return HttpResponseRedirect('levellist',locals())

    return render_to_response('level/level-list.html',locals(),context_instance = RequestContext(request))


@login_required
@permission_required('Manager.delete_level')
def dellevel(request):
    username = request.user
    title = "Level"

    groups = GroupName.objects.all()
    notifications = Notification.objects.filter(ToUser=username)


    if 'dellevelID' in request.GET:
        levelid = int(request.GET.get("dellevelID",'1'))
        ####checke people with level

        Level.objects.get(id=levelid).delete()
        messages.add_message(request, messages.SUCCESS, 'Delete level successfully!')
        return HttpResponseRedirect('levellist',locals())

    return render_to_response('level/level-list.html',locals(),context_instance = RequestContext(request))
#############################################################################

#################################### Score #########################################

@login_required
def scorelist(request):
    title = "Score"
    username = request.user

    groups = GroupName.objects.all()
    notifications = Notification.objects.filter(ToUser=username)

    try:
        base = Salarybase.objects.all()[0]
    except Exception as e:
        base = "" 

    if 'SearchName' in request.GET:
        users = Employee.objects.filter(UserID__icontains=request.GET.get("SearchName",'1'))
    else:
        users = Employee.objects.all()

    users = pageGenerator(request,users)

    return render_to_response('score/score-list.html',locals(),context_instance = RequestContext(request))


@login_required
@permission_required('Manager.change_salary')
def editscore(request):
    username = request.user
    title = "Score"

    groups = GroupName.objects.all()
    notifications = Notification.objects.filter(ToUser=username)

    if request.method == "POST":
        u_userid = request.POST['userid']
        u_scorenum = request.POST['scorenum']
        u_spoint = request.POST['spoint']
        u_event = request.POST['event']
        #print (u_groupid,u_groupname,u_groupmaster)

        user = Employee.objects.get(id=u_userid)
        user.Score = u_scorenum
        user.SalaryPoint = u_spoint
        user.save()
        eventobj = Salary(UserID=user.UserID,Score=u_scorenum,SalaryPoint=u_spoint,Event=u_event)
        eventobj.save()


        notification = Notification(Type="Score Change",ToUser=user.UserID,Content="/manage/eventlist?SearchName="+user.UserID)
        notification.save()
        messages.add_message(request, messages.SUCCESS, 'Edit score successfully!')
        return HttpResponseRedirect('scorelist',locals())

    return render_to_response('score/score-list.html',locals(),context_instance = RequestContext(request))


@login_required
def eventlist(request):
    title = "Score"
    username = request.user

    groups = GroupName.objects.all()
    notifications = Notification.objects.filter(ToUser=username)

    if 'SearchName' in request.GET:
        salarys = Salary.objects.filter(UserID__icontains=request.GET.get("SearchName",'1'))
    else:
        salarys = Salary.objects.all()

    salarys = pageGenerator(request,salarys)

    return render_to_response('score/event-list.html',locals(),context_instance = RequestContext(request))

@login_required
def salarybase(request):
    title = "Score"
    username = request.user

    if request.method == "POST":
        salary = Salarybase(Base=request.POST['base'],Publisher=username.username,Datetime=time.time()) 
        salary.save()
        messages.add_message(request, messages.SUCCESS, 'Set salary base successfully!')

    return HttpResponseRedirect('scorelist',locals())

#################################################################

##############################   html5  ########################

@login_required
def html5mario(request):

    return render_to_response('html5/mario/index.html',locals(),context_instance = RequestContext(request))
