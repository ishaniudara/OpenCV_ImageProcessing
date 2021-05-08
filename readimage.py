import cv2
image=cv2.imread("lena.jpg",1)
image=cv2.line(image,(0,0),(255,255),(0,0,255),5)
image=cv2.rectangle(image,(384,0),(510,128),(0,0,255),5)
image=cv2.circle(image,(447,63),63,(0,0,255),5)
font=cv2.FONT_HERSHEY_SCRIPT_COMPLEX
image=cv2.putText(image,"Ishani",(0,0),font,(0,0,255),5)
print(image)
cv2.imshow("hello",image)
cv2.waitKey(5000)
cv2.imwrite("lena.png",image)
