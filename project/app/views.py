from django.shortcuts import render,redirect
from app.models import *

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

# Create your views here.
def home(request):
    name=request.session.get('name')
    user=User.objects.get(id=request.session.get('id'))
    if user.is_admin:
        datas=Expenses.objects.all()
    else:
        datas=Expenses.objects.filter(created_by=user)
    context={
        'datas':datas,
        'user':user,
        'name':name
    }
    return render(request,'home.html',context)


def add_expenses(request):
   
    userid=request.session.get('id')
    if request.method=='POST':
        add_name=request.POST['name']
        add_category=request.POST['category']
        add_description=request.POST['description']
        add_date=request.POST['date']
        add_expenses=request.POST['expense']
        
        Expenses.objects.create(
            created_by=User.objects.get(id=userid),
            name=add_name,
            category=add_category,
            description=add_description,
            date=add_date,
            amount=add_expenses
        )

    return render(request,'add_expenses.html')

def edit(request,editid):
    run=Expenses.objects.filter(id=editid)
    cat=Expenses.objects.all()
    context={
        'run':run,
        'cat':cat,
        'categories': [i[0] for i in Expenses.CATEGORY_CHOICES]
    }
    return render(request,'edit.html',context)

def update(request,updateid):
    if request.method=='POST':
        ed_name=request.POST['name']
        ed_category=request.POST['category']
        ed_description=request.POST['description']
        ed_date=request.POST['date']
        ed_amount=request.POST['expense']
        Expenses.objects.filter(id=updateid).update(
            name=ed_name,
            category=ed_category,
            description=ed_description,
            date=ed_date,
            amount=ed_amount
        )
        
        return redirect('home')

    return render(request,'home.html')




def delete_item(request,delid):
    items = get_object_or_404(Expenses, id=delid)
    if request.method == 'POST':
        items.delete()
        messages.success(request, 'Item deleted successfully.')
        return redirect('home')  # Redirect to the view where you list items

    return render(request, 'delete.html',)

def signup(request):
    if request.method=='POST':
        user_name=request.POST['username']
        user_email=request.POST['email']
        user_password=request.POST['password']
        User.objects.create(
            name=user_name,
            email=user_email,
            password=user_password
        )
    return render(request,'signup.html')

def signin(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        
        
        if User.objects.filter(email=email,password=password).exists():
            data=User.objects.filter(email=email,password=password).values('email','id','name').first()
            request.session['email']=data['email']
            request.session['name']=data['name']
            request.session['id']=data['id']
            return redirect('home')

            
       
    return render(request,'signin.html')



def logout(request):
    del request.session['id']
    del request.session['email']
    del request.session['name']
    return redirect('signin')


def search(request):
    search_name=request.GET['search']
    if search_name:

        name=request.session.get('name')
        user=User.objects.get(id=request.session.get('id'))
        if user.is_admin:
            datas=Expenses.objects.filter(name__icontains=search_name)
        else:
            datas=Expenses.objects.filter(created_by=user,name__icontains=search_name)
        context={
            'datas':datas,
            'user':user,
            'name':name
        }
        return render(request,'home.html',context)

    # search_name=request.GET['search']
    # if search_name:
    #     name_search=Expenses.objects.filter(name__icontains=search_name)
       
    #     item=name_search
    #     context={
    #         'item':item
    #     }
    #     return render(request,'search.html',context)

def filter1(request):
    by_date=request.GET['search1']
    if by_date:
        date_search=Expenses.objects.filter(date__icontains=by_date)
       
        item1=date_search
        context={
            'item1':item1
        }

    return render(request,'filter.html',context)

