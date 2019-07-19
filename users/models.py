from django.db import models
from django.contrib.auth.models import User
import Pil

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	def __sr__ (self):
		return f'{self.user.username} Profile'