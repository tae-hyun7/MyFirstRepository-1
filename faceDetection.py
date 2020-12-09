  GNU nano 3.2                    faceDetection.py                              

    img = cv2.flip(img, -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(20, 20)
    )ㅇㅇㅇㅇㅇㅇㅇㅇ
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
ㅇㅇㅇㅇㅇㅇㅇㅇ
