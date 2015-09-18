#!/usr/bin/python
#-*-coding:utf-8-*-
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.paginator import Paginator,InvalidPage,EmptyPage
from django.contrib import messages
from PIL import Image
from Website.models import *
import Website

def pageGenerator(request,objs):
	paginator = Paginator(objs,10)
	try:
		page = int(request.GET.get("page",'1'))
	except ValueError:
		page = 1
	try:
		objs = paginator.page(page)
	except (InvalidPage,EmptyPage):
		objs = paginator.page(paginator.num_pages)
	return objs

def index(request):
	title = "首页-Skyrover银河通用"
	anns = Website.models.Announce.objects.all()[0:4]
	newss = Website.models.News.objects.all()[0:4]
	print("123")
	return render_to_response('website/index.html',locals(),context_instance = RequestContext(request))

def Introduce(request):
	title = "中心简介"
	return render_to_response('website/Introduce.html',locals(),context_instance = RequestContext(request))

def Structure(request):
	title = "中心框架"
	return render_to_response('website/Structure.html',locals(),context_instance = RequestContext(request))

def Greattarget(request):
	title = "中心目标"
	return render_to_response('website/Greattarget.html',locals(),context_instance = RequestContext(request))

def Partnership(request):
	title = "协同单位"

	colleges = Website.models.Partnership.objects.filter(PeopleType=PeopleType.objects.get(Name="College"))
	companys = Website.models.Partnership.objects.filter(PeopleType=PeopleType.objects.get(Name="Company"))

	return render_to_response('website/Partnership.html',locals(),context_instance = RequestContext(request))

def Greatleader(request):
	title = "领军人物"

	leaders = People.objects.filter(PeopleType=PeopleType.objects.get(Name="Greatleader"))
	return render_to_response('website/Greatleader.html',locals(),context_instance = RequestContext(request))

def LeaderIntro(request):
	title = "领军人物"
	if 'id' in request.GET:
		lead = People.objects.get(id=int(request.GET.get("id",'1')))

	return render_to_response('website/LeaderIntro.html',locals(),context_instance = RequestContext(request))


def Directorspeech(request):
	title = "所长致辞"
	return render_to_response('website/Directorspeech.html',locals(),context_instance = RequestContext(request))

def Teamstructure(request):
	title = "团队简介"
	return render_to_response('website/Teamstructure.html',locals(),context_instance = RequestContext(request))

def Teamtarget(request):
	title = "团队目标"
	return render_to_response('website/Teamtarget.html',locals(),context_instance = RequestContext(request))

def Teammember(request):
	title = "团队构成"

	mems = People.objects.filter(PeopleType=PeopleType.objects.get(Name="Member"))
	groups = Group.objects.all()
	
	return render_to_response('website/Teammember.html',locals(),context_instance = RequestContext(request))

def PersonIntro(request):
	title = "成员简介"
	if 'id' in request.GET:
		lead = People.objects.get(id=int(request.GET.get("id",'1')))
	return render_to_response('website/PersonIntro.html',locals(),context_instance = RequestContext(request))

def skr1620(request):
	title = "skr1620"
	return render_to_response('website/skr1620.html',locals(),context_instance = RequestContext(request))

def Announce(request):
	title = "通知公告"
	anns = Website.models.Announce.objects.all()
	anns = pageGenerator(request,anns)
	return render_to_response('website/Announce.html',locals(),context_instance = RequestContext(request))

def AnnDetail(request):
	title = "通知公告"
	if 'id' in request.GET:
		news = Website.models.Announce.objects.get(id=int(request.GET.get("id",'1')))
	return render_to_response('website/AnnDetail.html',locals(),context_instance = RequestContext(request))


def News(request):
	title = "新闻动态"

	newss = Website.models.News.objects.all()
	newss = pageGenerator(request,newss)
	return render_to_response('website/News.html',locals(),context_instance = RequestContext(request))

def NewsDetail(request):
	title = "新闻动态"
	if 'id' in request.GET:
		news = Website.models.News.objects.get(id=int(request.GET.get("id",'1')))
	return render_to_response('website/NewsDetail.html',locals(),context_instance = RequestContext(request))


def Policy(request):
	title = "政策文件"

	policys = Website.models.Policy.objects.all()
	policys = pageGenerator(request,policys)
	return render_to_response('website/Policy.html',locals(),context_instance = RequestContext(request))

def Magazine(request):
	title = "银河通用内刊"

	mags = Website.models.Magazine.objects.all()
	mags = pageGenerator(request,mags)

	return render_to_response('website/Magazine.html',locals(),context_instance = RequestContext(request))

def ContactJob(request):
	title = "联系我们"
	return render_to_response('website/contact.html',locals(),context_instance = RequestContext(request))

def ContactCop(request):
	title = "联系我们"
	return render_to_response('website/contact.html',locals(),context_instance = RequestContext(request))

