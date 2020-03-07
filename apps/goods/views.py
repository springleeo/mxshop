from goods.serializers import GoodsSerializer
from goods.models import Goods
from rest_framework.views import APIView
from rest_framework.response import Response


class GoodsListView(APIView):
	"""商品列表"""

	def get(self, request):
		self.dispatch
		goods = Goods.objects.all()
		goods_serializer = GoodsSerializer(goods, many=True)
		return Response(goods_serializer.data)
