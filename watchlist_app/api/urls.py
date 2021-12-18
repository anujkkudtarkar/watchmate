from django.urls import path, include

from watchlist_app.api.views import WatchlistAV, WatchDetailAV, StreamPlatformListAV, StreamPlatformDetailAV, ReviewlistAV, ReviewDetailAV

urlpatterns = [
    path('list/', WatchlistAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchDetailAV.as_view(), name='movie-details'),
    path('stream/', StreamPlatformListAV.as_view(), name='streamplatform-list'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='streamplatform-details'),
    path('review/', ReviewlistAV.as_view(), name='review-list'),
    path('review/<int:pk>', ReviewDetailAV.as_view(), name='review-details'),                  
]