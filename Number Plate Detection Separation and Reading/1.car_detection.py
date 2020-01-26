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
cars=car_haar.detectMultiScale(img_gray,scaleFactor=1.35,minNeighbors=3,minSize=(200,200))
for (x,y,w,h) in cars:
	cv2.rectangle(img_res,(x,y),(x+w,y+h),(0,255,0),1)
	#saving detected car image in roi(region of interest)
	roi=img[y:y+h,x:x+w]

cv2.imshow("1.Original Image",img)
cv2.imshow("2.Grayscle Image",img_gray)
cv2.imshow("3.Resultant Image",img_res)
cv2.imshow("4.Detected Car",roi)


if cv2.waitKey(0)==27:
	cv2.destroyAllWindows()
