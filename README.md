# Car-Number-Plate-Detction-Extraction-And-Reading

Steps:

1.Detction of car from image using haar cascade for cars.

2.Detection of plate of car and seperating it.

3.Reading the text using pytesseract module for Optical Character Recognition in detected number plate image.

1.Original Image:

![](sample%20images/1.Original%20Image.jpg)
 



2.Gray Scaled Image:

![](sample%20images/2.Grayscle%20Image.jpg)
 



3.Detected Car using Myhaar

![](sample%20images/3.Resultant%20Image.jpg)




4.Crop Car for detection of Number Plate

![](sample%20images/4.Detected%20Car.jpg)
 



5.Converting to grayscale

![](sample%20images/5.Detected%20Car%20Gray.jpg)
 



6.Smoothening the grayscale car image using Bilateral Filter(removing noise while preserving the edges)

![](sample%20images/6.Smoothen%20Car%20Gray.jpg)
 



7.Edge Detection using Canny Edge Detection

![](sample%20images/7.Edge%20Detection%20Car%20Gray.jpg)
 



8.Detecting Number Plate using Contours and Outlining Number Plate 

![](sample%20images/8.Detected%20number%20plate.jpg)
 



9.Segmentation Of Number Plate to read text from it

![](sample%20images/9.Number%20plate.jpg)
 



10.Saving Cropped image in Images folder

![](sample%20images/10.Only%20Number%20plate.jpg)
 


