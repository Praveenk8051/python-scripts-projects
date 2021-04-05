
import cv2
from matplotlib import pyplot as plt

path = r'./image2.png'
img = cv2.imread(path)
blurred = cv2.GaussianBlur(img, (30, 30), 0)
blurred = cv2.pyrMeanShiftFiltering(blurred, 13, 13)
gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
ret, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
contours, _ = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img, contours, 0, (0, 0, 255), 60)
print(len(contours))

plt.subplot(121), plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(blurred, cmap = 'gray')
plt.title('Contour Image'), plt.xticks([]), plt.yticks([])

plt.show()

path = r'./image1.png'
img = cv2.imread(path)
img = cv2.GaussianBlur(img, (3, 3), 0)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 100)

plt.subplot(121), plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()

import cv2
from matplotlib import pyplot as plt
import numpy as np
img = cv2.imread(r'IMG_1646.jpeg')

# img = cv2.imread(r'/Users/praveen/Documents/product_images/images/50251491/IMG_0109.jpeg')
blur_img = cv2.GaussianBlur(img, (15, 15), 0)
kernel = np.ones((15, 15), np.uint8)
erosion = cv2.morphologyEx(blur_img, cv2.MORPH_GRADIENT, kernel)
# hsv_image = cv2.cvtColor(erosion, cv2.COLOR_RGB2HSV)
# h, s, v = cv2.split(hsv_image)
def crop_image(img,tol=100):
    # img is 2D image data
    # tol  is tolerance
    mask = img > tol
    return img[np.ix_(mask.any(1),mask.any(0))]

def crop_with_argwhere(image):
    # Mask of non-black pixels (assuming image has a single channel).
    mask = image > 0
    print('here')
    # Coordinates of non-black pixels.
    coords = np.argwhere(mask)

    # Bounding box of non-black pixels.
    x0, y0 = coords.min(axis=0)
    x1, y1 = coords.max(axis=0) + 1   # slices are exclusive at the top

    # Get the contents of the bounding box.
    cropped = image[x0:x1, y0:y1]
    return cropped
def crop_image_only_outside(img,tol=0):
    # img is 2D image data
    # tol  is tolerance
    mask = img>tol
    m,n = img.shape
    mask0,mask1 = mask.any(0),mask.any(1)
    col_start,col_end = mask0.argmax(),n-mask0[::-1].argmax()-1
    row_start,row_end = mask1.argmax(),m-mask1[::-1].argmax()-1
    return img[row_start:row_end,col_start:col_end]
gray = cv2.cvtColor(erosion, cv2.COLOR_BGR2GRAY)
# _,thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
# final_img=thresh
# bbox = cv2.boundingRect(gray)
# x, y, w, h = bbox
# final_img = erosion[y:y+h, x:x+w]
final_img = crop_with_argwhere(gray)
final_img_ = crop_image(final_img, tol=50)
final_img = cv2.merge([final_img_, final_img_, final_img_])
final_img = cv2.GaussianBlur(final_img, (5, 5), 0)
# clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
# v = clahe.apply(v)
# hsv_image = cv2.merge([h, s, v])
# final_img = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2RGB)
plt.imshow(final_img)
plt.xticks([]), plt.yticks([])
plt.show()


# from PIL import ImageEnhance, Image
# img = cv2.imread(r'flip161.jpeg')
# img = Image.open(r'flip161.jpeg')
# img = ImageEnhance.Contrast(img)
# img.show()
# plt.imshow(img)
# plt.xticks([]), plt.yticks([])
# plt.show()
