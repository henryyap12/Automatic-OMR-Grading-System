import cv2
import numpy as np


def reorder(myPoints):
    myPoints = myPoints.reshape((4, 2))
    myPointsNew = np.zeros((4, 1, 2), dtype=np.int32)
    add = myPoints.sum(1)
    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]
    diff = np.diff(myPoints, axis=1)
    myPointsNew[1] = myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]

    return myPointsNew


def rectCounter(contours):
    rectCon = []
    for i in contours:
        area = cv2.contourArea(i)
        if area > 50:
            peri = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, 0.02 * peri, True)
            if len(approx) == 4:
                rectCon.append(i)
    rectCon = sorted(rectCon, key=cv2.contourArea, reverse=True)
    return rectCon


def getCornerPoints(cont):
    peri = cv2.arcLength(cont, True)  # LENGTH OF CONTOUR
    approx = cv2.approxPolyDP(cont, 0.02 * peri, True)  # APPROXIMATE THE POLY TO GET CORNER POINTS
    return approx


def splitBoxes(img,ans):
    question = len(ans)
    rows = np.vsplit(img,question)
    boxes = []
    for r in rows:
        cols = np.hsplit(r, 5)
        for box in cols:
            boxes.append(box)
    return boxes


def drawGrid(img, ans, choices=5):
    questions = len(ans)
    secW = int(img.shape[1] / choices)
    secH = int(img.shape[0] / questions)
    for i in range(0, questions):
        pt1 = (0, secH * i)
        pt2 = (img.shape[1], secH * i)
        pt3 = (secW * i, 0)
        pt4 = (secW * i, img.shape[0])
        cv2.line(img, pt1, pt2, (255, 255, 0), 2)
        cv2.line(img, pt3, pt4, (255, 255, 0), 2)

    return img


def showAnswers(img, myIndex, grading, ans, choices=5):
    questions = len(ans)
    secW = int(img.shape[1] / choices)
    secH = int(img.shape[0] / questions)
    for x in range(0, questions):
        myans = myIndex[x]
        cX = (myans * secW) + secW // 2
        cY = (x * secH) + secH // 2
        if grading[x] == 1:
            myColor = (0, 255, 0)
            cv2.circle(img, (cX, cY), 40, myColor, cv2.FILLED)
        else:
            myColor = (0, 0, 255)
            cv2.circle(img, (cX, cY), 30, myColor, cv2.FILLED)

            # CORRECT ANSWER
            myColor = (0, 255, 0)
            correctAns = ans[x]
            cv2.circle(img, ((correctAns * secW) + secW // 2, (x * secH) + secH // 2),
                       20, myColor, cv2.FILLED)


def biggestContour(contours):
    biggest = np.array([])
    max_area = 0
    for i in contours:
        area = cv2.contourArea(i)
        if area > 5000:
            peri = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, 0.02 * peri, True)
            if area > max_area and len(approx) == 4:
                biggest = approx
                max_area = area
    return biggest, max_area
