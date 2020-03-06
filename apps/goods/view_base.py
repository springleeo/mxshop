import json

from django.views.generic import View
from django.http import HttpResponse
from goods.models import Goods


class GoodsListView(View):
	"""获取商品列表"""

	def get(self, request):
		# 通过django自带的view实现商品列表页
		json_list = []
		# 获取所有商品
		goods = Goods.objects.all()
		for good in goods:
			json_dict = {}
			# 获取商品的每个字段，键值队的形式
			json_dict['name'] = good.name
			json_dict['category'] = good.category.name
			json_dict['market_price'] = good.market_price
			json_list.append(json_dict)

		return HttpResponse(json.dumps(json_list), content_type='application/json')
