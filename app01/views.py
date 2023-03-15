from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def index(request):
    return HttpResponse("Welcome to mysite")

def test(request):
    # data=['hello','world']
    # return render(request,'test.html',{'data':data})

    data={'k1':'hello','k2':'world'}
    return render(request,'test.html',{'data':data})

from app01.models import Person
def ormtest(request):
    '''
    :param request: 
    :return: 
    
    新增用户
    Person.objects.create(name='scott',age=10)
    Person.objects.create(name='jack', age=20)
    <QuerySet [<Person: Person object (1)>, <Person: Person object (2)>, <Person: Person object (3)>, <Person: Person object (4)>]>
    '''
    data=Person.objects.all()
    return render(request, 'test.html', {'data': data})

def list_user(request):
    data = Person.objects.all()
    return render(request, 'list_user.html', {'data': data})

def add_user(request):
    print(request.method)
    if request.method == 'GET':
        return render(request,'add_user.html')
    name=request.POST.get('user')
    age=request.POST.get('age')
    print(f'{ name } {age }')
    Person.objects.create(name=name,age=age)
    return redirect('/list/user/')

def delete_user(request):
    '''
    :param request: 
    :return:
     借助 ?id= 获取 key来删除
     https://blog.csdn.net/MaxineZhou/article/details/104971307
    '''
    id=request.GET.get('id')
    data=Person.objects.get(id=id).delete()
    print(data)
    return redirect('/list/user')

