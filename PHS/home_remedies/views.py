from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
import pandas as pd

df=pd.read_excel("./datasets/PHS_home_remedies_data.xlsx")
# Create your views here.
@login_required(login_url="/login/")
def index(request):
    return redirect('/#home_remedies')

@login_required(login_url="/login/")
def home_remedies_view(request, home_remedies):
    if home_remedies=="common_cold":
        hr="Common Cold"
    elif home_remedies=="headache":
        hr="Headache"
    elif home_remedies=="obesity":
        hr="Obesity"
    elif home_remedies=="kidney_stone":
        hr="Kidney Stone"
    elif home_remedies=="stomach_pain":
        hr="Stomach Pain"
    elif home_remedies=="muscle_ache":
        hr="Muscle Ache"
    elif home_remedies=="cough":
        hr="Cough"
    elif home_remedies=="nausea":
        hr="Nausea"
    else:
        hr="Malaria"
    ind=list(df[df['Name']==hr].index)
    h_remlist=df[df['Name']==hr].loc[ind[0]].to_list()
    remedyList=['Remedy1','Remedy1Detail','Remedy2','Remedy2Detail','Remedy3','Remedy3Detail','Remedy4','Remedy4Detail','Remedy5','Remedy5Detail']
    h_remdict={'name':hr,'image':f'/static/media/Home remedies/{hr}.jpeg','Remedy1':h_remlist[2],'Remedy1Detail':h_remlist[3],'Remedy2':h_remlist[4],'Remedy2Detail':h_remlist[5],'Remedy3':h_remlist[6],'Remedy3Detail':h_remlist[7],'Remedy4':h_remlist[8],'Remedy4Detail':h_remlist[9],'Remedy5':h_remlist[10],'Remedy5Detail':h_remlist[11]}
    return render(request,'home_remedies.html',h_remdict)