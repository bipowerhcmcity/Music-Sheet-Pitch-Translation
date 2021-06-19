import cv2
import numpy as np

def DrawLine(delete_line = False, img=None):
    img = np.copy(img)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.array([[0, 0, 0], [1, 1, 1], [0, 0, 0]], dtype=np.uint8)

    dilate = cv2.dilate(gray, kernel, iterations=100)
    th, threshold = cv2.threshold(dilate, 220, 255, cv2.THRESH_BINARY)
    # randomly take a vertical line point:
    data = np.squeeze(threshold[:, int(threshold.shape[1] / 2)])
    class_255 = np.empty(shape=(0), dtype=np.int64)
    class_0 = np.empty(shape=(0), dtype=np.int64)
    i = 0
    count = 0
    while i < len(data):
        count = 0
        if i + count > len(data):
            break

        while True:
            if i + count == len(data) or data[i] != data[i + count]:
                break
            if data[i] == data[i + count]:
                count += 1;
        if data[i] == 255:
            class_255 = np.append(class_255, count)
        else:
            class_0 = np.append(class_0, count)
        i += count

    thickLine = np.argmax(np.bincount(class_0.flat))
    spaceLine = np.argmax(np.bincount(class_255.flat))
    staffHeight = thickLine*5 + spaceLine*4


    line_arr = np.empty(shape=(0), dtype=np.int64)
    if delete_line:
        y = 0
        for i in range(len(class_0)):
            y += class_255[i]+class_0[i]
            line_arr = np.append(line_arr,y)
            cv2.line(img, (-1000, y), (1000, y), (255, 255, 255), class_0[i]*2)
    else:
        y = 0
        for i in range(len(class_0)):
            y += class_255[i] + class_0[i]
            line_arr = np.append(line_arr,y)
            cv2.line(img, (-1000, y), (1000, y), (0, 0, 255), thickLine)
    cv2.imshow("img", img)
    #cv2.imshow("dilate", dilate)
    #cv2.imshow("thresh", threshold)
    return line_arr, staffHeight

# line_arr = DrawLine(False,img)
