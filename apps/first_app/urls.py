from django.conf.urls import url
from . import views
urlpatterns = [
  url(r'^main$', views.index),
  url(r'^register$', views.register),
  url(r'^login$', views.login),
  url(r'^logout$', views.logout),
  url(r'^dashboard$', views.dashboard),
  url(r'^checklists/create$', views.create_new),
  url(r'^create_process$', views.create_process),
  url(r'^wish_items/(?P<item_id>\d+)$', views.item),
  url(r'^add_wish/(?P<item_id>\d+)$', views.add_wish),
  url(r'^remove_wish/(?P<item_id>\d+)$', views.remove_wish),
  url(r'^delete_item/(?P<item_id>\d+)$', views.delete_item),
]