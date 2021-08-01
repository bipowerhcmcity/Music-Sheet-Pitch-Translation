import cv2
import numpy as np



def StaffLineRemoval(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



    threshold =160# int(255/2)
    trans = np.copy(gray)
    trans[gray  < threshold] = 255 - trans[gray < threshold]
    trans[gray >= threshold] = 0

    window_size = 3
    kernel = np.asarray([1,0,1])
    compare_vec = np.zeros(window_size)

    shape = img.shape
    height = shape[0]
    width = shape[1]

    result_1 = np.copy(trans)
    for i in range(height - window_size + 1):
        for j in range(width - window_size + 1):
            window = trans[i : i+window_size, j:j+window_size]
            if((kernel.dot(window) == compare_vec).all()):
                #print(gray[i:i+3, j:j+3])
                #copy[i:i+3, j:j+3] = 0
                result_1[i:i+window_size, j:j+window_size] = 0

    result = np.copy(result_1)
    result[result_1 < threshold] = 255 - result[result_1 < threshold]
    result[result_1 >= threshold] = 0 #+ result[result_1 >=threshold]
    cv2.imshow("StaffLine Removal", result)
    return result

