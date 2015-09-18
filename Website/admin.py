from django.contrib import admin
from Website.models import *
from django import forms  
from django.utils.translation import ugettext_lazy
from Skyrover.widgets import KindEditor
# Register your models here.

class kindeditorNewsForm(forms.ModelForm):  
	Content = forms.CharField(label=ugettext_lazy(u"Content"), widget=KindEditor(attrs={'rows':15, 'cols':100}),required=True)
	class Meta:
		model = News 
		fields = "__all__" 

class NewsAdmin(admin.ModelAdmin):
	list_display = ('Title','Publsh_Date')
	form = kindeditorNewsForm

class kindeditorAnnounceForm(forms.ModelForm):  
	Content = forms.CharField(label=ugettext_lazy(u"Content"), widget=KindEditor(attrs={'rows':15, 'cols':100}),required=True)
	class Meta:
		model = Announce 
		fields = "__all__" 

class AnnounceAdmin(admin.ModelAdmin):
	list_display = ('Title','Publsh_Date')
	form = kindeditorAnnounceForm

class PolicyAdmin(admin.ModelAdmin):
	list_display = ('Name','Publsh_Date','keyword')

class MagazineAdmin(admin.ModelAdmin):
	list_display = ('Name','Publsh_Date','keyword')


class PartnershipAdmin(admin.ModelAdmin):
	list_display = ('Name','PeopleType')

class kindeditorPeopleForm(forms.ModelForm):  
	Content = forms.CharField(label=ugettext_lazy(u"Content"), widget=KindEditor(attrs={'rows':15, 'cols':100}),required=True)
	class Meta:
		model = People 
		fields = "__all__" 

class PeopleAdmin(admin.ModelAdmin):
	list_display = ('Name','PeopleType')
	form = kindeditorPeopleForm

admin.site.register(News,NewsAdmin)
admin.site.register(Announce,AnnounceAdmin)
admin.site.register(Policy,PolicyAdmin)
admin.site.register(Magazine,MagazineAdmin)
admin.site.register(PeopleType)
admin.site.register(Partnership,PartnershipAdmin)
admin.site.register(People,PeopleAdmin)
admin.site.register(Group)
