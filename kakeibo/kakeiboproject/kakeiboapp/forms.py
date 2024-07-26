from django import forms
from .models import Rireki,Koumoku
from datetime import date
import datetime
from django.core.exceptions import ValidationError
from django.utils import timezone

class RirekiForm(forms.ModelForm):
    date=forms.DateField(input_formats=['%Y-%m-%d', '%d/%m/%Y'],
                         widget=forms.DateInput(attrs={'type': 'date'}),
                         initial=date.today,
                         label="使用日")
    fee=forms.IntegerField(max_value=10000000,min_value=1,label="金額")
    def clean_date(self):
        date = self.cleaned_data.get("date")
        under_date=datetime.date(1980,1,1)
        today=timezone.now().date()
        top_date=datetime.date(today.year,today.month,today.day)
        if date < under_date:
            raise ValidationError("1980年以前の指定はできません")
        if date > top_date:
            raise ValidationError("今日より後の指定はできません")
        return date       
    class Meta:
        model=Rireki
        fields=["date","fee","koumoku"]
        labels={"date":"使用日","fee":"金額","koumoku":"項目名"}
    
class YMForm(forms.Form):
    today=datetime.datetime.now()
    year=forms.IntegerField(label="年",initial=today.date().year,min_value=1980,max_value=2100)
    month=forms.IntegerField(min_value=1,max_value=12,label="月",initial=today.date().month)
