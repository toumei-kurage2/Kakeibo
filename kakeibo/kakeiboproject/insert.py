import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kakeiboproject.settings')
from django import setup
setup()

from kakeiboapp.models import Koumoku,Rireki
from django.db.models import Sum
from datetime import date
import datetime

# Koumoku.objects.create(Koumoku_name="食費",yosan=80000)
# Koumoku.objects.create(Koumoku_name="日用雑貨",yosan=30000)
# Koumoku.objects.create(Koumoku_name="交通費",yosan=10000)
# Koumoku.objects.create(Koumoku_name="医療費",yosan=50000)
# Koumoku.objects.create(Koumoku_name="交際費",yosan=50000)
# Koumoku.objects.create(Koumoku_name="その他",yosan=50000)
