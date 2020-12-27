import cv2
import numpy as np
import utlis

phone = True
width = 400
height = 400
widthImg = 700
heightImg = 700
url = 'http://192.168.1.116:8080/video'
path = "sample/131781433_400868891230894_7668413708674499293_n.jpg"
cap = cv2.VideoCapture(url)
questions = 20
choices = 5
mark = int(input("Enter total mark: "))
ans = [1, 1, 3, 1, 0, 1, 3, 2, 1, 1, 1, 3, 2, 1, 0, 1, 3, 2, 1, 1]
ans1 = [1, 1, 3, 1, 0, 3, 2, 1, 1, 1, 3, 2, 1, 0, 1, 3, 2, 1, 1, 1]
count = 0

if __name__ == '__main__':
    while True:
        if phone:
            success, frame = cap.read()
        else:
            frame = cv2.imread(path)
        img = cv2.resize(frame, (widthImg, heightImg))
        imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        imgblur = cv2.GaussianBlur(imggray, (5, 5), 1)
        imgcanny = cv2.Canny(imgblur, 100, 200)
        imgcountours = img.copy()
        imgbigcountour = img.copy()
        imgsecondbigcountour = img.copy()
        imgblank = np.zeros((heightImg, widthImg, 3), np.uint8)

        try:
            contours, _ = cv2.findContours(imgcanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            cv2.drawContours(imgcountours, contours, -1, (0, 255, 0), 10)

            # Finding the Rectangle in paper
            rectcounts = utlis.rectCounter(contours)
            biggestcountours = utlis.getCornerPoints(rectcounts[0])
            secondbigcountours = utlis.getCornerPoints(rectcounts[1])
            gradepoint = utlis.getCornerPoints(rectcounts[2])

            if biggestcountours.size != 0 and secondbigcountours.size != 0 and gradepoint.size != 0:
                cv2.drawContours(imgbigcountour, biggestcountours, -1, (0, 255, 0), 10)
                cv2.drawContours(imgsecondbigcountour, secondbigcountours, -1, (0, 255, 0), 10)
                cv2.drawContours(imgbigcountour, gradepoint, -1, (255, 0, 0), 10)
                biggestcountours = utlis.reorder(biggestcountours)
                secondbigcountours = utlis.reorder(secondbigcountours)
                gradepoint = utlis.reorder(gradepoint)

                pt1 = np.float32(biggestcountours)
                pt2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])

                pt11 = np.float32(secondbigcountours)
                pt21 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])

                pt01 = np.float32(gradepoint)
                pt02 = np.float32([[0, 0], [300, 0], [0, 100], [300, 100]])

                matrix = cv2.getPerspectiveTransform(pt1, pt2)
                imgwrap = cv2.warpPerspective(img, matrix, (widthImg, heightImg))
                # cv2.imshow('21', imgwrap)
                matrixg = cv2.getPerspectiveTransform(pt11, pt21)
                imgwrapg = cv2.warpPerspective(img, matrixg, (widthImg, heightImg))
                # cv2.imshow('2',imgwrapg)
                matrixq = cv2.getPerspectiveTransform(pt01, pt02)
                imgwrapgrade = cv2.warpPerspective(img, matrixg, (300, 100))

                # Threshold Image
                imgwrapgray = cv2.cvtColor(imgwrap, cv2.COLOR_BGR2GRAY)
                imgthres = cv2.threshold(imgwrapgray, 170, 255, cv2.THRESH_BINARY_INV)[1]
                imgwrapgry = cv2.cvtColor(imgwrapg, cv2.COLOR_BGR2GRAY)
                imgthresh = cv2.threshold(imgwrapgry, 170, 255, cv2.THRESH_BINARY_INV)[1]
                boxes = utlis.splitBoxes(imgthres)
                boxesex = utlis.splitBoxes(imgthresh)

                mypixalvalue = np.zeros((questions, choices))
                countC = 0
                countR = 0
                for images in boxes:
                    totalpixal = cv2.countNonZero(images)
                    mypixalvalue[countR][countC] = totalpixal
                    countC += 1
                    if countC == choices:
                        countR += 1
                        countC = 0

                # Finding Index Value of Marking
                myIndex = []
                for x in range(0, questions):
                    arr = mypixalvalue[x]
                    myindexval = np.where(arr == np.amax(arr))
                    myIndex.append(myindexval[0][0])

                grading = []
                for x in range(0, questions):
                    if ans[x] == myIndex[x]:
                        grading.append(1)
                    else:
                        grading.append(0)

                mypixalvalue1 = np.zeros((questions, choices))
                countCol = 0
                countRow = 0
                for images in boxesex:
                    totalpixal1 = cv2.countNonZero(images)
                    mypixalvalue1[countRow][countCol] = totalpixal1
                    countCol += 1
                    if countCol == choices:
                        countRow += 1
                        countCol = 0

                # Finding Index Value of Marking
                myIndex1 = []
                for x in range(0, questions):
                    arr1 = mypixalvalue1[x]
                    myindexval1 = np.where(arr1 == np.amax(arr1))
                    myIndex1.append(myindexval1[0][0])

                grading1 = []
                for x in range(0, questions):
                    if ans1[x] == myIndex1[x]:
                        grading1.append(1)
                    else:
                        grading1.append(0)

                score = (sum(grading + grading1) / (questions * 2)) * mark
                print(score)
                imgfinal = img.copy()
                imgresult = imgwrap.copy()
                imgresult1 = imgwrapg.copy()
                utlis.showAnswers(imgresult, myIndex, grading, ans)  # DRAW DETECTED ANSWERS
                utlis.drawGrid(imgresult)
                utlis.showAnswers(imgresult1, myIndex1, grading1, ans1)  # DRAW DETECTED ANSWERS
                utlis.drawGrid(imgresult1)  # DRAW GRID
                imgRawDrawings = np.zeros_like(imgresult)  # NEW BLANK IMAGE WITH WARP IMAGE SIZE
                imgRawDrawings1 = np.zeros_like(imgresult1)

                utlis.showAnswers(imgRawDrawings, myIndex, grading, ans)  # DRAW ON NEW IMAGE
                utlis.showAnswers(imgRawDrawings1, myIndex1, grading1, ans1)
                invMatrix = cv2.getPerspectiveTransform(pt2, pt1)  # INVERSE TRANSFORMATION MATRIX
                imgInvWarp = cv2.warpPerspective(imgRawDrawings, invMatrix, (widthImg, heightImg))  # INV IMAGE WARP
                invMatrix1 = cv2.getPerspectiveTransform(pt21, pt11)  # INVERSE TRANSFORMATION MATRIX
                imgInvWarp1 = cv2.warpPerspective(imgRawDrawings1, invMatrix1, (widthImg, heightImg))  # INV IMAGE WARP

                # DISPLAY GRADE
                imgrawgrade = np.zeros_like(imgwrapgrade, np.uint8)

                # NEW BLANK IMAGE WITH GRADE AREA SIZE
                cv2.putText(imgrawgrade, str(float(score)) + "%", (50, 100), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 255, 0),
                            4)  # ADD THE GRADE TO NEW IMAGE

                invMatrixG = cv2.getPerspectiveTransform(pt02, pt01)
                # INVERSE TRANSFORMATION MATRIX
                imginvgradedisplay = cv2.warpPerspective(imgrawgrade, invMatrixG,
                                                         (widthImg, heightImg))  # INV IMAGE WARP
                # SHOW ANSWERS AND GRADE ON FINAL IMAGE
                imginvgradedisplay = cv2.addWeighted(imginvgradedisplay, 1, imgInvWarp, 1, 0)
                imginvgradedisplay = cv2.addWeighted(imginvgradedisplay, 1, imgInvWarp1, 1, 0)
                imgfinal = cv2.addWeighted(imgfinal, 1, imginvgradedisplay, 1, 1)

                imageArray = ([img, imggray, imgblur, imgcanny], [imgcountours, imgbigcountour, imgblank, imgblank],
                              [imgblank, imgblank, imgblank, imgblank])

                cv2.imshow("Final Result", imgfinal)

        except Exception:
            imageArray = ([img, imggray, imgblur, imgcanny], [imgcountours, imgbigcountour, imgblank, imgblank],
                          [imgblank, imgblank, imgblank, imgblank])
        lables = [["Original", "Gray", "Blur", "Canny"],
                  ["First Contours", "Second Con", "Threshold", "Threshold1"],
                  ["Inv Raw", "Raw Drawing", "Final", "Final"]]
        ImageStacked = utlis.stackImages(imageArray, 0.3,lables)
        cv2.imshow("imgfnal", ImageStacked)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite("FinalImage.jpg", imgwrap)
            cv2.waitKey(300)
            break
