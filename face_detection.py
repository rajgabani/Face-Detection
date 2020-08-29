# import libraries of python OpenCV
import cv2
import os

# capture frame from webcam
cap = cv2.VideoCapture(0)

# get current working directory
current_working_dir = os.getcwd()
# define XML file
faceCascade = cv2.CascadeClassifier(current_working_dir+'\haarcascade_frontalface_default.xml')


while True:
    try:
        # Capture image frame-by-frame
        ret, frame = cap.read()

        if ret == True:
            # conver colour image to gray scale image
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # detect faces
            faces = faceCascade.detectMultiScale(gray, 1.1, 4)
            # print('-------',faces)

            if len(faces)==0:
                cv2.putText(frame,"Face not detect",(10,30),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),1,cv2.LINE_AA)
            else:
                # Draw a rectangle around the faces
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    cv2.putText(frame,"{} face detect".format(len(faces)),(10,30),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1,cv2.LINE_AA)

            # Display the frame
            cv2.imshow('Video', frame)
            # press key-'Q' to stop
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        else:
            print("Image not captured")
            break

    except Exception as e:
        print("EXCEPTION : ", e)

cap.release()
cv2.destroyAllWindows()