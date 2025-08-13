from django.shortcuts import render, redirect
from defects.models import defectData, Defect_Screenshot, TesterData, DeveloperData,User
from django.contrib.auth.decorators import login_required
from defects.forms import DefectEditForm, DefectAddForm,FilterDefectForm
from django.core.paginator import Paginator
from defects.utils import send_email_view


# Create your views here.
@login_required(login_url='login')
def defectList(request):
    defect = defectData.objects.all()
    defect_count = len(defect)
    paginator= Paginator(defect,4)
    page_num = request.GET.get('pg')
    defect = paginator.get_page(page_num)

    # loggedin user details
    user = request.user
    show_button = False
    try :
        tester = TesterData.objects.get(tester_name=user)
        if tester.is_admin :
            show_button = True
    except TesterData.DoesNotExist :
        pass

    context = {
        'defect':defect,
        'defect_count':defect_count,
        'show_button':show_button
    }
    return render(request,'defects/alldefects.html',context)

@login_required(login_url='login')
def desc(request,id=0):
    defect = defectData.objects.get(id=id)
    defect1 = Defect_Screenshot.objects.filter(defect=defect)
    context = {
        'defect':defect,
        'defect1':defect1
    }
    return render(request,'defects/description.html',context)

@login_required(login_url='login')
def edit_defect(request,id=0):
    defect = defectData.objects.get(id=id)
    if request.method == 'POST':
        form = DefectEditForm(request.POST,instance=defect)
        if form.is_valid():
            form.save()
            return redirect('alldefects')
    else:
        form = DefectEditForm(instance=defect)
    return render(request,'defects/editdefect.html',{'form':form})

@login_required(login_url='login')
def add_defect(request):
    if request.method == 'POST':
        form = DefectAddForm(request.POST)
        if form.is_valid():
            dev_name = form.cleaned_data['assigned_to']
            print(dev_name)
            user = User.objects.get(username=dev_name)
            print(user.email)
            form.save()
            send_email_view(user.email)
            return redirect('alldefects')
    else:
        form = DefectAddForm()
    return render(request,'defects/add_defect.html',{'form':form})

# @login_required(login_url='login')
def filter_dev(request):
    if request.method =='POST':
        form = FilterDefectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['assigned_to']
            user = User.objects.get(username=name)
            dev_name =  DeveloperData.objects.get(dev_name=user)
            dev_defects = defectData.objects.filter(assigned_to=dev_name)
            print(dev_name)
            print(dev_defects)
    else:
        form =FilterDefectForm()
    return render(request,'defects/filter_defects.html',{'form':form})
@login_required(login_url='login')
def completed_defects(request):
    # Filter using the correct field name
    completed = defectData.objects.filter(defect_status__iexact ='Completed').order_by('-id')

    # Count for display
    completed_count = completed.count()

    # Pagination
    paginator = Paginator(completed, 4)
    page_num = request.GET.get('pg')
    completed = paginator.get_page(page_num)

    context = {
        'defect': completed,
        'defect_count': completed_count
    }
    return render(request, 'defects/completed_defects.html', context)

@login_required(login_url='login')
def pending_defects(request):
    # Filter using the correct field name
    pending = defectData.objects.exclude(defect_status__iexact ='Completed').order_by('-id')

    # Count for display
    pending_count = pending.count()

    # Pagination
    paginator = Paginator(pending, 4)
    page_num = request.GET.get('pg')
    pending = paginator.get_page(page_num)

    context = {
        'defect': pending,
        'defect_count': pending_count
    }
    return render(request, 'defects/pending_defects.html', context)
