"""
URL's of our app
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views



urlpatterns = [
path('', views.home, name='home'),
path('login/', views.login_view, name='login'),
path('signup/', views.signup_view, name='signup'),
path('logout/', views.logout_view, name='logout'),
path('contact/', views.contact, name='contact'),
path('jointrip/<trip_id>', views.join_trip, name='jointrip'),
path('trips/', views.trips, name='trips'),
path('addtrip/', views.add_trip, name='addtrip'),
path('yourtrips/', views.hosting_trips, name='hostingtrips'),
path('deletetrip/<trip_id>', views.delete_trip, name='deletetrip'),
path('modifytrip/<trip_id>', views.modify_trip, name='modifytrip'),
path('joinedtrips/', views.joined_trips, name='joinedtrips'),
path('tripsdetail/<int:trip_id>/', views.trip_detail, name='trip_detail'),
path('leave_trip/<int:trip_id>/', views.leave_trip, name='leave_trip'),
path('tips', views.tips, name='tips'),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
