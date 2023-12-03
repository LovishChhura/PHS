from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/login/")
def index(request):
    return render(request,'health_assessment.html')

@login_required(login_url="/login/")
def bmi(request):
    if request.method=="POST":
        weight=request.POST.get('weight')
        height=request.POST.get('height')
        weight=float(weight)
        height=float(height)
        if height>0:
            height=height/100
        else:
            height=1
        bmis=weight / (height ** 2)
        bmi_s= str(f'{bmis:.2f}')
        if bmis<16:
            bmiStat="Severe Thinness"
        elif bmis>=16 and bmis<17:
            bmiStat="Moderate Thinness"
        elif bmis>=17 and bmis<18.5:
            bmiStat="Mild Thinness"
        elif bmis>=18.5 and bmis<25:
            bmiStat="Normal"
        elif bmis>=25 and bmis<30:
            bmiStat="Overweight"
        elif bmis>=30 and bmis<35:
            bmiStat="Obese Class 1"
        elif bmis>=35 and bmis<40:
            bmiStat="Obese Class 2"
        elif bmis>=40:
            bmiStat="Obese Class 3"
        else:
            bmiStat=""
        return render(request,"health_assessment.html",{'score':bmi_s,'statusB':bmiStat,'Fscore':float(bmi_s)})
    return render(request,'health_assessment.html')

@login_required(login_url="/login/")
def gr1(request):
    if request.method=="POST":
        level=request.POST.get('mgdlGR')
        level=float(level)
        if level<140:
            bs='Normal'
        elif level>=140 and level <199:
            bs='Prediabetic'
        elif level >=200:
            bs="Diabetic"           
        else:
            bs=""
        return render(request,"health_assessment.html",{'status1':bs,'level':level})
        
              
    return render(request,'health_assessment.html')

