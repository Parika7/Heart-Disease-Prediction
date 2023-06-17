# importing  the liabraies
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve,roc_auc_score,auc
# loading the csv data as a pandas data frame
dataset=pd.read_csv("heart.csv")
# print features pf the dataset
print(dataset.columns)
# print first 5 rows data set
print(dataset.head(5))
# print last 5 rows of dataset
print(dataset.tail(5))
# number of rows and columns in the dataset
print(dataset.shape)
# getting some information about dataset
print(dataset.info())
# checking for missing values
print(dataset.isnull().sum())
# statistical measures about the data set
print(dataset.describe())
# checking the distribution of target of variable
print(dataset['target'].value_counts())
# 1-> defective heart
# 0-> healthy heart
# correlation matrix
plt.figure(figsize=(15,10))
sns.heatmap(dataset.corr(),annot=True)
plt.show()
plt.savefig("correlation figure")
# visualize the all dataset
fig=plt.figure(figsize=(15,20))
ax=fig.gca()
dataset.hist(ax=ax)
plt.show()
#visualize the count
sns.countplot(dataset['target'])
plt.show()
# occurance of cvd across age
plt.figure(figsize=(15,6))
sns.countplot(x='age',data=dataset,hue='cp')
plt.show()
#occurance of cvd across age
plt.figure(figsize=(16,7))
sns.displot(dataset[dataset['target']==0]['age'],kde=False,bins=50)
plt.title('age of heart disease')
plt.show()

#patients w.r.t gender
sns.countplot(data=dataset,x='sex',hue='target')
plt.title('Disease w.r.t Gender')
plt.show()

#Relationship between cholestrol and target
plt.figure(figsize=(16,7))
sns.displot(dataset[dataset['target']==0]['chol'],kde=False,bins=40)
plt.title('Relationship betweeen cholestrol and target')
plt.show()

#relationship between peak exercising(slope)and target
sns.countplot(data=dataset,x='slope',hue='target')
plt.title('peak exercising vs target')
plt.show()

#thalassemia relationship with the heart disease
sns.countplot(data=dataset,x='thal',hue='target')
plt.title('thal vs target')
plt.show()

# spliting the features and the target
x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,13].values
print(x)
print(y)

# spliting the data into training and testing data
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
print(x.shape,x_train.shape,x_test.shape)
print(y.shape,y_train.shape,y_test.shape)

# MODEL TRAINING 
# logistic regression model with training data
from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
# training the logistic regression model with training data
model.fit(x_train,y_train)

#model evaluation 
#accuracy score
#accuracy on training data
x_train_prediction=model.predict(x_train)

from sklearn.metrics import accuracy_score
training_data_accuracy=accuracy_score(x_train_prediction,y_train)

print("accuracy on training data:",training_data_accuracy)


# predicting the test set result
y_pred=model.predict(x_test)
print(y_pred)

#creating the confusion matrix
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)
sns.heatmap(cm,annot=True)
print("confusion matrix:\n",cm)
plt.show()

# accuracy on the test data
x_test_prediction=model.predict(x_test)
test_data_accuracy=accuracy_score(x_test_prediction,y_test)
print("accuracy an testing data:",test_data_accuracy)

#Plotting the ROC curve
prob_lr=model.predict_proba(x_test)
auc_lr=roc_auc_score(y_test,prob_lr[:,1])
fprlr,tprlr,_=roc_curve(y_test,prob_lr[:,1])
roc_arc=auc(fprlr,tprlr)
plt.plot(fprlr,tprlr,label="AUC=%.2f"%auc_lr)
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC curve for Logistic Regression")
plt.plot([0,1],[0,1],"--")
plt.legend()
plt.show()

# #building a predictive system
# age=int(input("enter the age of the person:"))
# gender=int(input("enter the gender of peson either 0 or 1(0=female;1=male):"))
# cp=int(input("enter the chest pain value either 0,1,2,3 where 0=typical angina;1=atypical angina;2=non -anginal pain;3=asympotatic:"))
# trestbps=int(input('enter the value of person resting blood pressure in(mm Hg):'))
# chol=int(input("enter the value of cholestrol in mg/al:"))
# fbs=int(input('enter the value of person fasting blood sugar(>120mg/dl,1=true;0=false):'))
# restecg=int(input('enter the value of resting electrocardiography measurement:'))
# thalach=int(input('enter the value of thalach:'))
# exang=int(input('enter the value of induced angina(1=yes;0=no):'))  
# oldpeak=int(input('enter the value of old peak:'))   
# slope=int(input('enter the value of slope of the peak ecercise ST segment(0=unsloping,1=flat,2= downslopping):'))
# ca=int(input('enter the value of number of major vessels(0-4):'))
# thal=int(input('enter the value of thalassemia(3=normal;6=fixed defect;7=reverseable defect):'))

# #passing all the values into a single tuple
# input_data=(age,gender,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)

# #change the input data to na numpy array
# input_data_as_numpy_array=np.asarray(input_data)

# #reshape the numpy array as we as are predicting for only one instances
# input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
# prediction=model.predict(input_data_reshaped)
# print("MODEL PREDICTION IS",prediction)

# if(prediction[0]==0):
#     print("the person does not have heart disease")
# else:
#     print("the person has heart disease")