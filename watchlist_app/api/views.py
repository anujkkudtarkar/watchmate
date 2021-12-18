from django.shortcuts import render
from watchlist_app.models import WatchList, StreamPlatform, Review
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from watchlist_app.api.serializers import StreamPlatformSerializer, WatchListSerializer, ReviewSerializer
from rest_framework import generics

# Create your views here.

class WatchlistAV(generics.ListCreateAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer
    
class WatchDetailAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer    
    
class StreamPlatformListAV(generics.ListCreateAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
    
class StreamPlatformDetailAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
    
class ReviewlistAV(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
class ReviewDetailAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer        

# class WatchlistAV(APIView):
    
#     def get(self,request, *args, **kwargs):
#         movies = WatchList.objects.all()
#         serializer = WatchListSerializer(movies, many=True)
#         return Response(serializer.data)
    
#     def post(self,request, *args, **kwargs):
#         serializer = WatchListSerializer(data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
# class WatchDetailAV(APIView):
    
#     def get(self,request, pk, *args, **kwargs):
#         movie = WatchList.objects.get(pk=pk)
#         serializer = WatchListSerializer(movie)
#         return Response(serializer.data)
    
#     def put(self,request,pk, *args, **kwargs):
#         movie = WatchList.objects.get(pk=pk)
#         serializer = WatchListSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else: 
#             return Response(serializer.errors)
        
    # def patch(self,request,pk, *args, **kwargs):
    #     movie = WatchList.objects.get(pk=pk)
    #     serializer = WatchListSerializer(movie, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()        
    #     pass
    
    # def delete(self,request,pk, *args, **kwargs):
    #     movie = WatchList.objects.get(pk=pk)
    #     serializer = WatchListSerializer(movie)
        
    #     pass
    
            