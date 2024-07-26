from django.shortcuts import render,redirect
from .forms import RirekiForm,YMForm
from .models import Rireki,Koumoku
from typing import List
from datetime import date
from django.utils import timezone


def register(request):
    if request.method=="POST":
        form=RirekiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")      
    else:
        form=RirekiForm()
    return render(request,"kakeiboapp/register.html",context={"form":form})

def list(request):
    form = YMForm()
    daylist=[0]
    if request.method == "POST":
        form=YMForm(request.POST)
        if form.is_valid():
            year=form.cleaned_data["year"]
            month=form.cleaned_data["month"]
            daylist=urucheck(year,month,daylist)
            start_date=date(year,month,1)
            end_date=date(year,month,len(daylist)-1)
            rireki = Rireki.objects.filter(date__range=[start_date, end_date]).order_by('date')
            return render(request,"kakeiboapp/list.html",context={
                "rireki":rireki,
                "form":form,
                "year":year,
                "month":month,
            })
    today=timezone.now().date()
    month= today.month
    year= today.year
    daylist=urucheck(year,month,daylist)
    start_date=date(year,month,1)
    end_date=date(year,month,len(daylist)-1)
    rireki = Rireki.objects.filter(date__range=[start_date, end_date]).order_by('date')
    return render(request,"kakeiboapp/list.html",context={
        "rireki":rireki,
        "form":form,
        "year":year,
        "month":month,
    })

def table(request):
    if request.method=="POST":
        form=YMForm(request.POST)
        if form.is_valid():
            month=form.cleaned_data["month"]
            year=form.cleaned_data["year"]
            list2=tablecheck(year,month)
            list1=list2[0]
            koumokulist=list2[1]
            sumlist=list2[2]
            kurikosilist=list2[3]
            raigetu=list2[4]
            yosan_sum=list2[5]
    else:
        form=YMForm()
        today=timezone.now().date()
        month= today.month
        year= today.year
        list2=tablecheck(year,month)
        list1=list2[0]
        koumokulist=list2[1]
        sumlist=list2[2]
        kurikosilist=list2[3]
        raigetu=list2[4]
        yosan_sum=list2[5]
    return render(request,"kakeiboapp/table.html",context={
        "form":form,
        "list1":list1,
        "koumokulist":koumokulist,
        "sumlist":sumlist,
        "kurikosilist":kurikosilist,
        "raigetu":raigetu,
        "yosan_sum":yosan_sum,
        "year":year,
        "month":month
    })

def update(request,rireki_id):
    rireki = Rireki.objects.get(pk=rireki_id)
    form = RirekiForm(instance=rireki)
    if request.method=="POST":
        form = RirekiForm(request.POST,instance=rireki)
        if form.is_valid():
            form.save()
            return redirect("list")
    return render(request,"kakeiboapp/update.html",context={"form":form})

def delete(request,rireki_id):
    record=Rireki.objects.get(pk=rireki_id)
    record.delete()
    return redirect("list") 
    
def tablecheck(year,month):
    daylist=[0]
    koumokulist=Koumoku.objects.all()
    daylist=urucheck(year,month,daylist)
    list1=createtop(month,year,daylist,koumokulist)
    sumlist=grouplist_reset()
    kurikosilist=grouplist_reset()
    for i in range(len(daylist)-1):
        for j in range(len(koumokulist)):
                sumlist[j] += list1[i][j]
                sumlist[len(koumokulist)] += list1[i][j]
    for k in range(len(koumokulist)):
        kurikosilist[k] = koumokulist[k].yosan-sumlist[k]
    yosan_sum=0
    for koumoku in koumokulist:
        yosan_sum += koumoku.yosan
    raigetu = sumlist[len(koumokulist)]
    if raigetu > yosan_sum:
        raigetu=yosan_sum
    kurikosilist[len(koumokulist)]=yosan_sum-sumlist[len(koumokulist)]
    list2=[list1,koumokulist,sumlist,kurikosilist,raigetu,yosan_sum,daylist]
    return list2
    
def urucheck(year,month,daylist):
    if month==2:
        if year%4==0:
            if year%100==0:
                if year%400==0:
                    daylist=listuru(daylist)                            
                else:
                    daylist=list28(daylist)
            else:
                daylist=listuru(daylist)
        else:
            daylist=list28(daylist)
    elif month==4 or month==6 or month==9 or month==11:
        daylist=list30(daylist)
    else:
        daylist=list31(daylist)
    return daylist

def list30(daylist: List[int]):
    for i in range(30):
        daylist.append(i+1)
    return daylist
            
def list31(daylist: List[int]):
    for i in range(31):
        daylist.append(i+1)
    return daylist

def listuru(daylist: List[int]):
    for i in range(29):
        daylist.append(i+1)
    return daylist
    
def list28(daylist: List[int]):
    for i in range(28):
        daylist.append(i+1)
    return daylist                            

def createtop(month,year,daylist: List[int],koumokulist):
    list=[]
    grouplist=grouplist_reset()
    for i in range(len(daylist)-1):
        check_date=date(year,month,daylist[i+1])
        dayrecord=Rireki.objects.filter(date=check_date)
        if len(dayrecord) == 0:
            list.append(grouplist_reset())
        else:
            for j in range(len(dayrecord)):
                for k in range(len(grouplist)-1):
                    if koumokulist[k] == dayrecord[j].koumoku:
                        grouplist[k] += dayrecord[j].fee
                        grouplist[len(grouplist)-1] += dayrecord[j].fee
            list.append(grouplist)
            grouplist=grouplist_reset()
    return list

def grouplist_reset():
    grouplist=[]
    koumokulist=Koumoku.objects.all()
    for i in range(len(koumokulist)):
        grouplist.append(0)
    grouplist.append(0)
    return grouplist
