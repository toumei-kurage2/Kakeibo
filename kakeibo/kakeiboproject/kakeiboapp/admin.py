from django.contrib import admin

# モデルをインポート
from . models import Koumoku,Rireki

# 管理ツールに登録
admin.site.register(Koumoku)
admin.site.register(Rireki)