from django.urls import path
from myapp import views


urlpatterns = [
    path('image-sync/', views.image_sync),
    path('image/',views.image)

]
