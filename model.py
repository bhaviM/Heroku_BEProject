# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 17:40:40 2019

@author: LENOVO
"""

import numpy as np
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import pydotplus
from IPython.display import Image
import pickle
import requests
import json

#loading dataset
df=pd.read_csv("UserData_1.csv",encoding="ISO-8859-1")

#preprocessing 
#converting age to ranges 0 to 2
#and converting categorical values to encoded values
bins = [13,35,60,100]
labels=[0,1,2]
df['Age'] = pd.cut(df['Age'], bins=bins, labels=labels, include_lowest=True)

x_fe=['Gender','Age','RS']
x=df[x_fe]
y_fe=['amusement_park','night_club','cafes','museum','shopping_mall','park','church','hindu_temple','art_gallery','casino','library','zoo']
y=df[y_fe]
from sklearn import preprocessing
x=x.apply(preprocessing.LabelEncoder().fit_transform)

print(x)
print(y)

#algorithm

x_test=[[1,0,0]]
y1=df['amusement_park']
clf1=DecisionTreeClassifier(criterion='entropy')
model1=clf1.fit(x,y1)
pred1=model1.predict(x_test)
print(pred1)
dot_data=tree.export_graphviz(model1,out_file=None,feature_names=x_fe,class_names=['no','yes'],filled=True)
graph=pydotplus.graph_from_dot_data(dot_data)
Image(graph.create_png())
graph.write_png("dtree_for_amusement_park.png")

y2=df['night_club']
clf2=DecisionTreeClassifier(criterion='entropy')
model2=clf2.fit(x,y2)
pred2=model2.predict(x_test)
print(pred2)

y3=df['cafes']
clf3=DecisionTreeClassifier(criterion='entropy')
model3=clf3.fit(x,y3)
pred3=model3.predict(x_test)
print(pred3)

y4=df['museum']
clf4=DecisionTreeClassifier(criterion='entropy')
model4=clf4.fit(x,y4)
pred4=model4.predict(x_test)
print(pred4)

y5=df['shopping_mall']
clf5=DecisionTreeClassifier(criterion='entropy')
model5=clf5.fit(x,y5)
pred5=model5.predict(x_test)
print(pred5)

y6=df['park']
clf6=DecisionTreeClassifier(criterion='entropy')
model6=clf6.fit(x,y6)
pred6=model6.predict(x_test)
print(pred6)

y7=df['church']
clf7=DecisionTreeClassifier(criterion='entropy')
model7=clf7.fit(x,y7)
pred7=model7.predict(x_test)
print(pred7)

y8=df['hindu_temple']
clf8=DecisionTreeClassifier(criterion='entropy')
model8=clf8.fit(x,y8)
pred8=model8.predict(x_test)
print(pred8)

y9=df['art_gallery']
clf9=DecisionTreeClassifier(criterion='entropy')
model9=clf9.fit(x,y9)
pred9=model9.predict(x_test)
print(pred9)

y10=df['casino']
clf10=DecisionTreeClassifier(criterion='entropy')
model10=clf10.fit(x,y10)
pred10=model10.predict(x_test)
print(pred10)

y11=df['library']
clf11=DecisionTreeClassifier(criterion='entropy')
model11=clf11.fit(x,y11)
pred11=model11.predict(x_test)
print(pred11)

y12=df['zoo']
clf12=DecisionTreeClassifier(criterion='entropy')
model12=clf12.fit(x,y12)
pred12=model12.predict(x_test)
print(pred12)

# Saving model to disk
pickle.dump(model1, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print ("Loaded Decision tree model :: ",model)
print(model.predict([[0,0,1]]))