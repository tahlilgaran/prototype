from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'home/$', 'present_trip.views.home'),
<<<<<<< HEAD
    url(r'home/(\w+)/$' , 'present_trip.views.home'),
=======
    url(r'home/username/$', 'present_trip.views.home_login'),
>>>>>>> maryam
    url(r'help/$', 'tourism.views.help'),
    url(r'tourdefine/(\w+)$', 'define_and_validate_trip.views.tarif_kind'),
    url(r'tourdefine/tour/(\w+)$','define_and_validate_trip.views.tour_define'),
    url(r'signup/$', 'user.views.signup'),
    url(r'signIn/$', 'user.views.signin'),
    url(r'signup/tourist/$', 'user.views.tourist_signup'),
    url(r'signup/tourist/tourBuilder$', 'user.views.servant_signup'),
    url(r'userpage/(\w+)$', 'informing.views.account'),
    url(r'show/(\w+)/$', 'present_trip.views.show_one_trip'),
<<<<<<< HEAD
    url(r'show/(\w+)/(\w+)$', 'present_trip.views.show_one_trip'),
    url(r'show/(\w+)/(\w+)/status/$', 'present_trip.views.show_one_trip_status'),
   # url(r'reserve/(P?<tour_id>\d+)/$', 'buy_cancel.views.reserve'),

     url(r'reserve/(\w+)/$', 'buy_cancel.views.reserve'),
   #  url(r'reserve/([service][tour])/$', 'buy_cancel.views.reserve'),
   url(r'purchase/(P?<tour_id>\d+)/$', 'buy_cancel.views.purchase'),
     url(r'purchase/(\w+)/$', 'buy_cancel.views.purchase'),
     url(r'purchase/$', 'buy_cancel.views.purchase'),
    url(r'search/form/$', 'present_trip.views.start_search'),
    url(r'search/form/(\w+)/$', 'present_trip.views.start_search'),
=======
    url(r'show/(\w+)/status/$', 'present_trip.views.show_one_trip_status'),
    url(r'reserve/(P?<tour_id>\d+)/$', 'buy_cancel.views.reserve'),
    url(r'reserve/(\w+)/$', 'buy_cancel.views.reserve'),
    url(r'reserve/confirm/$', 'buy_cancel.views.confirm'),
    url(r'purchase/(P?<tour_id>\d+)/$', 'buy_cancel.views.purchase'),
    url(r'purchase/(\w+)/$', 'buy_cancel.views.purchase'),
    url(r'purchase/$', 'buy_cancel.views.purchase'),
>>>>>>> maryam
    url(r'search/result/$', 'present_trip.views.search'),
    url(r'search/result/(\w+)/$', 'present_trip.views.search'),
    url(r'search/result/(\w+)/(\w+)$', 'present_trip.views.search'),
    url(r'purchase/(P?<tour_id>\d+)/$', 'buy_cancel.views.purchase'),
    url(r'cancel/(\w+)/$', 'accounting.views.cancel'),
    url(r'payment/(P?<id>\d+)/$', 'accounting.views.payment'),
    url(r'payment/Confirm/(P?<id>\d+)/$', 'accounting.views.confirm'),
<<<<<<< HEAD
=======
    url(r'^tourDefine/(P?<username>\w+)/$', 'define_and_validate_trip.views.tarif_kind'),
>>>>>>> maryam
    url(r'payment/$', 'accounting.views.payment'),
    url(r'payment/confirm/(P?<id>\d+)/$', 'accounting.views.confirm'),
    url(r'payment/confirm/$', 'accounting.views.confirm'),
    url(r'manager/Dashboard/$', 'manager_dashboard.views.Dashboard'),
    url(r'manager/tourLists/$', 'manager_dashboard.views.tourLists'),
    url(r'manager/tourRating/$', 'manager_dashboard.views.tourRating'),
    url(r'manager/tourRating/$', 'manager_dashboard.views.onlineComments'),
    url(r'manager/userLists/$', 'manager_dashboard.views.userLists'),
    url(r'manager/paymentsList/$', 'manager_dashboard.views.paymentLists'),
    url(r'manager/OnlineComments/$', 'manager_dashboard.views.onlineComments'),
    url(r'polling/(P?<tour_id>\+d)/$', 'quality_control.views.polling'),
    url(r'onlinePolling/$', 'quality_control.views.onlinePolling'),
    url(r'^admin/', include(admin.site.urls)),
]
