from django.conf.urls import url
from . import views
urlpatterns = [
  url(r'^$', views.home),
  url(r'^index$', views.index),
  url(r'^register$', views.register),
  url(r'^login$', views.login),
  url(r'^logout$', views.logout),
  url(r'^create$', views.create_new),
  url(r'^chngPswd$', views.chngPswd),
  url(r'^contact$', views.contact),
  url(r'^contributors$', views.contributors),
  url(r'^project$', views.project),
  url(r'^sampleChecklist$', views.sampleChecklist),
  url(r'^savedChecklist$', views.savedChecklist),
  # url(r'^create_process$', views.create_process),
  # url(r'^wish_items/(?P<item_id>\d+)$', views.item),
  # url(r'^add_wish/(?P<item_id>\d+)$', views.add_wish),
  # url(r'^remove_wish/(?P<item_id>\d+)$', views.remove_wish),
  # url(r'^delete_item/(?P<item_id>\d+)$', views.delete_item),
]