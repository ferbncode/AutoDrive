from classifier import *
#from moveCar import *
# Comment above import if you are not using a raspberry pi and just 
# testing the classifier
from sklearn.tree import DecisionTreeClassifier
from captureExtractFeatures import *


X_train, X_test, y_train, y_test = train_test(X, y)
clf = DecisionTreeClassifier(max_depth=3, random_state=35)
clf = train_classifier(clf, X_train, y_train)

totalTime = raw_input("Enter the amount for which the agent should try to perform\
 in the environment: ")

#incomplete



