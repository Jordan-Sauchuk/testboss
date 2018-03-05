import cv2

cap = cv2.VideoCapture(0)
cascade_path = "./haarcascade_frontalface_default.xml"
i = 1
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier(cascade_path)
    # Display the resulting frame
    cv2.imshow('frame',frame_gray)

    facerect = cascade.detectMultiScale(frame_gray, scaleFactor=1.01, minNeighbors=3, minSize=(3, 3))
    if len(facerect) > 0:
      print('face detected')
      color = (255, 255, 255)  # 白
      for rect in facerect:
                # 検出した顔を囲む矩形の作成
                #cv2.rectangle(frame, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), color, thickness=2)

        x, y = rect[0:2]
        width, height = rect[2:4]
        image = frame[y - 10: y + height, x: x + width]
        cv2.imwrite('./data/boss/image' + str(i) + '.jpg',image)
    
    i += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()