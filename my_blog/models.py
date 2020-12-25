from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=20)
	entry = models.TextField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	date_posted = models.DateTimeField(default=timezone.now)

	def get_absolute_url(self):
		return reverse('my_blog:detail', kwargs={'pk': self.pk})