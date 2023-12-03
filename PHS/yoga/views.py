from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
import pandas as pd

df=pd.read_excel("./datasets/final_asan1_1.xlsx")
# Create your views here.
@login_required(login_url="/login/")
def index(request):
    return redirect('/#yoga')

@login_required(login_url="/login/")
def yoga_view(request, yoga_name):
    L1="Beginners"
    L2="Intermediate"
    L3="Advanced"
    if yoga_name=="standing_pose":
        y_name="Standing"
    elif yoga_name=="sitting_pose":
        y_name="Sitting"
    elif yoga_name=="stomach_pose":
        y_name="Laying_on_Stomach_Pose"
    elif yoga_name=="back_pose":
        y_name="Laying_on_Back"
    elif yoga_name=="balancing_pose":
        y_name="Balancing"
    else:
        y_name="Eyes"
        L2="Beginners"
        L3="Beginners"
    filtered_df=df[(df[y_name]==1) & (df['Level']==L1)]
    num_random_rows = 4  # Adjust this number as needed
    # Get random rows from the filtered DataFrame
    random_rows = filtered_df.sample(n=num_random_rows,replace=True)
    filtered_df2=df[(df[y_name]==1) & (df['Level']==L2)]
    random_rows2 = filtered_df2.sample(n=num_random_rows,replace=True)
    filtered_df3=df[(df[y_name]==1) & (df['Level']==L3)]
    random_rows3 = filtered_df3.sample(n=num_random_rows,replace=True)
    beginner = [{'name': i, 'link': j, 'image': f'/static/media/FULL_Yoga/{i.lower()}.jpg'} for i, j in zip(random_rows.AName.to_list(), random_rows.Youtube_Video_Link.to_list())]
    intermediate = [{'name': i, 'link': j, 'image': f'/static/media/FULL_Yoga/{i.lower()}.jpg'} for i, j in zip(random_rows2.AName.to_list(), random_rows2.Youtube_Video_Link.to_list())]
    advance = [{'name': i, 'link': j, 'image': f'/static/media/FULL_Yoga/{i.lower()}.jpg'} for i, j in zip(random_rows3.AName.to_list(), random_rows3.Youtube_Video_Link.to_list())]
    
    print(f'beginner is {beginner},intermediate is {intermediate} , advance is {advance}')
    
    return render(request,'yoga.html',{'beginners': beginner,"intermediate":intermediate, 'advance': advance,'name':yoga_name.capitalize()})