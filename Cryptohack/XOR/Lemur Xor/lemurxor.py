import cv2

image1 = cv2.imread('flag.png')
image2 = cv2.imread('lemur.png')

dest = cv2.bitwise_xor(image1, image2)
cv2.imshow("xored",dest)
cv2.waitKey(0)
cv2.destroyAllWindows()

