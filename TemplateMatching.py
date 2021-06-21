import cv2
import numpy as np

def FindSelectedArea(img, template):
    img = np.copy(img)

    # Read the main image

    # Convert it to grayscale
    #img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Read the template
    template =   cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    size_template = template.shape

    # Store width and height of template in w and h
    w, h = template.shape[::-1]

    # Perform match operations.
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

    # Specify a threshold
    threshold = 0.8

    # Store the index of array res which its element higher than threshold
    loc = np.where(res >= threshold)
    prc = res[loc]
    transpose = np.array(prc)
    transpose = np.transpose(transpose).tolist()


    # Draw a rectangle around the matched region.
    # for pt in zip(*loc[::-1]):
    #     cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), color, 2)

    # Show the final image with the matched area.
    #cv2.imshow(name, img)
    return list(zip(*loc[::-1]))