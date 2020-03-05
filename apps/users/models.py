from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
	"""用户"""
	name = models.CharField('姓名', max_length=32, null=True)
	birthday = models.DateTimeField('生日', null=True)
	gender = models.CharField('性别', max_length=10, choices=(('male', '男'), ('female', '女')), default='female')
	mobile = models.CharField('手机号', max_length=11)
	email = models.EmailField('邮箱', max_length=128, null=True, blank=True)

	class Meta:
		verbose_name = '用户'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.username


class VerifyCode(models.Model):
	"""短信验证码"""
	code = models.CharField('验证码', max_length=10)
	mobile = models.CharField('手机号', max_length=11)
	add_time = models.DateTimeField('添加时间', default=datetime.now)

	class Meta:
		verbose_name = '短信验证码'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.code
