import cv2

grey_img = cv2.imread('images/test1.jpg', cv2.IMREAD_GRAYSCALE)

status = cv2.imwrite('images/test1.jpg', grey_img)

print("Image written to file-system : ", status)