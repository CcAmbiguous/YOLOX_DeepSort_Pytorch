from detector import Detector
import cv2
detector = Detector() # instantiate Detector

img = cv2.imread('object/p1.jpg') 	# load image
result = detector.detect(img) 	# detect targets

img_visual = result['visual'] 	 # visualized image
cv2.imshow('detect', img_visual) # imshow
k = cv2.waitKey(0)
## k = cv2.waitKey(0) & 0xFF  # 64位机器
if k == 27:         # 按下esc时，退出
    cv2.destroyAllWindows()
elif k == ord('s'): # 按下s键时保存并退出
    cv2.imwrite('result/out5.jpg',img_visual)
    cv2.destroyAllWindows()