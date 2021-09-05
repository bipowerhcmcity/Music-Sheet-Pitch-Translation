from __future__ import print_function 
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
import random
np.random.seed(11)
import cv2
import StaffLineRemoval

file_handle = cv2.imread("sheet_2.jpg")
GRAY = StaffLineRemoval.StaffLineRemoval(file_handle)
# GRAY = cv2.GaussianBlur(GRAY,(5,5),0)

win_size = 5
K = 2

def EDist(a, b):
	temp_1 = a.flatten()
	temp_2 = b.flatten()
	return (temp_1 - temp_2).dot(temp_1 - temp_2)

def FindLabel(x, centers):
	MIN = EDist(x, centers[0])
	label = 0
	for i in range(1,len(centers)):
		temp = EDist(x, centers[i])
		if MIN > temp:
			MIN = temp
			label = i
	return label
def Kmean_init_centers(X,K):
	#return X[np.random.choice(X.shape[0], K, replace=False)]
	center = []
	size = X.shape
	for i in range(K):
		height = random.randint(0, size[0] - win_size + 1)
		width = random.randint(0, size[1] - win_size + 1)
		center.append(X[height:height + win_size, width:width + win_size])
	return center#[np.zeros((win_size,win_size), dtype = np.uint8)]*3
def Kmean_assign_label(X, centers):
	#D = [FindLabel(X[i], centers) for i in range(len(X))](
	size = X.shape
	D = np.zeros((size[0] - win_size + 1, size[1] - win_size + 1))
	for i in range(size[0] - win_size + 1):
		for j in range(size[1] - win_size + 1):
			D[i, j] = FindLabel(X[i:i + win_size, j:j + win_size], centers)
	return D

def UpdateCenters(X, label, K):
	centers = []
	size = label.shape
	for i in range(K):
		temp = np.zeros((win_size, win_size))#, dtype = np.uint8)
		count = 0
		for j in range(size[0]):
			for k in range(size[1]):
				if label[j, k] == i:
					temp = temp + X[j:j+win_size, k:k+win_size]
					count = count + 1
		if count == 0:
			centers.append(temp)
		else:
			centers.append(temp/count)
	return (centers)

#def HasConverge(old_center, new_center):
#    return (set([tuple(a) for a in old_center]) == 
#        set([tuple(a) for a in new_center]))
def HasConverge(old_center, new_center):
	threshold = 0.02
	COST = 0
	for i,j in zip(old_center, new_center):
		COST = COST + EDist(i,j)
	return (COST < threshold)


def Kmeans(X, K):
	centers = Kmean_init_centers(X, K)
	it = 0
	for i in range(5):
		it = it + 1
		print("ITERATTION: ", it)
		label = Kmean_assign_label(X, centers)
		print(label)
		new_centers = UpdateCenters(X, label, K)
		print(new_centers)
		if HasConverge(centers, new_centers):
			break
		centers = new_centers

	return centers, label


centers, label = Kmeans(GRAY, K)
print(label)
print(centers)
size = label.shape
cout_1 =0
cout_2 =0
cout_3 = 0
for i in range(size[0]):
	for j in range(size[1]):
		if label[i, j] == 1:
			cout_1 = cout_1 + 1
		elif label[i,j] == 2:
			cout_2 = cout_2 + 1
		else:
			cout_3 = cout_3 + 1

print(cout_1, "\t", cout_2, "\t", cout_3)

red = np.zeros((win_size, win_size, 3), dtype = np.uint8)
blue = np.zeros((win_size, win_size, 3), dtype = np.uint8)
green = np.zeros((win_size, win_size, 3), dtype = np.uint8)

red[0:win_size, 0:win_size, 0] = 255
blue[0:win_size, 0:win_size, 1] = 255
green[0:win_size, 0:win_size, 2] = 255

img_shape = GRAY.shape
out = np.zeros((img_shape[0], img_shape[1], 3), dtype = np.uint8)
for i in range(size[0]):
	for j in range(size[1]):
		if label[i,j] == 1:
			out[i:i+win_size, j:j+win_size, 0:3] = red
		elif label[i,j] ==2:
			out[i:i+win_size, j:j+win_size, 0:3] = green
		else:
			out[i:i+win_size, j:j+win_size, 0:3] = blue
cv2.imshow("alfsfsdf", out)
cv2.waitKey(0)
#kernel = np.zeros((win_size, win_size), dtype=np.uint8)
#kernel[0, 0:win_size] = 1
#kernel[win_size-1, 0:win_size] = 1
#kernel[0:win_size, 0] = 1
#kernel[0:win_size, win_size - 1] = 1


#LIST = []
#for i in range(height - win_size + 1):
#   for j in range(width - win_size + 1):
#       window = result[i : i+win_size, j:j+win_size]
#       NULL = np.sum(window, dtype=np.uint8)
#       INSIDE = np.sum((np.multiply(kernel, window)), dtype=np.uint8)
#       if NULL != 0 and INSIDE == 0:
#           LIST.append(tuple([i, j]))

#print(LIST)
#for item in LIST:
#    cv2.rectangle(result,tuple([item[1], item[0]]), tuple([item[1] + 20, item[0] + 20]), (255,255,255))
#cv2.imshow("result", result)
#cv2.waitKey(0)