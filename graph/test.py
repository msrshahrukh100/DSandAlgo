import cv2
img = cv2.imread("khabib.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
inverted_img = 255 - gray_img
blurred_img = cv2.GaussianBlur(inverted_img, (21, 21), 0)
invered_blur_img = 255 - blurred_img
pencil_sketch_img = cv2.divide(gray_img, invered_blur_img, scale=256.0)
cv2.imwrite("khabib_sketch.jpg", pencil_sketch_img)