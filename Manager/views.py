#!/usr/bin/python
#-*-coding:utf-8-*-
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.models import User, Group
from django.contrib import auth
from django.core.paginator import Paginator,InvalidPage,EmptyPage


from rest_framework import viewsets

from Manager.models import *
from Manager.serializers import *

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

#########################   index   ######################
@login_required
def index(request):
    username = request.user
    title = "Dashboard"

    groups = GroupName.objects.all()
    return render_to_response('index.html',locals(),context_instance = RequestContext(request))

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
    error_message = ""
    username = request.user

    if 'SearchName' in request.GET:
        users = Employee.objects.filter(UserID=request.GET.get("SearchName",'1'))
    else:
        users = Employee.objects.all()

    users = pageGenerator(request,users)
    groups = GroupName.objects.all()
    #print(users)

    return render_to_response('user/user-list.html',locals(),context_instance = RequestContext(request))


@login_required
@permission_required('Manager.add_employee')
def adduser(request):
    title = "User"
    error_message = ""
    username = request.user

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
        print (u_username,u_password)

        #############################
        employee = Employee(UserID=u_userid,UserName=u_username,
            GroupName=GroupName.objects.get(Name=u_groupname),
            Levelname=Level.objects.get(Levelname=u_levelname),
            Tel=u_tel,Email=u_email,QQ=u_qq,Other=u_introduce)
        user = User.objects.create_user(username=u_userid,password=u_password)
        user.save()
        employee.save()
        
        return HttpResponseRedirect('userlist',locals())

    groups = GroupName.objects.all()
    levels = Level.objects.all()
    
    return render_to_response('user/new-user.html',locals(),context_instance = RequestContext(request))

@login_required
@permission_required('Manager.change_employee')
def edituser(request):
    title = "User"
    error_message = ""
    username = request.user

    if request.method == "POST":
        user = Employee.objects.get(UserID=request.POST['userid'])

        user.UserName = request.POST['username']
        user.GroupName = GroupName.objects.get(Name=request.POST['groupname'])
        user.Levelname = Level.objects.get(Levelname=request.POST['levelname'])
        user.Tel = request.POST['tel']
        user.Email = request.POST['email']
        user.Other = request.POST['introduce']
        user.QQ = request.POST['qq']
        #u_password = request.POST['password']
        #u_confpassword = request.POST['confpassword']
        #print (u_username,u_password)

        user.save()
        
        return HttpResponseRedirect('userlist',locals())

    if 'editUID' in request.GET:
        user = Employee.objects.get(id=int(request.GET.get("editUID",'1')))


        groups = GroupName.objects.all()
        levels = Level.objects.all()
        return render_to_response('user/edit-user.html',locals(),context_instance = RequestContext(request))

    groups = GroupName.objects.all()
    
    return HttpResponseRedirect('userlist',locals())


@login_required
@permission_required('Manager.delete_employee')
def deluser(request):
    username = request.user
    title = "User"
    error_message = ""

    if 'delUID' in request.GET:
        uid = int(request.GET.get("delUID",'1'))

        User.objects.get(username=uid).delete()
        Employee.objects.get(UserID=uid).delete()

        #print (groupid)
        error_message = "success"
        return HttpResponseRedirect('userlist',locals())
    
    groups = GroupName.objects.all()
    return render_to_response('user/user-list.html',locals(),context_instance = RequestContext(request))

##################################################
#########################  Group  ###################

@login_required
def grouplist(request):
    title = "Group"
    error_message = ""
    username = request.user

    if 'SearchName' in request.GET:
        groups = GroupName.objects.filter(Name=request.GET.get("SearchName",'1'))
    else:
        groups = GroupName.objects.all()

    groups = pageGenerator(request,groups)
    users = Employee.objects.all()
    #print(groups)

    return render_to_response('group/group-list.html',locals(),context_instance = RequestContext(request))

@login_required
@permission_required('Manager.add_groupname')
def addgroup(request):
    username = request.user
    title = "Group"
    error_message = ""

    if request.method == "POST":
        u_groupname = request.POST['groupname']
        u_groupmaster = request.POST['groupmaster']
        
        #print (u_groupname,u_groupmaster)

        group = GroupName(Name=u_groupname,GroupMaster=u_groupmaster)
        group.save()
        return HttpResponseRedirect('grouplist',locals())
    groups = GroupName.objects.all()
    return render_to_response('group/group-list.html',locals(),context_instance = RequestContext(request))

@login_required
@permission_required('Manager.change_groupname')
def editgroup(request):
    username = request.user
    title = "Group"
    error_message = ""

    if request.method == "POST":
        u_groupid = request.POST['groupid']
        u_groupname = request.POST['groupname']
        u_groupmaster = request.POST['groupmaster']
        
        #print (u_groupid,u_groupname,u_groupmaster)

        group = GroupName.objects.get(id=u_groupid)
        group.Name = u_groupname
        group.GroupMaster = u_groupmaster
        #print (group.Name)
        group.save()
        return HttpResponseRedirect('grouplist',locals())
    groups = GroupName.objects.all()
    return render_to_response('group/group-list.html',locals(),context_instance = RequestContext(request))


@login_required
@permission_required('Manager.delete_groupname')
def delgroup(request):
    username = request.user
    title = "Group"
    error_message = ""

    if 'delgroupID' in request.GET:
        groupid = int(request.GET.get("delgroupID",'1'))

        ####checke people in group

        GroupName.objects.get(id=groupid).delete()
        #print (groupid)
        error_message = "success"
        return HttpResponseRedirect('grouplist',locals())
    groups = GroupName.objects.all()
    return render_to_response('group/group-list.html',locals(),context_instance = RequestContext(request))

#####################  Team Plan  ######################

@login_required
def planlist(request):
    title = "Plan"
    error_message = ""
    username = request.user

    groups = GroupName.objects.all()

    subTitle = "Team"
    plans = Plan.objects.filter(planlevel="Team")

    if plans.count() > 0:
        first_plan = plans[0]
    plans = pageGenerator(request,plans)
     
    return render_to_response('plan/plan-list.html',locals(),context_instance = RequestContext(request))


@login_required
def plangrouplist(request):
    title = "Plan"
    error_message = ""
    username = request.user

    if 'planofgroup' in request.GET:
        plans = Plan.objects.filter(planlevel=request.GET.get("planofgroup",'1'))
        subTitle = request.GET.get("planofgroup",'1') + " Group"
        members = Employee.objects.filter(GroupName=GroupName.objects.get(Name=request.GET.get("planofgroup",'1')))
    elif 'planof' in request.GET:
        plans = Plan.objects.filter(planlevel=request.GET.get("planof",'1'))
        subTitle = request.GET.get("planof",'1') + "'s"
        members = Employee.objects.filter(GroupName=Employee.objects.get(UserID=request.GET.get("planof",'1')).GroupName)
    else:
        return HttpResponseRedirect('planlist',locals())

    if plans.count() > 0:
        first_plan = plans[0]
    plans = pageGenerator(request,plans)
    groups = GroupName.objects.all()
    return render_to_response('plan/plan-group-list.html',locals(),context_instance = RequestContext(request))


@login_required
def addplan(request):
    title = "Plan"
    error_message = ""
    username = request.user

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
        
        return HttpResponseRedirect('planlist',locals())

    groups = GroupName.objects.all()
    #levels = Level.objects.all()
    
    return render_to_response('plan/new-plan.html',locals(),context_instance = RequestContext(request))

@login_required
def plandetail(request):
    title = "Plan"
    error_message = ""
    username = request.user
    groups = GroupName.objects.all()

    if 'planid' not in request.GET:
        return HttpResponseRedirect('planlist',locals())
    else:
        detail = Plan.objects.get(id=int(request.GET.get("planid",'1')))
        plans = Plan.objects.filter(planlevel=detail.planlevel)
        groups = GroupName.objects.all()
        return render_to_response('plan/plan-detail.html',locals(),context_instance = RequestContext(request))

@login_required
def editplan(request):
    title = "Plan"
    error_message = ""
    username = request.user

    groups = GroupName.objects.all()

    if request.method == "POST":
        u_id = request.POST['id']
        plan = Plan.objects.get(id=u_id)

        plan.plantitle = request.POST['plantitle']
        plan.Datetime = request.POST['datetime']
        plan.planlevel = request.POST['planlevel']
        plan.Content = request.POST['content']
        plan.Progress = request.POST['progress']

        plan.save()
        
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
    error_message = ""

    groups = GroupName.objects.all()

    if 'planid' not in request.GET:
        return HttpResponseRedirect('planlist',locals())
    else:
        if username.username != Plan.objects.get(id=int(request.GET.get("planid",'1'))).UserID:
            return HttpResponseRedirect('planlist',locals())
        else:
            Plan.objects.get(id=int(request.GET.get("planid",'1'))).delete()
            error_message = "success"
            return HttpResponseRedirect('planlist',locals())

###################Level#############################
@login_required
def levellist(request):
    title = "Level"
    error_message = ""
    username = request.user

    if 'SearchName' in request.GET:
        levels = Level.objects.filter(Levelname=request.GET.get("SearchName",'1'))
    else:
        levels = Level.objects.all()

    levels = pageGenerator(request,levels)
    users = Employee.objects.all()
    #print(groups)
    groups = GroupName.objects.all()
    return render_to_response('level/level-list.html',locals(),context_instance = RequestContext(request))

@login_required
@permission_required('Manager.add_level')
def addlevel(request):
    username = request.user
    title = "Level"
    error_message = ""
    groups = GroupName.objects.all()

    if request.method == "POST":
        u_levelname = request.POST['levelname']
        
        #print (u_groupname,u_groupmaster)

        level = Level(Levelname=u_levelname)
        level.save()
        return HttpResponseRedirect('levellist',locals())
    
    return render_to_response('level/level-list.html',locals(),context_instance = RequestContext(request))

@login_required
@permission_required('Manager.change_level')
def editlevel(request):
    username = request.user
    title = "Level"
    error_message = ""

    groups = GroupName.objects.all()

    if request.method == "POST":
        u_levelid = request.POST['levelid']
        u_levelname = request.POST['levelname']
        
        #print (u_groupid,u_groupname,u_groupmaster)

        level = Level.objects.get(id=u_levelid)
        level.Levelname = u_levelname
        #print (group.Name)
        level.save()
        return HttpResponseRedirect('levellist',locals())
    
    return render_to_response('level/level-list.html',locals(),context_instance = RequestContext(request))


@login_required
@permission_required('Manager.delete_level')
def dellevel(request):
    username = request.user
    title = "Level"
    error_message = ""

    groups = GroupName.objects.all()

    if 'dellevelID' in request.GET:
        levelid = int(request.GET.get("dellevelID",'1'))

        ####checke people with level

        Level.objects.get(id=levelid).delete()
        #print (groupid)
        error_message = "success"
        return HttpResponseRedirect('levellist',locals())
    
    return render_to_response('level/level-list.html',locals(),context_instance = RequestContext(request))
#############################################################################

#################################### Score #########################################

@login_required
def scorelist(request):
    title = "Score"
    error_message = ""
    username = request.user

    if 'SearchName' in request.GET:
        users = Employee.objects.filter(UserID=request.GET.get("SearchName",'1'))
    else:
        users = Employee.objects.all()

    users = pageGenerator(request,users)
    #print(users)
    groups = GroupName.objects.all()
    return render_to_response('score/score-list.html',locals(),context_instance = RequestContext(request))


@login_required
def editscore(request):
    username = request.user
    title = "Score"
    error_message = ""

    groups = GroupName.objects.all()

    if request.method == "POST":
        u_userid = request.POST['userid']
        u_scorenum = request.POST['scorenum']
        u_event = request.POST['event']
        #print (u_groupid,u_groupname,u_groupmaster)

        user = Employee.objects.get(id=u_userid)
        user.Score = u_scorenum
        user.save()
        eventobj = Salary(UserID=user.UserID,Score=u_scorenum,Event=u_event)
        eventobj.save()
        
        return HttpResponseRedirect('scorelist',locals())
    
    return render_to_response('score/score-list.html',locals(),context_instance = RequestContext(request))


@login_required
def eventlist(request):
    title = "Score"
    error_message = ""
    username = request.user

    groups = GroupName.objects.all()

    if 'SearchName' in request.GET:
        salarys = Salary.objects.filter(UserID=request.GET.get("SearchName",'1'))
    else:
        salarys = Salary.objects.all()

    salarys = pageGenerator(request,salarys)

    return render_to_response('score/event-list.html',locals(),context_instance = RequestContext(request))

