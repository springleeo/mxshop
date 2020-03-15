import json

from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from django.core import serializers
from goods.serializers import GoodsSerializer, CategorySerializer
from goods.models import Goods, GoodsCategory
from goods.filters import GoodsFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


# class GoodsListView(View):
# 	"""1.使用django自带的view实现商品列表页，自定义返回的字段"""
#
# 	def get(self, request):
# 		json_list = []
# 		# 获取所有商品
# 		goods = Goods.objects.all()
# 		for good in goods:
# 			json_dict = {}
# 			# 获取商品的每个字段，键值队的形式
# 			json_dict['name'] = good.name
# 			json_dict['category'] = good.category.name
# 			json_dict['market_price'] = good.market_price
# 			json_list.append(json_dict)
#
# 		return HttpResponse(json.dumps(json_list), content_type='application/json')


# class GoodsListView(View):
# 	"""2.使用django自带的serializer序列化model，返回所有字段"""
#
# 	# 因为包含所有字段，所以image相关的字段必须序列化，这里就引入了django自带的序列化
# 	def get(self, request):
# 		"""将model整个转化为dict"""
# 		json_list = []
# 		goods = Goods.objects.all()
# 		# 将所有数据序列化
# 		json_data = serializers.serialize('json', goods)
# 		json_data = json.loads(json_data)
# 		return JsonResponse(json_data, safe=False)

# class GoodsListView(APIView):
# 	"""3/4.使用django rest framework的APIview和serializers.Serializer实现商品列表页"""
#
# 	def get(self, request):
# 		goods = Goods.objects.all()
# 		goods_serializer = GoodsSerializer(goods, many=True)
# 		return Response(goods_serializer.data)

# class GoodsListView(GenericAPIView):
# 	"""5.使用django rest framework的APIview和ModelSerializer实现商品列表页"""
# 	# 使用GenericAPIView，必须定义queryset和serializer_class
# 	queryset = Goods.objects.all()
# 	serializer_class = GoodsSerializer
#
# 	def get(self, request, *args, **kwargs):
# 		# 实例化获取数据
# 		goods = self.get_queryset()
# 		# 序列化数据
# 		goods_serializer = self.get_serializer(goods, many=True)
# 		# 返回数据
# 		return Response(goods_serializer.data)


# class GoodsListView(mixins.ListModelMixin, GenericAPIView):
# 	"""6.使用django rest framework的GenericAPIView和ModelSerializer实现商品列表页"""
# 	# # 使用GenericAPIView，必须定义queryset和serializer_class
# 	queryset = Goods.objects.all()
# 	serializer_class = GoodsSerializer
#
# 	def get(self, request, *args, **kwargs):
# 		return self.list(request, *args, **kwargs)


# class GoodsListView(ListAPIView):
# 	"""7.使用django rest framework的ListAPIView实现商品列表页"""
# 	# 定义queryset和serializer_class
# 	queryset = Goods.objects.all()
# 	serializer_class = GoodsSerializer


class GoodsPagination(PageNumberPagination):
	"""自定义分页功能"""
	# 默认每页显示的个数
	page_size = 12
	# 可以动态改变每页显示的个数
	page_size_query_param = 'page_size'
	# 页码参数
	page_query_param = 'page'
	# 每页显示的最大个数
	max_page_size = 100


# class GoodsListView(ListAPIView):
# 	"""自定义分页功能"""
# 	pagination_class = GoodsPagination
# 	# 必须定义一个默认的排序，添加order_by才不会提示'分页可能产生不一致的结果'
# 	queryset = Goods.objects.all().order_by('id')
# 	serializer_class = GoodsSerializer


class GoodsListViewSet(mixins.ListModelMixin, GenericViewSet):
	"""使用viewset和Router实现商品列表页"""

	pagination_class = GoodsPagination
	# 必须定义一个默认的排序，添加order_by才不会提示'分页可能产生不一致的结果'
	queryset = Goods.objects.all().order_by('id')
	serializer_class = GoodsSerializer

	filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

	# 设置filter的类为我们自定义的类
	filter_class = GoodsFilter
	# 商品搜索, =name表示精确搜索，也可以使用各种正则表达式
	search_fields = ('=name', 'goods_brief', 'goods_desc')
	# 排序
	ordering_fields = ('sold_num', 'shop_price')


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
	"""商品分类列表"""
	queryset = GoodsCategory.objects.filter(category_type=1)
	serializer_class = CategorySerializer
