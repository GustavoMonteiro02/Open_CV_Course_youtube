#pylint:disable=no-member

import cv2 as cv

# img = cv.imread(r'C:\Users\asus\Desktop\opencv-course\Resources\Photos\cat_large.jpg')
# if img is None:
#     print("Error: Image not found or unable to load.")
# else:
#     cv.imshow('Cats', img)

#cv.waitKey(0) # awaits for a key to be pressed

# Reading Videos
capture = cv.VideoCapture(r'..\recursos\videos\dog.mp4')

while True:
    isTrue, frame = capture.read()
    
    # if cv.waitKey(20) & 0xFF==ord('d'):
    # This is the preferred way - if `isTrue` is false (the frame could 
    # not be read, or we're at the end of the video), we immediately
    # break from the loop. 
    if isTrue:    
        cv.imshow('Video', frame)
        if cv.waitKey(20) & 0xFF==ord('d'):
            break            
    else:
        break

capture.release()
cv.destroyAllWindows()
