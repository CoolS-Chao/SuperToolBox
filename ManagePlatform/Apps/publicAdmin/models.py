from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as _UserManager

# Create your models here.


class UserManager(_UserManager):
	"""
	Note:
		If you do not need the default fields in auth_user, you can choose to give default values.
	Example:
		def create_superuser(self, username, password, email=None, **extra_fields):
			super(UserManager, self).create_superuser(
				username=username,
				password=password,
				email=email,
				**extra_fields
			)
	"""
	def create_superuser(self, username, password, **extra_fields):
		super(UserManager, self).create_superuser(
			username=username,
			password=password,
			**extra_fields
		)


class Users(AbstractUser):
	"""
	Note:
		If you need to add additional required fields based on auth_user, you can add them as follows.
	Example:
		REQUIRED_FIELDS = ['mobile']
		mobile = models.CharField(
			max_length=11, unique=True, verbose_name="手机号", help_text='手机号',
			error_messages={'unique': "此手机号已注册"}
		)
	"""
	objects = UserManager()
	
	class Meta:
		db_table = "site_users"
		verbose_name = "用户"    # 在admin站点中显示的名称
		verbose_name_plural = verbose_name  # 显示的复数名称
		
	def __str__(self):
		return self.username