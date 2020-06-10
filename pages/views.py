from django.shortcuts import render
import random
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html')

def hello(request):
    menu = ['닭갈비','탕수육','초밥','스파케티']
    pick=random.choice(menu)
    return render(request, 'hello.html',{'pick':pick})

def name(request):
    my_name = '유환우'
    return render(request,'name.html',{'my_name':my_name})

def introduce(request):
    my_info=['유환우','29']
    name='유환우'
    age=29
    context={
        'name':'유환우',
        'age':29,
        'location':'신촌',
        'git':'http://www.github.com/yuhwanwoo'
    }
    return render(request,'introduce.html',context)

def classroom(request):
    bigdata=['김슬기','이영주','김민정','윤소윤','심재민','이준성','김현수','김현정','유명인','박누리']
    pick=random.choice(bigdata)
    return render(request,'classroom.html',{'pick':pick})

def yourname(request,name):
    context={
        'name':name
    }
    return render(request,'yourname.html',context)

def myname(request,name,age):
    context={
        'name':name,
        'age':age,
    }
    return render(request,'myname.html',context)

def times(request,num1,num2):
    num3=num1*num2
    context={
        'num1':num1,
        'num2':num2,
        'num3':num3
    }
    return render(request,'times.html',context)

def gugudan(request,big,small):
    result=[]
    if big<small:
        big,small=small,big
    for num in range(1,small+1):
        result.append(big*num)
    context={
        'result':result
    }
    return render(request,'gugudan.html',context)

def dtl(request):
    my_list=['짜장면','차돌짬뽕','탕수육','콩국수']
    empty_list=[]
    my_string="Life is short, You need Python"
    today=datetime.now()
    context={
        'my_list':my_list,
        'empty_list':empty_list,
        'my_string':my_string,
        'today':today
    }
    return render(request,'dtl.html',context)

def forif(request):
    my_list=[100,50,30,20,10]
    my_string='간단한 문자열'
    data_a='첫번째 데이터'
    data_b='두번째 데이터'
    data_a,data_b=data_b,data_a
    context={
        'my_list':my_list,
        'my_string':my_string,
        'data_a':data_a,
        'data_b':data_b
    }
    return render(request,'forif.html',context)


