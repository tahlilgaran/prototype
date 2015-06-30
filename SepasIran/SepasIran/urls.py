
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'home/$', 'present_trip.views.home'),
    url(r'home/username/$' , 'present_trip.views.home_login'),
    url(r'help/$', 'tourism.views.help'),
    url(r'signup/$', 'user.views.signup'),
    url(r'signIn/$', 'user.views.signin'),
    url(r'signup/tourist/$', 'user.views.tourist_signup'),
    url(r'signup/tourist/tourBuilder$', 'user.views.servant_signup'),
    url(r'userPage/tourBuilder/(P?<user_id>\d+)$', 'informing.views.builder_page'),
    url(r'userPage/tourists/(P?<user_id>\d+)$', 'informing.views.tourist_page'),
    url(r'tourList/(P?<search_id>\d+)/$', 'present_trip.views.listTour'),
    url(r'show/(\w+)/$', 'present_trip.views.show_one_trip'),
    url(r'show/(\w+)/status/$', 'present_trip.views.show_one_trip_status'),
    url(r'purchase/(P?<tour_id>\d+)/$', 'buy_cancel.views.purchase'),
    url(r'payment/(P?<id>\d+)/$', 'accounting.views.payment'),
    url(r'payment/Confirm/(P?<id>\d+)/$', 'accounting.views.confirm'),
    url(r'tourDefine/$', 'define_and_validate_trip.views.defineTour'),
    url(r'manager/Dashboard/$', 'manager_dashboard.views.Dashboard'),
    url(r'manager/tourLists/$', 'manager_dashboard.views.tourLists'),
    url(r'manager/userLists/$', 'manager_dashboard.views.userLists'),
    url(r'manager/paymentsList/$', 'manager_dashboard.views.paymentLists'),
    url(r'manager/OnlineComments/$', 'manager_dashboard.views.onlineComments'),
    url(r'polling/(P?<tour_id>\+d)/$', 'quality_control.views.polling'),
    url(r'onlinePolling/$', 'quality_control.views.onlinePolling'),
    url(r'^admin/', include(admin.site.urls)),
]
