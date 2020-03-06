"""mxshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
import xadmin
from goods.view_base import GoodsListView

urlpatterns = [
	path('xadmin/', xadmin.site.urls),
	path('goods/', GoodsListView.as_view(), name='goods_list'),
	path('docs/', include_docs_urls(title='接口文档')),
	path('api-auth/', include('rest_framework.urls')),
]
