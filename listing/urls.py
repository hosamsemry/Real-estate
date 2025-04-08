from django.urls import path
from .views import *


urlpatterns = [
    path('manage/', ManageListingView.as_view(), name='manage-listing'),
    path('detail/', ListingDetailView.as_view(), name='listing-detail'),
    path('all/', ListingsView.as_view(), name='listing-list'),
]