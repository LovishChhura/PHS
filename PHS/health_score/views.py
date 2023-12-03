from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from joblib import load
# import pandas as pd

modal=load('./models/health_score.joblib')
# Create your views here.
@login_required(login_url="/login/")
def index(request):
    return render(request,'health_check.html')

def health_index(request):
    if request.method=="POST":
        tempF=request.POST.get('tempF')
        pulse=request.POST.get('pulse')
        respr=request.POST.get('respr')
        bpsys=request.POST.get('bpsys')
        bpdia=request.POST.get('bpdia')
        popct=request.POST.get('popct')
        # healthFrame=pd.DataFrame([[float(tempF), float(pulse), float(respr), float(bpsys), float(bpdia), float(popct)]],columns=['TEMPF','PULSE','RESPR','BPSYS','BPDIAS','POPCT'])
        # pred=modal.predict((healthFrame))
        pred=modal.predict([[tempF,pulse,respr,bpsys,bpdia,popct]])
        if pred[0]==0:
            status="Excellent"
        elif pred[0]==1:
            status="Fine"
        elif pred[0]==2:
            status=="Need Care"
        elif pred[0]==3:
            status=="Medical Attention Needed"
        else:
            status=""
        params={"score":pred[0],"status":status}
    return render(request,'health_check.html',params)