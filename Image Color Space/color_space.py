import cv2
from PIL import Image, ImageStat
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D
from matplotlib import colors


colex_img = cv2.imread("A.jpg")
small_bgr = cv2.resize(colex_img, (30,30)) # resize to small 30*30


small_HSV = cv2.cvtColor(small_bgr, cv2.COLOR_BGR2HSV)
small_YCRCB = cv2.cvtColor(small_bgr, cv2.COLOR_BGR2YCrCb)
B, G ,R = cv2.split(small_bgr)
h, s, v = cv2.split(small_HSV)
Y,Cr,Cb = cv2.split(small_YCRCB)




# RGB color space
rgb_fig = plt.figure()
ax_rgb = Axes3D(rgb_fig)

for i in range(30):
    for j in range(30):
        ax_rgb.scatter(R[i][j], G[i][j], B[i][j], c=[R[i][j]/255., G[i][j]/255., B[i][j]/255.], marker='.' )
ax_rgb.grid(False)
ax_rgb.set_xlabel('R')
ax_rgb.set_ylabel('G')
ax_rgb.set_zlabel('B')
ax_rgb.set_title('RGB color space')
plt.savefig('RGB_SPACE.jpg')




# HSV color space
hsv_fig = plt.figure()
ax_hsv = Axes3D(hsv_fig)

for i in range(30):
    for j in range(30):
        ax_hsv.scatter(h[i][j], s[i][j], v[i][j], c=[R[i][j]/255., G[i][j]/255., B[i][j]/255.], marker='.')
ax_hsv.grid(False)
ax_hsv.set_xlabel('H')
ax_hsv.set_ylabel('S')
ax_hsv.set_zlabel('V')
ax_hsv.set_title('HSV color space')
plt.savefig('HSV_SPACE.jpg')




# YCbCr color space
ycbcr_fig = plt.figure()
ax_Ycbcr = Axes3D(ycbcr_fig)

for i in range(30):
    for j in range(30):
        ax_Ycbcr.scatter(Cr[i][j], Cb[i][j], Y[i][j], c=[R[i][j]/255., G[i][j]/255., B[i][j]/255.], marker='.')
ax_Ycbcr.grid(False)
ax_Ycbcr.set_xlabel('Cr')
ax_Ycbcr.set_ylabel('Cb')
ax_Ycbcr.set_zlabel('Y')
ax_Ycbcr.set_title('YCbCr color space')
plt.savefig('YCBCR_SPACE.jpg')
