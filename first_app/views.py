from django.shortcuts import render,HttpResponse,redirect
import bcrypt
from .models import *
from django.contrib import messages


def policeinfo(request):
     return render(request, 'policeinfo.html')
def driver(request):
    return render(request, 'driver.html')

def police(request):
    return render(request, 'police.html')

def login(request):
    return render(request, 'login.html')    

def addviolation(request):
    return render(request,'addviolation.html')

def showviolation(request):
    this_driver=Driver.objects.get(id=request.session['driver_id'])
    context={
        'allviolations': Violation.objects.all(),
        'this_driver':Driver.objects.get(id=request.session['driver_id'])
    }
    return render(request,'showviolation.html',context)


def home(request):
    return render(request,'home.html')
def reg(request):
        errors = Driver.objects.basic_validator(request.POST)
        users=Driver.objects.all()
        for user in users:
            if user.email==request.POST['email']:
                errors['email']="this email aleady exsist"
        for user in users:
            if user.notional_id==request.POST['nid']:
                errors['notional_id']="this notional_id is not valid"

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/login')
        password= request.POST['password']
        pw_hash= bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() 
        Driver.objects.create (
            full_name=request.POST['fullname'],
            birthday=request.POST['birthday'],
            notional_id=request.POST['nid'],
            city=request.POST['city'],
            blood_type=request.POST['blood_type'],
            email=request.POST['email'],
            password=pw_hash,
            phone_number=request.POST['phonenumber'],
        
        )
        name1=Driver.objects.last()
        request.session['full_name']=name1.full_name
        request.session['driver_id'] = name1.id

        return redirect('/driver')

def regpolice(request):
    
        errors = Police.objects.basic_validator2(request.POST)
        polices=Police.objects.all()
        for police in polices:
            if police.email==request.POST['email']:
                errors['email']="this email aleady exsist"

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/login')
        password= request.POST['password']
        pw_hash= bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() 
        Police.objects.create (
            full_name=request.POST['fullname'],
            birthday=request.POST['birthday'],
            city=request.POST['city'],
            email=request.POST['email'],
            password=pw_hash,
            phone_number=request.POST['phonenumber'],
        
        )
        name1=Police.objects.last()
        request.session['full_name_p']=name1.full_name
        request.session['police_id'] = name1.id

        return redirect('/policeinfo')

def signin(request):
    if request.POST['type']=='driver':
        driver = Driver.objects.filter(email=request.POST['email']) 
        if driver:
            logged_driver=driver[0]


            if bcrypt.checkpw(request.POST['password'].encode(),logged_driver.password.encode()):
                request.session['driver_id']= logged_driver.id
                request.session['full_name']= logged_driver.full_name
                return redirect('/driver')
            else:
                messages.error(request,"Your email or password is wrong try ag!")
                return redirect('/login')
        else:
            messages.error(request,"Your email or password is wrong try ag!")

        return redirect('/login')

    elif request.POST['type']=='police':
        police =Police.objects.filter(email=request.POST['email']) 
        if police:
            logged_police=police[0]


            if bcrypt.checkpw(request.POST['password'].encode(),logged_police.password.encode()):
                request.session['police_id'] = logged_police.id
                request.session['full_name_p']= logged_police.full_name
                return redirect('/policeinfo')
            else:
                messages.error(request,"Your email or password is wrong try ag!")
                return redirect('/login')
        else:
            messages.error(request,"Your email or password is wrong try ag!")

        return redirect('/login')

def add_vio(request):
    # -------------------------
    # Validator for valdition Table
    # -------------------------
    errors = Violation.objects.basic_validator3(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/addviolation')

    police1 = Police.objects.get(id = request.session['police_id'])
    driver1= Driver.objects.get(notional_id=request.POST['driver_id'])

    Violation.objects.create(
        location = request.POST['location'],
        violation_date = request.POST['violation_date'],
        expierd_date_violation = request.POST['ex_date'],
        resson = request.POST['reason'],
        driver = Driver.objects.get(notional_id=request.POST['driver_id']),
        police = police1,
        fees=request.POST['fees']

    )
    return redirect('/addviolation')



