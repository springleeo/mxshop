from datetime import datetime

from django.db import models
from DjangoUeditor.models import UEditorField


class GoodsCategory(models.Model):
	"""商品类别"""
	CATEGORY_TYPE = (
		(1, '一级类目'),
		(2, '二级类目'),
		(3, '三级类目')
	)
	name = models.CharField('类别名', max_length=32, default='')
	code = models.CharField('类别code', max_length=32, default='')
	desc = models.TextField('类别描述', max_length=64, default='')
	category_type = models.IntegerField('类目级别', choices=CATEGORY_TYPE)
	parent_category = models.ForeignKey('self', related_name='sub_cat', verbose_name='父类目级别', null=True, blank=True,
	                                    on_delete=models.CASCADE)
	is_tab = models.BooleanField('是否导航', default=False)
	add_time = models.DateTimeField('添加时间', default=datetime.now)

	class Meta:
		verbose_name = '商品类别'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name


class GoodsCategoryBrand(models.Model):
	"""品牌"""
	category = models.ForeignKey(GoodsCategory, related_name='brands', verbose_name='商品类目', null=True, blank=True,
	                             on_delete=models.CASCADE)
	name = models.CharField('品牌名', max_length=32, default='')
	desc = models.TextField('品牌描述', max_length=200, default='')
	image = models.ImageField('品牌图片', max_length=200, upload_to='brands/')
	add_time = models.DateTimeField('添加时间', default=datetime.now)

	class Meta:
		verbose_name = '品牌'
		verbose_name_plural = verbose_name
		db_table = 'goods_goodsbrand'

	def __str__(self):
		return self.name


class Goods(models.Model):
	category = models.ForeignKey(GoodsCategory, related_name='goods', verbose_name='商品类目', default='',
	                             on_delete=models.CASCADE)
	goods_sn = models.CharField('商品货号', default='', max_length=50)
	name = models.CharField('商品名', max_length=32)
	click_num = models.IntegerField('点击数', default=0)
	sold_num = models.IntegerField('商品销售量', default=0)
	fav_num = models.IntegerField('收藏数', default=0)
	goods_num = models.IntegerField('库存数', default=0)
	market_price = models.FloatField('市场价格', default=0)
	shop_price = models.FloatField('市场价格', default=0)
	goods_brief = models.TextField('商品简短描述', default=0)
	goods_desc = UEditorField('商品内容', width=1000, height=300, imagePath='goods/images/', filePath='goods/files/',
	                          default='')
	goods_front_image = models.ImageField('封面图', upload_to='goods/images', null=True, blank=True)
	ship_free = models.BooleanField('是否承担运费', default=True)
	is_new = models.BooleanField('是否新品', default=False)
	is_hot = models.BooleanField('是否热销', default=False)
	add_time = models.DateTimeField('添加时间', default=datetime.now)

	class Meta:
		verbose_name = '商品'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name


class GoodsImage(models.Model):
	"""商品轮播图"""
	goods = models.ForeignKey(Goods, verbose_name='商品', related_name='images', on_delete=models.CASCADE)  # 不理解
	image = models.ImageField('图片', upload_to='', null=True, blank=True)
	add_time = models.DateTimeField('添加时间', default=datetime.now)

	class Meta:
		verbose_name = '商品图片'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.goods.name


class Banner(models.Model):
	"""轮播的商品"""
	goods = models.ForeignKey(Goods, verbose_name='商品', on_delete=models.CASCADE)
	image = models.ImageField('轮播图片', upload_to='banner')
	index = models.IntegerField('轮播顺序', default=0)
	add_time = models.DateTimeField('添加时间', default=datetime.now)

	class Meta:
		verbose_name = '轮播商品'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.goods.name
