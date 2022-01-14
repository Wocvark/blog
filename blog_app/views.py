from django.shortcuts import render

# Create your views here.
from .models import blog

def main(resp):
	
	q1 = blog.objects.order_by('-pub_date')
	count  = blog.objects.count()
	dic = {'q1':q1, 'count':count}
	
	return render(resp, 'blog/home.html', dic)

def blogs(resp, id):

	wr = blog.objects.get(pk=id)
	print(type(wr))
	return render(resp, 'blog/blogs.html', {'write':wr })
