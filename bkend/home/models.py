from django.db import models
import datetime
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=122)
    desc = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.name 
        # function used to store each contact details by the name of the form writer

# class CustomAccountManager(BaseUserManager):
#     def create_user(self, umail , uname , password , **other_fields ):
#         if not umail:
#             raise ValueError(_('Please provide email address'))

#         if not uname:
#             raise ValueError(_('Please provide username'))
#         umail = self.normalize_email(umail)
#         user = self.model(umail=umail , uname=uname , **other_fields)
#         user.set_password(password)
#         user.save()
#         return user
#     def create_superuser(self, umail , uname , password , **other_fields):
#         other_fields.setdefault('is_seller',True)
#         other_fields.setdefault('is_superuser',True)
#         other_fields.setdefault('is_active',True)


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    product_cat = models.CharField(max_length=50)
    product_price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateTimeField()
    is_avail = models.BooleanField(default=False)
    image = models.ImageField(upload_to="home/images" ,default="")

    def __str__(self):
        return self.product_name


# class NewUser(AbstractBaseUser,PermissionsMixin):
#     umail = models.EmailField(_('email_address'),unique=True)
#     uname = models.CharField(max_length=40 , unique=True )
#     dob = models.DateTimeField(default=timezone.now)
#     address = models.TextField(_('address'),max_length=100 , blank=True)
#     is_customer = models.BooleanField(default=True)
#     is_seller = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)

#     objects= CustomAccountManager()
#     USERNAME_FIELD = 'uname'
#     REQUIRED_FIELDS = ['umail']

#     def __str__(self):
#         return self.uname