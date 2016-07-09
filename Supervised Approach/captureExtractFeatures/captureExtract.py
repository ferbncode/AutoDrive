import cv2
import requests
from os import system
from sklearn.cluster import KMeans
import numpy as np
import Image



def convertToKClusterdImage(img):
	system("convert {} -resize 30x28! {}.png".format(img))
	# figured out the worst method but the easiest implementation
	a, b, c = cv2.imread(img).shape
	im = cv2.imread(img).transpose(2,0,1).reshape(3, -1).transpose()
	# Don't ask. I know its shit code
	clusterer = KMeans(n_clusters=2, max_iter=50, random_state=1)
	preds = clusterer.fit_predict(im)
	for iter in range(len(im)):
		im[iter] = clusterer.cluster_centers_[preds[iter]]
	im = np.fliplr(im)
	im = im.reshape(a, b, c)
	img = Image.fromarray(im)
	Image.save('img_clustered.png')
	return im

def make2dBlueMatrix(img):
	imgBlueIntensities = img.transpose(2, 0, 1).reshape(3, -1)[0]
	return imgBlueIntensities[0]

def captureImage():
	system("wget http://192.168.43.1:8080/photo.jpg")



	
