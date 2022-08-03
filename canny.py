import cv2
import os

trainA_path = "/data2/pytorch-CycleGAN-and-pix2pix/datasets/maps/trainA"
trainB_path = "/data2/pytorch-CycleGAN-and-pix2pix/datasets/maps/trainB"

# for i in range(51):
# imgA_path = os.path.join(trainB_path,"{}.png".format(i))

imgA_path = "/data2/pytorch-CycleGAN-and-pix2pix/checkpoints/maps_cyclegan/web/images/epoch013_real_A.png"
image = cv2.imread(imgA_path)
print(image.shape)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
canny = cv2.Canny(blurred, 30, 150)


imgB_path = "/data2/pytorch-CycleGAN-and-pix2pix/checkpoints/maps_cyclegan/web/images/epoch013_fake_B.png"
image = cv2.imread(imgB_path)
print(image.shape)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
canny2 = cv2.Canny(blurred, 30, 150)
# edge_pix_num = 0
# for row in canny:
# 	for column in row:
# 		if column==255:
# 			# print(column)
# 			edge_pix_num+=1

# print(edge_pix_num)
cv2.imshow('Input', canny)
cv2.imshow('Result', canny2)
cv2.waitKey(0)
