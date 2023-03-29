from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def index(request):
    # return HttpResponse("Welcome to mysite")
    return render(request,'index.html')
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


#####添加用户，这里基于modelform来处理
# Django ModelForm修改默认的控件属性
# https://blog.csdn.net/weixin_30254435/article/details/99050157
from django.forms import ModelForm
class Add_user_modelfrom(ModelForm):
    class Meta:
        model=Person
        # fields = ['name', 'age', ]
        fields='__all__'

#      <input type="email" class="form-control" id="exampleInputEmail1" placeholder="Email">
    def __init__(self, *args, **kwargs):
        super(Add_user_modelfrom, self).__init__(*args, **kwargs)
        for field_name in self.base_fields:
            field = self.base_fields[field_name]
            field.widget.attrs.update({'class': "form-control", 'id': 'exampleInput'})

def add_user(request):
    print(request.method)
    if request.method == 'GET':
        form=Add_user_modelfrom()
        return render(request,'add_user.html',{'form':form})
    form=Add_user_modelfrom(request.POST)
    form.save()
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


from django.forms import ModelForm
class Modify_user_modelfrom(ModelForm):
    class Meta:
        model=Person
        # fields = ['name', 'age', ]
        fields='__all__'

#      <input type="email" class="form-control" id="exampleInputEmail1" placeholder="Email">
    def __init__(self, *args, **kwargs):
        super(Modify_user_modelfrom, self).__init__(*args, **kwargs)
        for field_name in self.base_fields:
            field = self.base_fields[field_name]
            field.widget.attrs.update({'class': "form-control", 'id': 'exampleInput'})

def modify_user(request,uid):
    '''
    :param request: 
    :return:
    '''
    data = Person.objects.filter(id=uid).first()
    print(data)
    if request.method == 'GET':
        form=Modify_user_modelfrom(instance=data)
        return render(request,'modify.html',{'form':form})

    else:
        form= Modify_user_modelfrom(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('/list/user')
