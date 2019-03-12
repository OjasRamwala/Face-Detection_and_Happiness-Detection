# Face_Detection
A learning attempt on Face Detection by using the Viola-Jones algorithm. [Computer-Vision , OpenCV-Python]


Viola Jones algorithm is specifically desinged for frontal faces.


For simplicity we turn the image into gray scale.

Reference : https://www.cs.cmu.edu/~efros/courses/LBMV07/Papers/viola-cvpr-01.pdf

In the Viola–Jones object detection framework, the Haar-like features are organized in something called a classifier cascade to form a strong learner or classifier. 

The key advantage of a Haar-like feature over most other features is its calculation speed.

Haar-Like Features: https://www.google.com/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwiWo8TZxvvgAhUHuo8KHWxrAoMQjRx6BAgBEAU&url=https%3A%2F%2Fdocs.opencv.org%2F3.4.3%2Fd7%2Fd8b%2Ftutorial_py_face_detection.html&psig=AOvVaw3mihxkk91Md681J5jvAsqS&ust=1552443994732116

An integral image helps you rapidly calculate summations over image subregions. 

Every pixel in an integral image is the summation of the pixels above and to the left of it. 

To calculate the summation of a subregion of an image, you can use the corresponding region of its integral image.
