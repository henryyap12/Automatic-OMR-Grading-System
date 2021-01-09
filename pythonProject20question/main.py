import cv2
import numpy as np
import utlis


phone = True
width = 800
height = 800
widthImg = 700
heightImg = 700
path = "multiple_choice_template20.png"
url = 'http://192.168.1.107:8080/video'
#cap = cv2.VideoCapture(url)
questions = 20
choices = 5
ans = [1, 1, 3, 2, 1, 0, 1, 3, 2, 1,1, 1, 3, 2, 1, 0, 1, 3, 2, 1]
mark = int(input("Enter total mark: "))
count = 0

if __name__ == '__main__':
    while True:
        #if phone:
        #    success, frame = cap.read()
        #else:
        frame = cv2.imread(path)
        img = cv2.resize(frame, (widthImg, heightImg))
        imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        imgblur = cv2.GaussianBlur(imggray, (5, 5), 3)
        imgcanny = cv2.Canny(imgblur, 70, 100)
        imgcountours = img.copy()
        imgbigcountour = img.copy()
        imgfinal = img.copy()
        imgblank = np.zeros((heightImg, widthImg, 3), np.uint8)

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
                boxes = utlis.splitBoxes(imgthres)

                mypixalvalue = np.zeros((questions, choices))
                countC = 0
                countR = 0
                for images in boxes:
                    totalpixal = cv2.countNonZero(images)
                    if totalpixal < 2000:
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
                    if np.sum(arr) > 5000:
                        myIndex[x] = 900
                print(myIndex)
                grading = []
                for x in range(0, questions):
                    if ans[x] == myIndex[x]:
                        grading.append(1)
                    else:
                        grading.append(0)
                print(grading)
                score = (sum(grading) / questions) * mark
                print(score)

                imgresult = imgwrap.copy()
                utlis.showAnswers(imgresult, myIndex, grading, ans)
                utlis.drawGrid(imgresult)
                imgRawDrawings = np.zeros_like(imgresult)

                utlis.showAnswers(imgRawDrawings, myIndex, grading, ans)
                invMatrix = cv2.getPerspectiveTransform(pt2, pt1)
                imgInvWarp = cv2.warpPerspective(imgRawDrawings, invMatrix, (widthImg, heightImg))  # INV IMAGE WARP

                imgrawgrade = np.zeros_like(imgwrapgrade, np.uint8)
                cv2.putText(imgrawgrade, str(int(score)) + "%", (50, 100), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 255, 0),
                            4)

                invMatrixG = cv2.getPerspectiveTransform(pt02, pt01)
                imginvgradedisplay = cv2.warpPerspective(imgrawgrade, invMatrixG,
                                                         (widthImg, heightImg))
                imginvgradedisplay = cv2.addWeighted(imginvgradedisplay, 1, imgInvWarp, 1, 0)
                imgfinal = cv2.addWeighted(imgfinal, 1, imginvgradedisplay, 1, 1)

                ImageArray = ([img, imggray, imgblur, imgcanny],
                              [imgcountours, imgbigcountour, imgwrap, imgthres],
                              [imgresult, imgInvWarp, imgfinal, imgblank])
                cv2.imshow("Final Result", imgfinal)

        except Exception:
            imageArray = ([img, imggray, imgblur, imgcanny], [imgcountours, imgbigcountour, imgblank, imgblank],
                          [imgblank, imgblank, imgblank, imgblank])
            lables = [["Original", "Gray", "Blur", "Canny"],
                      ["Contours", "Biggest Con", "Warp", "Threshold"],
                      ["Result", "Raw Drawing", "Inv Raw", "Final"]]
            ImageStacked = utlis.stackImages(imageArray, 0.4, lables)
            cv2.imshow("imgfnal", ImageStacked)
            if cv2.waitKey(1) & 0xFF == ord('s'):
                cv2.imshow('Result', imgfinal)
                cv2.waitKey(300)
                count += 1
