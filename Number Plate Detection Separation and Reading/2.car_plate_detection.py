import cv2

#loading haar
# car_haar=cv2.CascadeClassifier("cars.xml")
car_haar=cv2.CascadeClassifier("myhaar.xml")

#loading image
img=cv2.imread("cars\\car.jpg")

#copy of input image
img_res=img.copy()

#converting image to grayscale
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#detecting car
######Source to understadnd params of detectMultiscale
######https://stackoverflow.com/questions/20801015/recommended-values-for-opencv-detectmultiscale-parameters
cars=car_haar.detectMultiScale(img_gray,scaleFactor=1.35,minNeighbors=3,minSize=(300,300))
for (x,y,w,h) in cars:
	cv2.rectangle(img_res,(x,y),(x+w,y+h),(0,255,0),1)
	#saving detected car image in roi(region of interest)
	roi=img[y:y+h,x:x+w]

#DETECTING NUMBER PLATE FROM CAR roi

roi_copy=roi.copy()
#coversion of roi to gray
roi_gray=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)

#smoothening of roi_gray (bilateralFilter : removes noise while preserving edges)
roi_bilateral=cv2.bilateralFilter(roi_gray,11,17,17)	#(image on which to perform,diameter of pixel neighbour,sigma color,sigma space)

#detecting edges in roi_bilateral using canny edge detection
roi_canny=cv2.Canny(roi_bilateral,140,230)				#(image on which to perform,1st thrshold value,2nd threshold value)

#finding contours of rectangle shape
contours,_=cv2.findContours(roi_canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)    #(,mode ,method)
contours=sorted(contours, key = cv2.contourArea, reverse = True)[:30]

for contour in contours:
	approx=cv2.approxPolyDP(contour,0.02*cv2.arcLength(contour,True),True)	  #(approxPolyDP : for detecting the polygon. parameters (contour,approximation*length of contour(contour out of contours, is it closed fig),is it closed figure))
	if (len(approx)==4):
		number_plate=approx
		break
	# cv2.drawContours(roi_copy,approx,-1,(0,255,0),2)

#drawing contour on the plate
# print(number_plate)												#number_plate contains numpy array of 4 points of no. plate
cv2.drawContours(roi_copy,[number_plate],-1,(255,0,0),2)			#(image on which contour to be drawn,contour,-1(for all or put here 0 for this example),color,thickness)



#Displaying
cv2.imshow("1.Original Image",img)
cv2.imshow("2.Grayscle Image",img_gray)
cv2.imshow("3.Resultant Image",img_res)
cv2.imshow("4.Detected Car",roi)
cv2.imshow("5.Detected Car Gray",roi_gray)
cv2.imshow("6.Smoothen Car Gray",roi_bilateral)
cv2.imshow("7.Edge Detection Car Gray",roi_canny)
cv2.imshow("8.Detected number plate",roi_copy)




#Exit from program
if cv2.waitKey(0)==27:
	cv2.destroyAllWindows()
