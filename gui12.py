from cProfile import label
from tkinter import*
from tkinter import ttk
import model
import numpy as np

mainwindow=Tk()
mainwindow.title('Heart Disease')
#mainwindow.geometry('500x200')

GENDER=["Male",'Male','Female']
variable1=StringVar()

CP=['0 ->Typical Angina','0 ->Typical Angina','1 ->Atypical Angina','2 ->Non-Anginal Pain','3 ->Asymptomatic']
variable2=StringVar()
variable2.set(CP[0])

BS=["True","True","False"]
variable3=StringVar()
variable3.set(BS[0])

ANNGINA=["Yes","Yes","No"]
variable4=StringVar()
variable4.set(ANNGINA[0])
 
SLOPE=["0 ->Unsloping","0 ->Unsloping","1 ->Flat","2 ->Downsloping"]
variable5=StringVar()
variable5.set(SLOPE[0])
 
VESSAL=[0,0,1,2,3,4]
variable6=StringVar()
variable6.set(VESSAL[0])
 
THALASSEMIA=["3 ->Normal","3 ->Normal","6 ->Fixed Defect","7 ->Reverseable Defect"]
variable7=StringVar()
variable7.set(THALASSEMIA)

def showResult():
    age=int(etAge.get())
    trestbps=int(etBloodPressure.get())
    chol=int(etCholestrol.get())
    restecg=int(etElcCar.get())
    thalach=int(etThalach.get())
    oldpeak=int(etOldPeak.get())
    ca=int(variable6.get())
    if variable1.get()=="Male":
        gender=1
    else:
        gender=0
    if variable2.get()=="0 ->Typical Angina":
        cp=0
    elif variable2.get()=="1 ->Atypical Angina":
        cp=1
    elif variable2.get()=="2 ->Non-Anginal Pain":
        cp=2
    else:
        cp=3
    if variable3.get()=="False":
        fbs=0
    else:
        fbs=1
    if variable4.get()=="No":
        exang=0
    else:
        exang=1
    if variable5.get()=="1 ->Flat":
        slope=1
    elif variable5.get()=="2 ->Downsloping":
        slope=2
    else:
        slope=0
    
    if variable7.get()=="6 ->Fixed Defect":
        thal=6
    elif variable7.get()=="7 ->Reverseable Defect":
        thal=7
    else:
        thal=3
    input_data=(age,gender,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
    input_data_as_numpy_array=np.asarray(input_data)
    
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
    prediction=model.model.predict(input_data_reshaped)
    modelPrediction="MODEL PREDICTION IS"+str(prediction)
    
    if(prediction[0]==0):
        result="The Person Does Not Have Heart Problem"
    else:
        result="The Person Has Heart Problem"
    lblResult["text"]=modelPrediction+"\n"+result
    
#ADDING WIDGET
ProjectName=ttk.Label(mainwindow,text="Heart Disease Prediction",font=('Times New Roman',24,'bold'),foreground='green')
lblAge=ttk.Label(mainwindow,text="Enter Age of Person:")
etAge=ttk.Entry(mainwindow)
lblGender=ttk.Label(mainwindow,text="Gender:")
omGender=ttk.OptionMenu(mainwindow, variable1,*GENDER)
sperate1=ttk.Separator(mainwindow,orient='horizontal')
lblChestPain=ttk.Label(mainwindow,text="Enter the Chest Pain Value:")
omChestPain=ttk.OptionMenu(mainwindow, variable2, *CP)
     
lblBloodPressure=ttk.Label(mainwindow,text='Enter Resting Blood Pressure(in mm Hg):')
etBloodPressure=ttk.Entry(mainwindow)
     
sperate2=ttk.Separator(mainwindow,orient='horizontal')
lblCholestrol=ttk.Label(mainwindow,text="Enter Cholestrol Value(in mg/aL):")
etCholestrol=ttk.Entry(mainwindow)
lblSugar=ttk.Label(mainwindow,text="Enter Fasting Blood Sugar > 120mg/dL")
omSugar=ttk.OptionMenu(mainwindow, variable3,*BS)
     
sperate3=ttk.Separator(mainwindow,orient='horizontal')
lblElcCar=ttk.Label(mainwindow,text="Enter Resting Electrocardiography Measurement:")
etElcCar=ttk.Entry(mainwindow)
lblThalach=ttk.Label(mainwindow,text="Enter Thalach Value:")
etThalach=ttk.Entry(mainwindow)
     
sperate4=ttk.Separator(mainwindow,orient='horizontal')
lblAngina=ttk.Label(mainwindow,text="Enter Induced Angina:")
omAngina=ttk.OptionMenu(mainwindow, variable4,*ANNGINA)
lbOldPeak=ttk.Label(mainwindow,text="Enter Old Peak  Value:")
etOldPeak=ttk.Entry(mainwindow)

sperate5=ttk.Separator(mainwindow,orient='horizontal')
lblSlope=ttk.Label(mainwindow,text="Enter Slope of the Peak Ecercise ST Segment Value:")
omSlope=ttk.OptionMenu(mainwindow, variable5, *SLOPE)
lblVessal=ttk.Label(mainwindow,text="Enter Number of Major Vessels:")
omVessal=ttk.OptionMenu(mainwindow, variable6, *VESSAL)
sperate6=ttk.Separator(mainwindow,orient='horizontal')
lblThalassemia=ttk.Label(mainwindow,text="Enter Thalassemia Value:")
omThalassemia=ttk.OptionMenu(mainwindow, variable7, *THALASSEMIA)

sperate7=ttk.Separator(mainwindow,orient='horizontal')
sperate8=ttk.Separator(mainwindow,orient="horizontal")
btnShowRessult=ttk.Button(mainwindow,text="ShowResult",command=showResult)
lblResult=ttk.Label(mainwindow,text="",font=("Times New Roman",12,"bold"),foreground="green")

#ALLIGN WIDGET
ProjectName.grid(row=0,column=0,columnspan=3)
lblAge.grid(row=1,column=0)
etAge.grid(row=2,column=0)
lblGender.grid(row=1,column=1)
omGender.grid(row=2,column=1)

sperate1.grid(row=3,column=0,columnspan=2,ipadx=250,pady=10)
lblChestPain.grid(row=4,column=0)
omChestPain.grid(row=5,column=0)

lblBloodPressure.grid(row=4,column=1)
etBloodPressure.grid(row=5,column=1)

sperate2.grid(row=6,column=0,columnspan=2,ipadx=250,pady=10)
lblCholestrol.grid(row=7,column=0)
etCholestrol.grid(row=8,column=0)

lblSugar.grid(row=7,column=1)
omSugar.grid(row=8,column=1)

sperate3.grid(row=9,column=0,columnspan=2,ipadx=250,pady=10)
lblElcCar.grid(row=10,column=0)
etElcCar.grid(row=11,column=0)

lblThalach.grid(row=10, column=1)
etThalach.grid(row=11, column=1)

sperate4.grid(row=12,column=0,columnspan=2,ipadx=250,pady=10)
lblAngina.grid(row=13,column=0)
omAngina.grid(row=14,column=0)
lbOldPeak.grid(row=13,column=1)
etOldPeak.grid(row=14,column=1)

sperate5.grid(row=15,column=0,columnspan=2,ipadx=250,pady=10)
lblSlope.grid(row=16,column=0)
omSlope.grid(row=17,column=0)

lblVessal.grid(row=16,column=1)
omVessal.grid(row=17,column=1)

sperate6.grid(row=18,column=0,columnspan=2,ipadx=250,pady=10)
lblThalassemia.grid(row=19,column=0,columnspan=2)
omThalassemia.grid(row=20,column=0,columnspan=2)
sperate7.grid(row=21,column=0,columnspan=2,ipadx=250,pady=5)
sperate8.grid(row=22,column=0,columnspan=2,ipadx=250)#,pady=0)
btnShowRessult.grid(row=23,column=0,pady=10)
lblResult.grid(row=23,column=1)
mainwindow.mainloop()
 
 

 
     
     
   
    
        