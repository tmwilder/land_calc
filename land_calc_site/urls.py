from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^get_odds/$', 'land_calc_app.views.get_odds'),
    url(r'^.*$', 'land_calc_app.views.main')
)