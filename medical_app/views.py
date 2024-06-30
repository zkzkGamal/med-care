from django.shortcuts import render ,redirect
from django.contrib import auth
from django.contrib.auth.models import User , Group
from django.contrib import messages
from .decoretors import *
from .models import *
from django.contrib.auth.decorators import login_required


# Create your views here.

@authandicated
def signup(request):
    return render(request , 'signup.html')
@authandicated
def login(request):
    email1=request.POST.get('email')
    password1=request.POST.get('password')
    msg = ''
    if request.method == 'POST':
        user = User.objects.get(email = email1)
        user1 = auth.authenticate(request , username = user.username , password = password1)
        if user1 is not None:
            auth.login(request , user1)
            next_url = request.GET.get('next')
            if next_url == '' or next_url == None:
                next_url = 'Home'
                return redirect(next_url)
            else:
                msg = messages.error('please cheak username or pass')
    return render(request , 'Login.html' , {'msg':msg})
@authandicated
def medical_sign(request):
    first_name=request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    age = request.POST.get('age')
    mobilenumber = request.POST.get('mobilenumber')
    address = request.POST.get('address')
    email = request.POST.get('email')
    password = request.POST.get('password')
    NationalId=request.POST.get('NationalId')
    medicalType = request.POST.get('choosemedicalprovider')
    msg = ''
    if request.method == 'POST':
        username = first_name + last_name
        user = User.objects.create_user(username = username , password = password , email = email)
        profile1 = profile( user = user , frist_name = first_name , last_name = last_name , age = age 
                       , phone = mobilenumber , address = address , nationalID = NationalId ,
                       medicalType = medicalType , email = email)
        authUser = auth.authenticate(request , username = username , email = email , password = password)
        if authUser is not None:
            profile1.save()
            group = Group.objects.get(name = 'doctor')
            user.groups.add(group)
            auth.login(request , authUser)
            next_url = request.GET.get('next')
            if next_url == '' or next_url == None:
                next_url = 'Home'
                return redirect(next_url)
            else:
                msg = messages.error('please cheak username or pass')
    return render(request , 'medical-signup.html',{'msg':msg})
@authandicated
def prtiant_sign(request):
    first_name=request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    age = request.POST.get('age')
    mobilenumber = request.POST.get('mobilenumber')
    address = request.POST.get('address')
    email = request.POST.get('email')
    password = request.POST.get('password')
    confirmpassword = request.POST.get('confirmpassword')
    NationalId=request.POST.get('NationalId')
    msg = ''
    if request.method == 'POST':
        username = first_name + last_name
        user = User.objects.create_user(username=username , password=password ,email=email)
        profile1 = profile(user = user , frist_name = first_name , last_name = last_name , age = age 
                       , phone = mobilenumber , address = address , nationalID = NationalId , email = email )
        authUser = auth.authenticate(request , username = username , email = email , password = password)
        if authUser is not None:
            profile1.save()
            group = Group.objects.get(name = 'petiant')
            user.groups.add(group)
            auth.login(request , authUser)
            next_url = request.GET.get('next')
            if next_url == '' or next_url == None:
                next_url = 'Home'
                return redirect(next_url)
            else:
                msg = messages.error('please cheak username or pass')
    return render(request , 'petiant-signup.html' , {'msg':msg})
def logoutUser(request):
    auth.logout(request)
    return redirect('login')
def Home(request):
    user = request.user
    doctor1 = user.groups.filter(name='doctor').exists()
    doctors = doctor.objects.all()
    listt = []
    for e in doctors:
        listt.append(e.specialist)
    listt = list(set(listt))
    return render(request,'index.html',{'doctor':doctor1 , 'specialist':listt})
@login_required(login_url = 'login')
@only_Doctor
def profileReception(request):
    user = request.user
    reception = profile.objects.get(user = user)
    doc = doctor.objects.filter(reception = reception)
    doc_img = ''
    if doc:
        doc = doctor.objects.get(reception = reception)
        doc_img = doc.image
    doctor1 = user.groups.filter(name='doctor').exists()
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    address = request.POST.get('address')
    email = request.POST.get('email')
    if request.method == 'POST':
        frist_name , last_name = name.split(' ')
        reception.frist_name = frist_name
        reception.last_name = last_name
        reception.phone = phone
        reception.address = address
        reception.email = email
        reception.save()
    
    return render(request , 'reception.html' , {'reception': reception , 'doctor': doctor1, 'doc_img':doc_img})
@login_required(login_url = 'login')
@only_Doctor
def DoctorProfile(request):
    user = request.user
    imagesList = ''
    reception = profile.objects.get(user = user)
    doc = doctor.objects.filter(reception = reception)
    name = request.POST.get('name')
    about = request.POST.get('about')
    specialist = request.POST.get('specialist')
    location = request.POST.get('location')
    price = request.POST.get('price')
    years_of_experience = request.POST.get('years_of_experience')
    gender = request.POST.get('gender')
    if doc:
        doc = doctor.objects.get(reception = reception)
        imagesList = clinicPICs.objects.filter(doctor = doc)
        if imagesList:
            imagesList = clinicPICs.objects.filter(doctor = doc)
    if request.POST.get('save'):
        data = doctor(reception = reception , name = name , about = about
                        ,specialist =specialist , location = location, price=price
                        , years_of_experience=years_of_experience, gender=gender)
        if request.method == 'POST':
            data.save()
            doctor_pro = doctor.objects.get(reception = data.reception)
            images = request.FILES.getlist('images')
            for img in images:
                pictures = clinicPICs.objects.create(
                    doctor = doctor_pro,
                    pic = img
                )
            return redirect('profile')
    elif request.POST.get('submit-img'):
        doc_img = request.FILES.get('cover')
        doc.image = doc_img 
        if request.method == 'POST':
            doc.save()
            return redirect('profile')
    elif request.POST.get('update'):
        doc.name = name
        doc.about = about
        doc.location = location
        doc.gender = gender
        doc.price = price
        doc.years_of_experience = years_of_experience
        doc.specialist = specialist
        if request.method == 'POST':
            doc.save()
            images = request.FILES.getlist('images')
            oldImage = clinicPICs.objects.filter(doctor = doc)
            oldImage.delete()
            for img in images:
                pictures = clinicPICs.objects.get_or_create(
                    doctor = doc,
                    pic = img
                )
            return redirect('profile')
    
    return render(request , 'profile.html' , {'doctor1':doc , 'images': imagesList})

from .filters import DoctorFilter as Filter
def cards(request):
    doctors = doctor.objects.all()
    myFilter = Filter(request.GET, queryset=doctors)
    doctors= myFilter.qs
    user = request.user
    doctor1 = user.groups.filter(name='doctor').exists()
    return render(request , 'Specialtais.html' , {'doctors':doctors , 'doctor':doctor1 , 'filter':myFilter})
def special(request, sp):
    doctors = doctor.objects.filter(specialist = sp)
    user = request.user
    doctor1 = user.groups.filter(name='doctor').exists()
    return render(request , 'Specialtais.html',{'doctors':doctors , 'doctor':doctor1})
def Doctor_detail(request , slug):
    detail = doctor.objects.get(slug = slug)
    user = request.user
    doctor1 = user.groups.filter(name='doctor').exists()
    clinic = clinicPICs.objects.filter(doctor = detail)
    return render(request , 'doctor-detail.html' , {'doctor':doctor1,'doctor1':detail , 'clinic':clinic})

