from classifier import *
#from moveCar import *
# Comment above import if you are not using a raspberry pi and just 
# testing the classifier
from sklearn.tree import DecisionTreeClassifier
from captureExtractFeatures import *


X_train, X_test, y_train, y_test = train_test(X, y)
clf = DecisionTreeClassifier(max_depth=3, random_state=35)
clf = train_classifier(clf, X_train, y_train)
# the classifier has a 0.77 f1 score on the test set. (can be improved by using sophisticated hardware for
# sensors and better training set
totalTime = int(raw_input("Enter the amount for which the agent should try to perform\
 in the environment: "))

for time_unit in range(totalTime):
	#incomplete
	captureImage()
	imgArray = convertToKClusteredImage('photo.jpg')
	im = make2dBlueMatrix(imgArray)

	pred_action = predict_label(clf, im)

	print pred_action

	#takeAction(action = pred_action)



