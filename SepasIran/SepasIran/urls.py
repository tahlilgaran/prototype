
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'home/$', 'tourism.views.main'),
    url(r'help/$', 'tourism.views.help'),
    url(r'signup/$', 'user.views.signup'),
    url(r'signIn/$', 'user.views.signin'),
    url(r'signup/tourist/$', 'user.views.tourist_signup'),
    url(r'signup/tourist/tourBuilder$', 'user.views.servant_signup'),
    url(r'userPage/tourBuilder/(P?<user-id>\d+)$', 'user.views.builder_page'),
    url(r'userPage/tourists/(P?<user-id>\d+)$', 'user.views.tourist_page'),
    url(r'tourList/(P?<search_id>\d+)/$', 'tourism.views.listTour'),
    url(r'tourShow/(P?<tour-id>\d+)/$', 'tourism.views.showingTour'),
    url(r'purchase/(P?<tour-id>\d+)/$', 'tourism.views.purchase'),
    url(r'payment/(P?<id>\d+)/$', 'accounting.views.payment'),
    url(r'payment/Confirm/(P?<id>\d+)/$', 'accounting.views.confirm'),
    url(r'tourDefine/$', 'tourism.views.defineTour'),
    url(r'manager/Dashbord/$', 'management.views.Dashbord'),
    url(r'manager/tourLists/$', 'management.views.tourLists'),
    url(r'manager/userLists/$', 'management.views.userLists'),
    url(r'manager/paymentsList/$', 'management.views.paymentLists'),
    url(r'manager/OnlineComments/$', 'management.views.onlineComments'),
    url(r'polling/(P?<tour-id>\+d)/$', 'user.views.polling'),
    url(r'onlinePolling/$', 'user.views.onlinePolling'),
    url(r'^admin/', include(admin.site.urls)),
]
