from django.shortcuts import render
import numpy as np
from cmath import nan
import pickle as pi
from sklearn.impute import SimpleImputer

# Create your views here.

def check(results):
        if results == 1 :
            results1 = ' you are sick '
        elif results == 0 :
            results1 = 'you are not sick '
        else:
            results1 = 'insert you results'
        return results1

def Scaling(xx):
    fill_values = SimpleImputer(missing_values=np.nan, strategy="mean")
    xx = fill_values.fit_transform(xx)
    return xx

def inputDiabetes(request):
    if request.method=='POST': 
        age2 = request.POST.get('age2')
        Pregnancies = request.POST.get('Pregnancies')
        Glucose = request.POST.get('Glucose')
        BloodPressur = request.POST.get('BloodPressur')
        SkinThickness = request.POST.get('SkinThickness')
        Insulin = request.POST.get('Insulin')
        BMI_input = request.POST.get('BMI')
        DPFunction = request.POST.get('DPFunction')
        data = [Pregnancies,Glucose,
                BloodPressur,SkinThickness,
                Insulin,BMI_input,DPFunction,age2] 
        return data
    else:
        return None
    
def inputHeart(request):
    if request.method=='POST': 
        ag1 = request.POST.get('ag1')
        gender = request.POST.get('gender')
        impluse = request.POST.get('impluse')
        pressureHigh = request.POST.get('pressureHigh')
        pressureLow = request.POST.get('pressureLow')
        Glucose1 = request.POST.get('Glucose1')
        Kcm = request.POST.get('Kcm')
        troponin = request.POST.get('troponin')
        data = [ag1,gender,impluse,pressureHigh,
                pressureLow,Glucose1,Kcm,
                troponin] 
        return data
    else:
        return None


def Home(request):
    user = request.user
    doctor = user.groups.filter(name='doctor').exists()
    return render(request,'main-AI.html' , {'doctor':doctor})

def heart(request):
    user = request.user
    doctor = user.groups.filter(name='doctor').exists()
    if inputHeart(request):
        values = [inputHeart(request)]
        scaling_input = Scaling(values)
        loaded_model = pi.load(open('AI_app/modelHeart1.sav','rb'))
        predicted_date = loaded_model.predict(scaling_input)
    else:
        predicted_date = ''
    return render(request , 'Heart.html' , {'doctor':doctor , 'r3':check(predicted_date)})
def diabetes(request):
    user = request.user
    doctor = user.groups.filter(name='doctor').exists()
    if inputDiabetes(request):
        values = [inputDiabetes(request)]
        scaling_input = Scaling(values)
        loaded_model = pi.load(open('AI_app/modelDiabetes3.sav','rb'))
        predicted_date = loaded_model.predict(scaling_input)
    else:
        predicted_date = ''
    return render(request , 'Diabetes.html', {'doctor':doctor,'r3':check(predicted_date)})