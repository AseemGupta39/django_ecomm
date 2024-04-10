from django.db.models import OneToOneField
from django.db.models import CharField
from django.db.models import BooleanField
from django.db.models import ImageField
from django.db.models import CASCADE
from django.contrib.auth.models import User
from base.models import BaseModel
# Create your models here.

class Profile(BaseModel):
    user = OneToOneField(User,on_delete=CASCADE,related_name="profile")
    is_email_verified = BooleanField(default=False)
    email_token = CharField(max_length=100,null=True,blank=True)
    profile_image = ImageField(upload_to='profile')
