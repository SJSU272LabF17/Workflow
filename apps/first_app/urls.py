from django.conf.urls import url
from . import views
urlpatterns = [
  # home page
  url(r'^$', views.home),
  url(r'^about$', views.about),
  url(r'^contact$', views.contact),
  url(r'services$', views.services),
  # user account
  url(r'^register$', views.register),
  url(r'^login$', views.login),
  url(r'^logout$', views.logout),
  url(r'^signin$', views.signin),
    # url(r'^chngPswd$', views.chngPswd),
# dashboard
  url(r'^dashBoard$', views.dashBoard),
# show templates
  url(r'^templates$', views.showTemplates),
  url(r'^constructmain$', views.constructmain),
  url(r'^coffeemain$', views.coffeemain),
  url(r'^itmain$', views.itmain),
# checklist
  url(r'^newchecklist$', views.newchecklist),
  url(r'^create$', views.create_new),
  url(r'^createSuccess$', views.createSuccess),
  url(r'^checklist$', views.checklist),
  url(r'^delete/(?P<container_id>\d+)$', views.delete),
  url(r'^savedChecklists$', views.savedChecklists),
  url(r'^show/(?P<container_id>\d+)$', views.show),
  url(r'^edit/(?P<container_id>\d+)$', views.edit),  
  # test
  url(r'^test$', views.test),
  url(r'^testnew$', views.test_new),


  # url(r'^remove_wish/(?P<item_id>\d+)$', views.remove_wish),
  
]