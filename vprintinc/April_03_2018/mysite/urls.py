from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'loan_pricing.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

   url(r'^admin/', include(admin.site.urls)),
       (r'^contact/$', 'myapp.views.inquiry_form'),
       (r'^application/$', 'myapp.views.application'),
       (r'^rates/$', 'myapp.views.quote'),
       (r'^zip_test/$', 'myapp.views.zip_test'),
       (r'^calculator/$', 'myapp.views.calculator'),
       (r'^about/$', 'myapp.views.about'),
       (r'^programs/$', 'myapp.views.programs'),
       (r'^investor$', 'myapp.views.investor'),
       (r'^bankstatement$', 'myapp.views.bankstatement'),
       (r'^foreignnational$', 'myapp.views.foreignnational'),
	   (r'^realtors$', 'myapp.views.realtors'),
	   (r'^military$', 'myapp.views.military'),
	   (r'^valoans$', 'myapp.views.valoans'),
	   (r'^easyinvestorloan$', 'myapp.views.easyinvestorloan'),
	   (r'^brokers$', 'myapp.views.brokers'),
	   (r'^purchasenewhome$', 'myapp.views.purchasenewhome'),
	   (r'^homeexperts$', 'myapp.views.homeexperts'),
	   (r'^esign$', 'myapp.views.esign'),
	   (r'^adjustableratemortgage$', 'myapp.views.adjustableratemortgage'),
       (r'^noincome$', 'myapp.views.noincome'),
       (r'^$', 'myapp.views.fluid'),
)
