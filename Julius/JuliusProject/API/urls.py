# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:11:03 2018

@author: Joao Junkes
"""

from django.conf.urls import url
from DelyCadoApp.views import ItemListView, ItemView

helper_patterns = [
    url(r'^item/$', ItemListView.as_view(), name='item'),
    url(r'^item/(?P<pk>[0-9]+)/$', ItemView.as_view(), name='get_item')
]

urlpatterns = helper_patterns