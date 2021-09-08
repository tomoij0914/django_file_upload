from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from django.http import HttpResponse
import sys

# ------------------------------------------------------------------
# request: ブラウザからのリクエスト（HttpRequestクラスのオブジェクト）
def file_upload(request):
    # HttpRequestオブジェクトのドメインを含めないパス(/upload/)を表示
    #print(request.path)
    # HttpRequestオブジェクトの属性method(GET)を表示
    #print(request.method)

    # POSTメソッド：データの提供
    if request.method == 'POST':
        # 記述したタイトル名を表示
        #print(request.POST['title'])
        # 選択したファイル名を表示
        #print(request.FILES['file'])

        # forms.pyのUploadFileFormクラスの実行
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # ファイルアップロード関数の実行，引数は選択したファイル名
            handle_uploaded_file(request.FILES['file'])
            # 選択したファイル名を標準エラー出力する
            file_obj = request.FILES['file']
            sys.stderr.write(file_obj.name + "\n")
            # 指定したアドレスを送信
            #return HttpResponseRedirect('/success/url/')
            # htmlへの辞書型引数を作成
            context = {
                'fname': file_obj.name,
            }
            return render(request, 'file_upload/image.html', context)

    # GETメソッド：ページの表示を要求
    elif request.method == 'GET':
        # forms.pyのUploadFileFormクラスの実行と辞書型データの取得
        param = UploadFileForm()
    # renderメソッド：指定したテンプレートにコンテキスト(辞書型データ)を反映して，HttpResponseオブジェクト(レスポンス)を生成する
    # データベースのデータなどを反映させたHTMLページを作成して、HTTPレスポンスとしてブラウザに返す
    # https://office54.net/python/django/views-render-how-to
    # 第1引数：requestブラウザからのリクエスト（HttpRequestクラスのオブジェクト）
    # 第2引数：表示するテンプレートの選択
    # 第3引数: コンテキスト(辞書型データ), htmlに渡す変数と名前
    return render(request, 'file_upload/upload.html', {'form': param})
#
#
# ------------------------------------------------------------------
 # ファイルアップロード関数
def handle_uploaded_file(file_obj):
    # ファイルパスの作成
    file_path = 'media/documents/' + file_obj.name
    #print(file_obj.chunks())
    # 指定したファイルを書き込みモードで開く
    with open(file_path, 'wb') as destination:
        # https://teratail.com/questions/137973
        for chunk in file_obj.chunks():
            # 指定したファイル(destination)を保存
            destination.write(chunk)
#
"""
# ------------------------------------------------------------------
 # ファイルアップロード完了時の関数
def success(request):
    #str_out = "Success!<p />"
    # 指定した文字列をHTTPレスポンスとして返す，辞書型データは渡せない
    #return HttpResponse(str_out)
    context = {
        'fname': 'satoshi',
    }
    return render(request, 'file_upload/image.html', context)
# ------------------------------------------------------------------
"""