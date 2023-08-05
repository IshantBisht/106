import cv2;
img=cv2.imread("4f.jpg")
grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
facecascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
faces=facecascade.detectMultiScale(grey,1.1,5)
for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    roi=img[y:y+h,x:x+w]
    cv2.imwrite("multiFace.jpg",roi)
cv2.imshow("img",img)
cv2.waitKey(0)