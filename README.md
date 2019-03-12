# Face_Detection
A learning attempt on Face Detection by using the Viola-Jones algorithm. [Computer-Vision , OpenCV-Python]


Viola Jones algorithm is specifically desinged for frontal faces.

For simplicity we turn the image into gray scale.

Reference : https://www.cs.cmu.edu/~efros/courses/LBMV07/Papers/viola-cvpr-01.pdf

In the Viola–Jones object detection framework, the Haar-like features are organized in something called a classifier cascade to form a strong learner or classifier. 

The key advantage of a Haar-like feature over most other features is its calculation speed.

An integral image helps you rapidly calculate summations over image subregions. 
Every pixel in an integral image is the summation of the pixels above and to the left of it. 
To calculate the summation of a subregion of an image, you can use the corresponding region of its integral image.


The algorithm first shrinks the image to 24-by-24 pixels and then looks for Haar-Like features.These features are scalable.

When training happens we know which features are important and what threshold they should have. Thresholds are use to identify if the haar-like features we are looking for is present or not.

Adaptive Boosting [ADABOOST] and Cascading is also used.

