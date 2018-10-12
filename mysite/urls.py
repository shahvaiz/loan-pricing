from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

from myapp.views import *



urlpatterns = [
    url(r'^contact/$', inquiry_form, name='inquiry_form'),
    url(r'^application/$', application, name='application'),
    url(r'^rates/$', quote, name = 'quote'),
    url(r'^zip_test/$', zip_test, name='myapp.views.zip_test'),
    url(r'^calculator/$', calculator, name='myapp.views.calculator'),
    url(r'^about/$', about, name='myapp.views.about'),
    url(r'^programs/$', programs, name='myapp.views.programs'),
    url(r'^investor$', investor, name='myapp.views.investor'),
    url(r'^bankstatement$', bankstatement, name='myapp.views.bankstatement'),
    url(r'^foreignnational$', foreignnational, name='myapp.views.foreignnational'),
	url(r'^realtors$', realtors, name='myapp.views.realtors'),
	url(r'^military$', military, name='myapp.views.military'),
	url(r'^valoans$', valoans,name='myapp.views.valoans'),
	url(r'^easyinvestorloan$', easyinvestorloan, name='myapp.views.easyinvestorloan'),
	url(r'^brokers$', brokers,name='myapp.views.brokers'),
	url(r'^purchasenewhome$', purchasenewhome, name='myapp.views.purchasenewhome'),
	url(r'^homeexperts$', homeexperts,name='myapp.views.homeexperts'),
	url(r'^esign$', esign,name='myapp.views.esign'),
	url(r'^adjustableratemortgage$', adjustableratemortgage, name='myapp.views.adjustableratemortgage'),
	url(r'^mortgageloanoptions$', mortgageloanoptions, name='myapp.views.mortgageloanoptions'),
    url(r'^noincome$', noincome,name ='myapp.views.noincome'),
    url(r'^$', fluid,name='myapp.views.fluid'),
	url(r'^sitemap\.xml$', sitemap,name='myapp.views.sitemap'),
]
