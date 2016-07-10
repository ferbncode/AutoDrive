# AutoDriving: A Supervised Learning Approach.
# 
# An autonomous car (driverless car, self-driving car, robotic car) is a vehicle that is capable of sensing its environment and navigating without human input. This is just a simple supervised learning approach for classification of action to be taken based on the properties of the inputs. However, combined with a reinforcement learning technique like Q-learning, the actions taken by the agent in the environment can be improved a lot. This ipython notebook is just presenting the the outline of the approach taken in the initial step: **A Supervised Approach to Action Selection**. Later this approach becomes the part of the reinforcement learning for an agent which enables it to take specific action in the present state.

# camera input
# sensor information
import numpy as np 
import pandas as pd
#from sklearn.svm import SVC
from sklearn.metrics import f1_score
from sklearn.cross_validation import train_test_split
#from sklearn.linear_model import LogisticRegression
X = pd.read_csv('dataSet/features.csv')
y = pd.read_csv('dataSet/labels.csv')

# ### Developing a Model
# 
# #### Defining a Performance Metric

def performance_metric(y_true, y_predict):
    '''This function uses f1 score as the evaluation metric as 'accuracy' is not a very good
    evaluation metric for biased datasets.'''
    score = f1_score(y_true, y_predict,average='weighted')
    return score

#testlabels = ['forward']*457
#performance_metric(y, testlabels)#debug
# Above shows that we have a very biased dataset
# ### Test Train Split

def train_test(X, y):
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.18, random_state=14)
	print("Training set has size {} and Test size has a size of {} examples".format(y_train.shape, y_test.shape))
	return X_train, X_test, y_train, y_test


def train_classifier(clf, X_train, y_train):
    clf.fit(X_train, y_train)
    print "Trained Model"
    return clf

def f1_labels(clf, features, target):
    y_pred = clf.predict(features)
    print y_pred
    return performance_metric(target, y_pred)

def predict_label(clf, testX):
	print testX.shape
	return clf.predict(testX)
#clf = SVC(gamma=.001,C=0.3,kernel='linear',random_state=21)
#clf = DecisionTreeClassifier(max_depth=3, random_state=35)

#train_classifier(clf, X_train,y_train)
#print predict_labels(clf, X_test, y_test)
#print predict_labels(clf, X_train, y_train)
#print (y_test)




