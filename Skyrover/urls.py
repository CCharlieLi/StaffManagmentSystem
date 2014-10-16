from django.conf.urls import include, url
from django.contrib import admin
from Manager import views
from rest_framework import routers


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', views.UserAuthViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'announcements', views.AnnouncementViewSet)
router.register(r'levels', views.LevelViewSet)
router.register(r'calendar', views.CalendarViewSet)
router.register(r'salary', views.SalaryViewSet)


urlpatterns = [
    # Examples:
    # url(r'^$', 'Skyrover.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),

    #### REST ####
    url(r'^API/REST/', include(router.urls),name='REST'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    ####  Manager  ####
    url(r'^manage/login$','Manager.views.login',name="login"),
    url(r'^manage/logout$','Manager.views.logout',name="logout"),
    url(r'^manage/index$','Manager.views.index',name="index"),

    #announce
    url(r'^manage/addannounce$','Manager.views.addannounce',name="addannounce"),
    url(r'^manage/editannounce$','Manager.views.editannounce',name="editannounce"),
    url(r'^manage/delannounce$','Manager.views.delannounce',name="delannounce"),
    url(r'^manage/readannounce$','Manager.views.readannounce',name="readannounce"),

    #user
    url(r'^manage/userlist$','Manager.views.userlist',name="userlist"),
    url(r'^manage/adduser$','Manager.views.adduser',name="adduser"),
    url(r'^manage/edituser$','Manager.views.edituser',name="edituser"),
    url(r'^manage/deluser$','Manager.views.deluser',name="deluser"),

    #group
    url(r'^manage/grouplist$','Manager.views.grouplist',name="grouplist"),
    url(r'^manage/addgroup$','Manager.views.addgroup',name="addgroup"),
    url(r'^manage/editgroup$','Manager.views.editgroup',name="editgroup"),
    url(r'^manage/delgroup$','Manager.views.delgroup',name="delgroup"),

    #level
    url(r'^manage/levellist$','Manager.views.levellist',name="levellist"),
    url(r'^manage/addlevel$','Manager.views.addlevel',name="addlevel"),
    url(r'^manage/editlevel$','Manager.views.editlevel',name="editlevel"),
    url(r'^manage/dellevel$','Manager.views.dellevel',name="dellevel"),

    #score
    url(r'^manage/scorelist$','Manager.views.scorelist',name="scorelist"),
    url(r'^manage/editscore$','Manager.views.editscore',name="editscore"),
    url(r'^manage/eventlist$','Manager.views.eventlist',name="eventlist"),

    #Calendar
    url(r'^manage/calendar$','Manager.views.calendar',name="calendar"),

    #plan
    url(r'^manage/planlist$','Manager.views.planlist',name="planlist"),
    url(r'^manage/plangrouplist$','Manager.views.plangrouplist',name="plangrouplist"),
    url(r'^manage/planlist$','Manager.views.planlist',name="planlist"),
    url(r'^manage/addplan$','Manager.views.addplan',name="addplan"),
    url(r'^manage/plandetail$','Manager.views.plandetail',name="plandetail"),
    url(r'^manage/editplan$','Manager.views.editplan',name="editplan"),
    url(r'^manage/delplan$','Manager.views.delplan',name="delplan"),
]
