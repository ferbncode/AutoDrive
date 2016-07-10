import cv2
import requests
from os import system
from sklearn.cluster import KMeans
import numpy as np
import Image



def convertToKClusteredImage(img):
	print img
	system("convert {} -resize 30x28! {}.png".format(img, img))
	# figured out the worst method but the easiest implementation
	a, b, c = cv2.imread('{}.png'.format(img)).shape
	im = cv2.imread('{}.png'.format(img)).transpose(2,0,1).reshape(3, -1).transpose()
	# Don't ask. I know its shit code
	clusterer = KMeans(n_clusters=2, max_iter=50, random_state=1)
	preds = clusterer.fit_predict(im)
	for iter in range(len(im)):
		im[iter] = clusterer.cluster_centers_[preds[iter]]
	im = np.fliplr(im)
	im = im.reshape(a, b, c)
	img = Image.fromarray(im)
	#Image.save('img_clustered.png')
	print im.shape
	return im

def make2dBlueMatrix(img):
	print img.shape
	imgBlueIntensities = img.transpose(2, 0, 1).reshape(3, -1)
	print imgBlueIntensities.shape
	return imgBlueIntensities[0]

def captureImage():
	url = "http://192.168.43.134:8080/photo.jpg"
	response = requests.get(url)
	if response.status_code  == 200:
		f= open("photo.jpg", 'wb')
		f.write(response.content)
		f.close()

	
