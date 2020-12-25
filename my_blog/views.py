from django.shortcuts import render,redirect,get_object_or_404
from .models import Article
from django.contrib.auth.models import User
from .forms import Articleform
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class PostListView(ListView):
	model = Article
	ordering = ['-date_posted']

class UserPostListView(ListView):
	model = Article
	template_name = 'my_blog/user_post.html'

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Article.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
	model = Article

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Article

	fields = [
	'title',
	'entry']

	def form_valid(self,form):
		form.instance.author =self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
	model = Article

	fields = [
	'title',
	'entry']

	def form_valid(self,form):
		form.instance.author =self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model = Article
	success_url = '/'
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False



def about_view(request):
	return render(request,"my_blog/about.html",{})


def start_view(request):
	
	last = Article.objects.order_by('-id')[:3]
	cnxt = {
	'last' : last,

	}
	return render(request,"my_blog/start.html",cnxt)