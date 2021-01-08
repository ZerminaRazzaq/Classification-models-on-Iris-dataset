# -*- coding: utf-8 -*-
"""Naive Bayes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h1vu21iZ1JaFWiFPXHmGtmchLPDBfCco
"""

#first import the library
import pandas as pd
# datasert load
dataset = pd.read_excel("/content/Accident (1) (1).xlsx")

print(dataset.head()) #it prints 5 rows of data
#slicing
X_features_input = dataset.iloc[:, :-1].values #features[rows, columms]
print("X features input:\n",X_features_input)
y_label_output = dataset.iloc[:, 3].values #labels
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_features_input, y_label_output, test_size=0.20, random_state=5)
#x_train = 80% of our features data(input)
#x_test = 20% of our features data(input)
#y_train = 80% of our lable data(output)
#y_test = 20 % of pur lable data(output)
#imported the algorithms from library
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
# to train the model you have to use the function of "fit()"
# while traininf we only pass the 80 percent of our data
classifier.fit(X_train, y_train) # X_train = features #y_train= lable
# now we have to take prediction on testing data
y_pred = classifier.predict(X_test) #here we only pass the features
# from sklearn.metrics import classification_report, confusion_matrix
# print(confusion_matrix(y_test, y_pred))
#print(classification_report(y_test, y_pred))
from sklearn.metrics import accuracy_score
print('Accuracy Score: ', accuracy_score(y_pred, y_test)) #y_pred is the output