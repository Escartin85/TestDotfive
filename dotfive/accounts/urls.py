from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='homePage'),
    url(r'^login/$', views.login_page, name='loginPage'),
    url(r'^register/$', views.register_page, name='registerPage'),
    url(r'^logout/$', views.logout_page, name='logoutPage'),
	url(r'^account/item/$', views.item_list, name='itemList'),
    url(r'^account/item/create/$', views.item_create, name='itemCreateNew'),
    url(r'^account/item/(?P<slug>[\w-]+)/$', views.item_detail, name='itemDetail'),
    url(r'^account/item/(?P<slug>[\w-]+)/edit/$', views.item_update, name='itemUpdate'),
    url(r'^account/item/(?P<slug>[\w-]+)/delete/$', views.item_delete, name='itemDelete'),
]
