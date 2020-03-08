from goods.serializers import GoodsSerializer
from goods.models import Goods
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView


# class GoodsListView(APIView):
# 	"""商品列表"""
#
# 	def get(self, request):
# 		goods = Goods.objects.all()
# 		goods_serializer = GoodsSerializer(goods, many=True)
# 		return Response(goods_serializer.data)

class GoodsListView(GenericAPIView):
	"""商品列表"""
	# 使用GenericAPIView，必须定义queryset和serializer_class
	queryset = Goods.objects.all()
	serializer_class = GoodsSerializer

	def get(self, request, *args, **kwargs):
		# 实例化获取数据
		goods = self.get_queryset()
		# 序列化数据
		goods_serializer = self.get_serializer(goods, many=True)
		# 返回数据
		return Response(goods_serializer.data)

