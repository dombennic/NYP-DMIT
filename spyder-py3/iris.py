# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 10:07:04 2021

@author: domin
"""

from  sklearn import  datasets
iris=datasets.load_iris()

x=iris.data
y=iris.target

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.5)
"""
from sklearn import tree
classifier=tree.DecisionTreeClassifier()

"""

from sklearn import neighbors
classifier=neighbors.KNeighborsClassifier()

classifier.fit(x_train,y_train)

predictions=classifier.predict(x_test)

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,predictions))


"""
from  sklearn import  datasets
iris=datasets.load_iris()
x=iris.data
y=iris.target
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.5)
from sklearn import tree
classifier=tree.DecisionTreeClassifier()
classifier.fit(x_train,y_train)
predictions=classifier.predict(x_test)
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,predictions))
"""