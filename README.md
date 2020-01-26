# Car-Number-Plate-Detction-Extraction-And-Reading

Steps:
1.Detction of car from image using haar cascade for cars.
2.Detection of plate of car and seperating it.
3.Reading the text using pytesseract module for Optical Character Recognition in detected number plate image.

1.Original Image:

 



2.Gray Scaled Image:

 



3.Detected Car using Myhaar

 



4.Crop Car for detection of Number Plate

 



5.Converting to grayscale

 



6.Smoothening the grayscale car image using Bilateral Filter(removing noise while preserving the edges)

 



7.Edge Detection using Canny Edge Detection

 



8.Detecting Number Plate using Contours and Outlining Number Plate 

 



9.Segmentation Of Number Plate to read text from it

 



10.Saving Cropped image in Images folder

 


