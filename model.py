#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle 


# In[2]:


#read the csv file
data_set=pd.read_csv("heart.csv")
print(data_set)


# In[3]:


x=data_set.iloc[:,:13].values
y=data_set.iloc[:,13].values


# In[4]:


print("Shape of the Dataset:",data_set.shape)
print("Size of the Data:",data_set.size)
print(data_set.describe)
data_set.head(10)


# In[5]:


#Analyzing the Dataset
plt.figure(figsize=(16,6))
sns.countplot(x="age",data=data_set)


# In[6]:


sns.countplot(x="sex",data=data_set)


# In[7]:


sns.countplot(x="target",data=data_set)


# In[8]:


#plt.figure(figsize=(16,6))
sns.barplot("cp","target",data=data_set)


# In[9]:


sns.heatmap(data_set.isnull())


# In[10]:


from sklearn import model_selection
x_train,x_test,y_train,y_test=model_selection.train_test_split(x,y,test_size=0.18,random_state=5)


# In[11]:


from sklearn.tree import DecisionTreeClassifier  
regressor= DecisionTreeClassifier(criterion='entropy', random_state=0)  
regressor.fit(x_train, y_train)
y_predict=regressor.predict(x_test)


# In[12]:


from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
a=accuracy_score(y_test,y_predict)
c=confusion_matrix(y_test,y_predict)
print(a,c)


# In[13]:


from sklearn.linear_model import LogisticRegression
regressor=LogisticRegression(random_state=0)
regressor.fit(x_train,y_train)
a=accuracy_score(y_test,y_predict)
c=confusion_matrix(y_test,y_predict)
print(a,c)


# In[14]:


pickle.dump(regressor,open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[2, 9, 6,8,12,2,3,5,6,8,1,23,3]]))

