#Import Dependencies 
import pandas as pd
import os
import numpy as np
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

#Read Dataset
dataset = pd.read_csv('harden.csv')

#Convert Minutes from object to float
time = dataset['MP'].str.split(':', expand=True).astype(float)
time_ = time[1] / 60
dataset['MINUTES'] = time[0] + time_

#Convert RESULT column to binary W and L
df2 = dataset['RESULT']
p = df2.to_string()
l = p.split()
j = []
for k in range(1, len(l), 3):
    if 'W' or "L" in l[k]:
        if l[k] == "W": j.append("W");
        elif l[k] == "L": j.append("L")

#Create New column with binary RESULTS
dataset["RESULTS"] = j

#Filter dataset to only include desired stats
dataset = dataset.filter(["MINUTES", 'PTS',"TRB", "AST", "GmSc", 'RESULTS'])

#Class distribution
dataset.groupby('RESULTS').size()

#split out validation
array = dataset.values
X = array[:,0:5]
y =array[:,5]
X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=1)

#Make predictions
model = LinearDiscriminantAnalysis()
model.fit(X_train, Y_train)
predictions = model.predict(X_validation)

#Print Results
ml_data = print(accuracy_score(Y_validation, predictions))
    

def return_values():
    return ml_data