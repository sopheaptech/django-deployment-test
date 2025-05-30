from django.db import models
from django.contrib.auth.models import User

# Create your models here.()
# In User model only username, password, email, first_name, last_name are present.
# We will extend this model to include additional information like profile picture, bio, etc.

class UserProfileInfo(models.Model):
  """
  UserProfileInfo model to extend the User model with additional fields.
  This model is linked to the User model via a OneToOneField.
  """

  # This model extends the User model to include additional information
  user=models.OneToOneField(User, on_delete=models.CASCADE) # usre have one to one relationship files with User class from django.contrib.auth.models
  # Additional fields
  # Use upload_to='profile_pics' to make sure you can upload pic
  profile_pic=models.ImageField(upload_to='profile_pics', blank=True)
  portpolio_site=models.URLField(blank=True)
  bio=models.TextField(blank=True)

  def __str__(self):
    """
    String representation of the UserProfileInfo model.
    Returns the username of the user associated with this profile.
    """
    return self.user.username
  
