from rest_framework import serializers
from goods.models import Goods, GoodsCategory


# class GoodsSerializer(serializers.Serializer):
# 	"""3.使用django rest framework的APIview和serializers.Serializer实现商品列表页"""
# 	name = serializers.CharField(required=True, max_length=100)
# 	click_num = serializers.IntegerField(default=0)
# 	goods_front_image = serializers.ImageField()
# 	add_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")


class GoodsCategorySerializer(serializers.ModelSerializer):
	"""序列化所有category信息"""
	class Meta:
		model = GoodsCategory
		fields = '__all__'
		# 添加深度，会显示category类别中字段的外键信息
		depth = 1


class GoodsSerializer(serializers.ModelSerializer):
	"""序列化所有商品信息"""
	# 也可以给单个字段做特殊的定义，比如更改了add_time
	add_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

	# 实例化商品类别对象，虽然我们上面实例化了类别所有信息，但是它只会覆盖当前商品所属类别的信息
	category = GoodsCategorySerializer()

	class Meta:
		model = Goods
		fields = '__all__'
