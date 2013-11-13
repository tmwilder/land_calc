from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'main/^$', 'land_calc_app.views.main'),
    url(r'.*^$', 'land_calc_app.views.main'),
)
