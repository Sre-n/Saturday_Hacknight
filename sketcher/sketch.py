import cv2
def sketch(image):
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    blur_gray = cv2.GaussianBlur(gray,(5,5),900)
    edges = cv2.Canny(blur_gray,45,90)
    ret,thre = cv2.threshold(edges,70,255,cv2.THRESH_BINARY_INV)
    return thre