from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

from goods.models import Goods

User = get_user_model()


class UserFav(models.Model):
	"""
	用户收藏
	"""
	user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
	goods = models.ForeignKey(Goods, verbose_name='商品', on_delete=models.CASCADE)
	add_time = models.DateTimeField('添加时间', default=datetime.now)

	class Meta:
		verbose_name = '用户收藏'
		verbose_name_plural = verbose_name
		unique_together = ("user", "goods")  # 联合唯一

	def __str__(self):
		return self.user.username


class UserLeavingMessage(models.Model):
	"""
	用户留言
	"""
	MESSAGE_TYPE = (
		(1, "留言"),
		(2, "投诉"),
		(3, "询问"),
		(4, "售后"),
		(5, "求购")
	)
	user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
	message_type = models.IntegerField('留言类型', default=1, choices=MESSAGE_TYPE)
	subject = models.CharField('主题', max_length=100, default='')
	message = models.TextField('留言内容', default='')
	file = models.FileField('上传的文件', upload_to='message/images/')
	add_time = models.DateTimeField('添加时间', default=datetime.now)

	class Meta:
		verbose_name = "用户留言"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.subject


class UserAddress(models.Model):
	"""
	用户收货地址
	"""
	user = models.ForeignKey(User, verbose_name="用户", on_delete=models.CASCADE)
	province = models.CharField('省份', max_length=100, default='')
	city = models.CharField('城市', max_length=100, default='')
	district = models.CharField('区域', max_length=100, default='')
	address = models.CharField('详细地址', max_length=100, default='')
	signer_name = models.CharField('收货人', max_length=100, default='')
	signer_mobile = models.CharField('电话', max_length=11, default='')
	add_time = models.DateTimeField('添加时间', default=datetime.now)

	class Meta:
		verbose_name = "收货地址"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.address
