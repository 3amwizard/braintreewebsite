from django.urls import path
from website import views
from django.urls import reverse_lazy
#from suite import forms

app_name = 'website'

urlpatterns = [
	path('', views.Landing.as_view(), name='landing'),
	path('home/', views.Home.as_view(), name='home'),
	path('case-studies/', views.Case.as_view(), name='case'),
	path('read/', views.Read.as_view(), name='read'),
	path('b2b/', views.B2b.as_view(), name='b2b'),
	path('azure/', views.Azure.as_view(), name='azure'),
	path('ms/', views.Ms.as_view(), name='ms'),
	path('shop/', views.Shop.as_view(), name='shop'),
	path('reseller/', views.Reseller.as_view(), name='reseller'),
	path('contact/', views.Contact.as_view(), name='contact'),
	path('signup/', views.Signup.as_view(), name='signup'),
	path('product/', views.Product.as_view(), name='product'),
	path('gaming/', views.Gaming.as_view(), name='gaming'),
	path('industry/', views.Industry.as_view(), name='industry'),
	path('error/', views.Error.as_view(), name='error'),
	path('gaming/', views.Gaming.as_view(), name='gaming'),
	path('tournaments/', views.Tournaments.as_view(), name='tournaments'),
	path('blogG/', views.BlogG.as_view(), name='blogG'),
	path('shopG/', views.ShopG.as_view(), name='shopG'),
	path('productG/', views.ProductG.as_view(), name='productG'),
	path('account/', views.Account.as_view(), name='account'),
	path('signupG/', views.SignupG.as_view(), name='signupG'),
	path('ajax/business-form/', views.ajax_business, name='ajax_business'),
	path('ajax/individual-form/', views.ajax_individual, name='ajax_individual'),
]