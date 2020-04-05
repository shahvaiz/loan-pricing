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
       (r'^noincome$', 'myapp.views.noincome'),
       (r'^$', 'myapp.views.fluid'),
)
