from rest_framework import serializers
from goods.models import Goods


# class GoodsSerializer(serializers.Serializer):
# 	name = serializers.CharField(required=True, max_length=100)
# 	click_num = serializers.IntegerField(default=0)
# 	goods_front_image = serializers.ImageField()
# 	add_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

class GoodsSerializer(serializers.ModelSerializer):
	# 也可以给单个字段做特殊的定义，比如更改了add_time
	add_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

	class Meta:
		model = Goods
		fields = '__all__'
