from django import forms

from django.conf import settings

from django.utils.safestring import mark_safe

from django.template.loader import render_to_string

class KindEditor(forms.Textarea):

    class Media:

        js  = (

                settings.STATIC_URL + 'manage/kindeditor/kindeditor.js' ,

                settings.STATIC_URL + 'manage/kindeditor/plugins/code/prettify.js',

        )

    def __init__(self, attrs = {}):

        #attrs['style'] = "width:800px;height:400px;visibility:hidden;"

        super(KindEditor, self).__init__(attrs)

    def render(self, name, value, attrs=None):

        rendered = super(KindEditor, self).render(name, value, attrs)

        return rendered  + mark_safe(render_to_string('kindeditor.html'))
