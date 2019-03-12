import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # We load the cascade for the face.
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml') # We load the cascade for the eyes.

def detect(gray, frame): 
#Frame is the original image frame
# We create a function that takes as input the image in black and white (gray) and the original image (frame), and that will return the same image with the detector rectangles. 
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) # We apply the detectMultiScale method from the face cascade to locate one or several faces in the image.
                                                        # The image will be reduced by 1.3 times and 5 neighbour zones will also be accepted
    for (x, y, w, h) in faces: # For each detected face: 
        
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2) # We paint a rectangle around the face.# 2 is the thickness of the border of the rectangle # x and y are the upper left coordinates of the rectangle w is the width and h is the height
        
        roi_gray = gray[y:y+h, x:x+w] # We get the region of interest in the black and white image.
        
        roi_color = frame[y:y+h, x:x+w] # We get the region of interest in the colored image.
        
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3) # We apply the detectMultiScale method to locate one or several eyes in the image.
        
        for (ex, ey, ew, eh) in eyes: # For each detected eye:
            
            cv2.rectangle(roi_color,(ex, ey),(ex+ew, ey+eh), (0, 255, 0), 2) # We paint a rectangle around the eyes, but inside the referential of the face.
    
    return frame # We return the image with the detector rectangles.

#we need the last frame coming from the webcam...because on this last frame we will apply the detect function
#VideoCapture is a class working on web cam

video_capture = cv2.VideoCapture(0) # We turn the webcam on # 0 if it is the  webcam of the computer and 1 if external webcam is connected

while True: # We repeat infinitely (until break):
    
    _, frame = video_capture.read() # We get the last frame.#we put "_" so that we don't get the first element returned by the read
    
    #cvtColor is a function of our cv2 module which helps us do transformations on some frames
    #Transformation on our original color frame to convert it into black and white image
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # We do some colour transformations.# Cascades are done on black and white images
    
    canvas = detect(gray, frame) # We get the output of our detect function.
    
    #we can display in an animated way all the successive outputs (processed images) in a window

    cv2.imshow('Video', canvas) # We display the outputs.
    
    if cv2.waitKey(1) & 0xFF == ord('q'): # If we type on the keyboard:#we need to stop the webcam and face-detection process if we press 'q' on keyboard
    
    break # We stop the loop.


video_capture.release() # We turn the webcam off.

cv2.destroyAllWindows() # We destroy all the windows inside which the images were displayed.
