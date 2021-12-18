from django.urls import path, include

from watchlist_app.api.views import WatchlistAV, WatchDetailAV

urlpatterns = [
    path('list/', WatchlistAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchDetailAV.as_view(), name='movie-details'),    
]