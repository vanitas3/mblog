# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
reload(sys)
sys.setdefaultencoding('utf8')#Python的str默认是ascii编码，和unicode编码冲突

from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Post
from datetime import datetime
from django.template.loader import get_template

# Create your views here.

def homepage(request):
	#posts = Post.objects.all()
	#post_lists = list()
	#for count, post in enumerate(posts):
		#post_lists.append("No.{}:".format(str(count)) + str(post) + "<br>")
		#post_lists.append("<small>" + str(post.body) + "</small><br><br>")
	#return HttpResponse(post_lists)
	

	template = get_template('index.html')
	posts = Post.objects.all()
	now = datetime.now()
	html = template.render(locals())
	return HttpResponse(html)

def showpost(request, slug):
	template = get_template('post.html')
	try:
		post = Post.objects.get(slug = slug)
		if post != None:
			html = template.render(locals())
			return HttpResponse(html)
	except:
		return redirct('/')
	
