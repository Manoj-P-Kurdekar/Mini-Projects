import cv2
import os
from matplotlib.pyplot import gray

video = cv2.VideoCapture(0) # 0 is the default camera
facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
count = 0
nameID = str(int("Enter the name: ")).lower() # Enter the name of the person
path = 'images/' + nameID
isExists = os.path.exists(path) # Check if the path exists
if isExists: # If the path exists
    print("Directory already exists")
else:
    os.makedirs(path) # Create the directory
while True:
    ret, frame = video.read() # Read the frame
    faces = facedetect.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        count = count + 1
        name = "images/" + nameID + "/" + str(count) + ".jpg" # Create the name of the image
        print("Creating image............"+name) # Print the name of the image
        cv2.imwrite(name, frame[y:y+h, x:x+w]) # Save the image
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2) # Draw the rectangle
    cv2.imshow('WindowFrame', frame) # Display the frame
    cv2.waitKey(1) # Wait for 1 millisecond
    if count > 500: # If the count is greater than 500
        break
video.release() # Release the video
cv2.destroyAllWindows() # Destroy the window