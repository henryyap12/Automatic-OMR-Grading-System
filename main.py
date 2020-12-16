import cv2
import numpy as np
import utlis

phone = True
width = 800
height = 800
widthImg =300
heightImg = 500
path = "IMG_20201215_170248.jpg"
url = 'http://192.168.1.108:8080/video'
cap = cv2.VideoCapture(0)
questions = 5
choices = 5
ans = [1,1,3,2,1]

count = 0

if __name__ == '__main__':
    while True:
        #if phone:
        #    success, frame = cap.read()
         #   img = cv2.resize(frame, (width, height))

        #else:
        frame = cv2.imread(path)
        img = cv2.resize(frame, (widthImg, heightImg))
        try:
            imgcountours = img.copy()
            imgbigcountour = img.copy()
            imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            imgblur = cv2.GaussianBlur(imggray, (5, 5), 2)
            imgcanny = cv2.Canny(imgblur, 10, 90)
            imgblank= np.zeros((heightImg,widthImg,3),np.uint8)
            contours, _ = cv2.findContours(imgcanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            cv2.drawContours(imgcountours, contours, -1, (0, 255, 0), 10)

            # Finding the Rectangle in paper
            rectcounts = utlis.rectCounter(contours)
            biggestcountours = utlis.getCornerPoints(rectcounts[0])
            gradepoint = utlis.getCornerPoints(rectcounts[1])
            #print(biggestcountours)

            if biggestcountours.size != 0 and gradepoint.size != 0:
                cv2.drawContours(imgbigcountour, biggestcountours, -1, (0, 255, 0), 10)
                cv2.drawContours(imgbigcountour, gradepoint, -1, (255, 0, 0), 10)
                biggestcountours = utlis.reorder(biggestcountours)
                gradepoint = utlis.reorder(gradepoint)

                pt1 = np.float32(biggestcountours)
                pt2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])
                pt01 = np.float32(gradepoint)
                pt02 = np.float32([[0, 0], [300, 0], [0, 100], [300,100]])

                matrix = cv2.getPerspectiveTransform(pt1, pt2)
                imgwrap = cv2.warpPerspective(img, matrix, (widthImg, heightImg))
                matrixg = cv2.getPerspectiveTransform(pt01, pt02)
                imgwrapgrade = cv2.warpPerspective(img, matrixg, (300, 100))

                # Threshold Image
                imgwrapgray = cv2.cvtColor(imgwrap, cv2.COLOR_BGR2GRAY)
                imgthres = cv2.threshold(imgwrapgray, 170, 255, cv2.THRESH_BINARY_INV)[1]
                boxes = utlis.splitBoxes(imgthres)
                #cv2.imshow("splte",boxes[2])
                #print(cv2.countNonZero(boxes[0]))
                    #print(cv2.countNonZero(boxes[2]))
                    # print(cv2.countNonZero(boxes[1]))
                    #cv2.imshow("test",boxes[0])


                mypixalvalue = np.zeros((questions, choices))
                countC = 0
                countR = 0
                for images in boxes:
                    totalpixal = cv2.countNonZero(images)
                    mypixalvalue[countR][countC] = totalpixal
                    countC += 1
                    if countC == choices:
                        countR += 1;countC = 0
   #             print(mypixalvalue)

                # Finding Index Value of Marking
                myIndex = []
                for x in range(0, questions):
                    arr = mypixalvalue[x]
  #                  print("arr",arr)
                    myindexval = np.where(arr == np.amax(arr))
 #                   print(myindexval[0])
                    myIndex.append(myindexval[0][0])
#                    print(myIndex)
                grading = []
                for x in range(0,questions):
                    if ans[x] == myIndex[x]:
                        grading.append(1)
                    else:
                        grading.append(0)
#                print(grading)

                score = (sum(grading)/questions)*100
                print(score)
                imgfinal= img.copy()
                imgresult = imgwrap.copy()
                utlis.showAnswers(imgresult, myIndex, grading, ans)  # DRAW DETECTED ANSWERS
                utlis.drawGrid(imgresult)  # DRAW GRID
                imgRawDrawings = np.zeros_like(imgresult)  # NEW BLANK IMAGE WITH WARP IMAGE SIZE

                utlis.showAnswers(imgRawDrawings, myIndex, grading, ans)  # DRAW ON NEW IMAGE
                invMatrix = cv2.getPerspectiveTransform(pt2, pt1)  # INVERSE TRANSFORMATION MATRIX
                imgInvWarp = cv2.warpPerspective(imgRawDrawings, invMatrix, (widthImg, heightImg))  # INV IMAGE WARP

                # DISPLAY GRADE
                imgrawgrade = np.zeros_like(imgwrapgrade, np.uint8)

                # NEW BLANK IMAGE WITH GRADE AREA SIZE
                cv2.putText(imgrawgrade, str(int(score)) + "%", (50, 100), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 255, 0),4)  # ADD THE GRADE TO NEW IMAGE

                invMatrixG = cv2.getPerspectiveTransform(pt02, pt01)
                # INVERSE TRANSFORMATION MATRIX
                imginvgradedisplay = cv2.warpPerspective(imgrawgrade, invMatrixG,(widthImg, heightImg))  # INV IMAGE WARP
                # SHOW ANSWERS AND GRADE ON FINAL IMAGE
                imginvgradedisplay = cv2.addWeighted(imginvgradedisplay, 1, imgInvWarp, 1, 0)
                cv2.imshow("mark",imginvgradedisplay)
                imgfinal = cv2.addWeighted(imgfinal, 1, imginvgradedisplay, 1, 1)

                ImageArray = ([img, imggray, imgblur, imgcanny],
                              [imgcountours, imgbigcountour, imgwrap, imgthres],
                              [imgresult, imgInvWarp, imgfinal, imgBlank])
                cv2.imshow("Final Result", imgfinal)

        except Exception:
                imgBlank = np.zeros_like(img)
                ImageArray = ([img, imggray, imgblur, imgcanny],
                            [imgcountours, imgbigcountour, imgwrap, imgthres],
                            [imgresult, imgInvWarp, imgBlank, imgBlank])
        lables = [["Original", "Gray", "Blur", "Canny"],
                  ["Contours", "Biggest Con", "Warp", "Threshold"],
                  ["Result", "Raw Drawing", "Inv Raw", "Final"]]
        ImageStacked = utlis.stackImages(ImageArray, 0.4)
        cv2.imshow("imgfnal",ImageStacked)
        cv2.imshow("final",imgfinal)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite("FinalImage.jpg", imgwrap)
            cv2.waitKey(300)
            break
