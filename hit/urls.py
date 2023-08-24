from django.urls import path

from . import views
# from .views import ArticleDetailView

urlpatterns = [

    path('api/hitcount/<str:endpoint_path>/',
         views.CustomHitCountDetailView.as_view(), name='get_hit_count'),

    path('api/car/<int:endpoint>/',
         views.get_hit_count, name='get_hit_count2'),


]
