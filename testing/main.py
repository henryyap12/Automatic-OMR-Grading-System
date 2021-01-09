import cv2
import numpy as np

import utlis


def omrmarking(path,ans,mark,student,lecturer,course,score=0):
    if 1:
        widthImg = 450
        heightImg = 750
        choices = 5
        mark = int(mark.strip())
        ans = list(map(str, ans.strip().split(',')))
        ans = [0 if x == 'A' or x == "a" else x for x in ans]
        ans = [1 if x == 'B' or x == "b" else x for x in ans]
        ans = [2 if x == 'C' or x == "c" else x for x in ans]
        ans = [3 if x == 'D' or x == "d" else x for x in ans]
        ans = [4 if x == 'E' or x == "e" else x for x in ans]
        questions = len(ans)

        while True:
            frame = cv2.imread(path)
            img = cv2.resize(frame, (widthImg, heightImg))
            imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            imgblur = cv2.GaussianBlur(imggray, (5, 5), 3)
            imgcanny = cv2.Canny(imgblur, 100, 200)
            imgcountours = img.copy()
            imgbigcountour = img.copy()
            imgfinal = img.copy()

            try:
                contours, _ = cv2.findContours(imgcanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
                cv2.drawContours(imgcountours, contours, -1, (0, 255, 0), 10)
                rect = utlis.rectCounter(contours)
                biggestcountours = utlis.getCornerPoints(rect[0])
                gradepoint = utlis.getCornerPoints(rect[1])

                if biggestcountours.size != 0 and gradepoint.size != 0:
                    cv2.drawContours(imgbigcountour, biggestcountours, -1, (0, 255, 0), 10)
                    cv2.drawContours(imgbigcountour, gradepoint, -1, (255, 0, 0), 10)
                    biggestcountours = utlis.reorder(biggestcountours)
                    gradepoint = utlis.reorder(gradepoint)

                    pt1 = np.float32(biggestcountours)
                    pt2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])
                    pt01 = np.float32(gradepoint)
                    pt02 = np.float32([[0, 0], [300, 0], [0, 100], [300, 100]])

                    matrix = cv2.getPerspectiveTransform(pt1, pt2)
                    imgwrap = cv2.warpPerspective(img, matrix, (widthImg, heightImg))
                    matrixg = cv2.getPerspectiveTransform(pt01, pt02)
                    imgwrapgrade = cv2.warpPerspective(img, matrixg, (300, 100))

                    imgwrapgray = cv2.cvtColor(imgwrap, cv2.COLOR_BGR2GRAY)
                    imgthres = cv2.threshold(imgwrapgray, 170, 255, cv2.THRESH_BINARY_INV)[1]
                    boxes = utlis.splitBoxes(imgthres,ans)

                    mypixalvalue = np.zeros((questions, choices))
                    countC = 0
                    countR = 0
                    if 5 < questions <= 10:
                        for images in boxes:
                            totalpixal = cv2.countNonZero(images)
                            if totalpixal < 2000:
                                totalpixal = 0
                            mypixalvalue[countR][countC] = totalpixal
                            countC += 1
                            if countC == choices:
                                countR += 1
                                countC = 0
                        myIndex = []
                        for x in range(0, questions):
                            arr = mypixalvalue[x]
                            myindexval = np.where(arr == np.amax(arr))
                            myIndex.append(myindexval[0][0])
                            if np.sum(arr) > 6000 or np.sum(arr) < 100:
                                myIndex[x] = 900
                        grading = []
                        for x in range(0, questions):
                            if ans[x] == myIndex[x]:
                                grading.append(1)
                            else:
                                grading.append(0)

                    elif questions >= 20:
                        for images in boxes:
                            totalpixal = cv2.countNonZero(images)
                            if totalpixal < 1700:
                                totalpixal = 0
                            mypixalvalue[countR][countC] = totalpixal
                            countC += 1
                            if countC == choices:
                                countR += 1
                                countC = 0
                        print(mypixalvalue)
                        myIndex = []
                        for x in range(0, questions):
                            arr = mypixalvalue[x]
                            myindexval = np.where(arr == np.amax(arr))
                            myIndex.append(myindexval[0][0])
                            if np.sum(arr) > 4000:
                                myIndex[x] = 900
                        print(myIndex)
                        grading = []
                        for x in range(0, questions):
                            if ans[x] == myIndex[x]:
                                grading.append(1)
                            else:
                                grading.append(0)

                    else:
                        for images in boxes:
                            totalpixal = cv2.countNonZero(images)
                            if totalpixal < 5000:
                                totalpixal = 0
                            mypixalvalue[countR][countC] = totalpixal
                            countC += 1
                            if countC == choices:
                                countR += 1
                                countC = 0
                        myIndex = []
                        for x in range(0, questions):
                            arr = mypixalvalue[x]
                            myindexval = np.where(arr == np.amax(arr))
                            myIndex.append(myindexval[0][0])
                            if np.sum(arr) > 14000:
                                myIndex[x] = 900
                        print(mypixalvalue)
                        grading = []
                        for x in range(0, questions):
                            if ans[x] == myIndex[x]:
                                grading.append(1)
                            else:
                                grading.append(0)
                                grading.append(0)
                    score = (sum(grading) / questions) * mark
                    imgresult = imgwrap.copy()
                    utlis.showAnswers(imgresult, myIndex, grading, ans)
                    utlis.drawGrid(imgresult, ans)
                    imgRawDrawings = np.zeros_like(imgresult)

                    utlis.showAnswers(imgRawDrawings, myIndex, grading, ans)
                    invMatrix = cv2.getPerspectiveTransform(pt2, pt1)
                    imgInvWarp = cv2.warpPerspective(imgRawDrawings, invMatrix, (widthImg, heightImg))

                    imgrawgrade = np.zeros_like(imgwrapgrade, np.uint8)
                    cv2.putText(imgrawgrade, str(float(score)) + "%", (50, 100), cv2.FONT_HERSHEY_COMPLEX, 3,(0, 255, 0),4)
                    invMatrixG = cv2.getPerspectiveTransform(pt02, pt01)
                    imginvgradedisplay = cv2.warpPerspective(imgrawgrade, invMatrixG, (widthImg, heightImg))
                    imginvgradedisplay = cv2.addWeighted(imginvgradedisplay, 1, imgInvWarp, 1, 0)
                    imgfinal = cv2.addWeighted(imgfinal, 1, imginvgradedisplay, 1, 1)

            except:
                pass
            name = "{}_{}_{}.jpg".format(course, lecturer, student)
            cv2.imwrite("Scanned.jpg", imgfinal)
            cv2.imwrite(name,imgfinal)
            return score
