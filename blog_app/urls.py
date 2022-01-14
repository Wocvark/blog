from django.urls import path
from blog_app import views


urlpatterns = [

	path('', views.main, name="main"),
	path('home/<int:id>/', views.blogs, name='blogs')

]