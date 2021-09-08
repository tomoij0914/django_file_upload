from django.urls import path, include
import file_upload.views as file_upload
# 画像の表示に必要
from . import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    # http://127.0.0.1:8000/success/url/に
    # アクセスしたら，アプリ「file_upload」
    # フォルダのurls.pyのsuccess関数に移動
    #path('success/url/',file_upload.success),
    # http://127.0.0.1:8000/upload/にアクセスしたら，
    # アプリ「file_upload」フォルダのurls.pyに移動
    path('upload/',include('file_upload.urls')),
]
# 画像の表示に必要,MEDIA_URLとMEDIA_ROOTを設定
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
