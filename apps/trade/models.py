from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models

from apps.goods.models import Goods

User = get_user_model()


class ShoppingCart(models.Model):
	"""购物车"""
	# 为什么不继承自己建的users，因为自己建的users只是扩展，User还是在原有的模型中
	user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
	goods = models.ForeignKey(Goods, verbose_name='商品', on_delete=models.CASCADE)
	nums = models.IntegerField('购买数量', default=0)
	add_time = models.DateTimeField('添加时间', default=datetime.now)

	class Meta:
		verbose_name = '购物车'
		verbose_name_plural = verbose_name

	def __str__(self):
		return "%s(%d)".format(self.goods.name, self.nums)


class OrderInfo(models.Model):
	"""订单信息"""
	PAY_STATUS = (
		('TRADE_SUCCESS', '成功'),
		('TRADE_CLOSED', '超时关闭'),
		('WAIT_BUYER_PAY', '交易创建'),
		('TRADE_FINISHED', '交易结束'),
		('paying', '待支付'),

	)
	user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
	order_sn = models.CharField('订单号', max_length=32, null=True, blank=True, unique=True)
	trade_no = models.CharField('交易号', max_length=100, null=True, blank=True, unique=True)
	pay_status = models.CharField('订单状态', choices=PAY_STATUS, default='paying', max_length=32)
	post_script = models.CharField('订单留言', max_length=200)
	order_mount = models.FloatField('订单金额', default=0.0)
	pay_time = models.DateTimeField('支付时间', default=0.0, null=True, blank=True)
	address = models.CharField('收获地址', max_length=100, default=0)
	signer_name = models.CharField('收货人', max_length=32, default='')
	singer_mobile = models.CharField('联系电话', max_length=11)
	add_time = models.DateTimeField('添加时间', default=datetime.now)

	class Meta:
		verbose_name = '订单'
		verbose_name_plural = verbose_name

	def __str__(self):
		return str(self.order_sn)


class OrderGoods(models.Model):
	"""订单的商品详情"""
	order = models.ForeignKey(OrderInfo, verbose_name='订单信息', related_name='goods', on_delete=models.CASCADE)
	goods = models.ForeignKey(Goods, verbose_name='商品', on_delete=models.CASCADE)
	goods_num = models.IntegerField('商品数量', default=0)
	add_time = models.DateTimeField('添加时间', default=0)

	class Meta:
		verbose_name = '订单商品'
		verbose_name_plural = verbose_name

	def __str__(self):
		return str(self.order.order_sn)
