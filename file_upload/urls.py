from django.urls import path
from . import views

urlpatterns = [
    #空のURLにアクセスしたらviews.pyのfile_upload関数に移動
    path('', views.file_upload, name='file_upload'),
]