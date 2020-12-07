from django.contrib import admin
from django.urls import path
from firstapp import views
 
urlpatterns = [ path('',views.index, name='index'),]
urlpatterns += [path('ENartistic',views.ENartistic),]
urlpatterns += [ path('ENstrict',views.ENstrict), ]  
urlpatterns += [ path('UAartistic',views.UAartistic), ]  
urlpatterns += [ path('UAstrict',views.UAstrict), ]  
