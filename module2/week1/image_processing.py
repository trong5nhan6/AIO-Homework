import matplotlib.image as mpimg
import numpy as np


# Hàm chuyển đổi từ RGB sang Grayscale sử dụng phương pháp Lightness
def rgb2gray_lightness(rgb):
    max_rgb = np.max(rgb[..., :3], axis=2)
    min_rgb = np.min(rgb[..., :3], axis=2)
    return (max_rgb + min_rgb)/2


# Hàm chuyển đổi từ RGB sang Grayscale sử dụng phương pháp Average
def rgb2gray_average(rgb):
    return np.mean(rgb, axis=2)


# Hàm chuyển đổi từ RGB sang Grayscale sử dụng phương pháp Luminosity
def rgb2gray_luminosity(rgb):
    return np.dot(rgb[..., :3], [0.21, 0.72, 0.07])


img = mpimg.imread('D:\VS_code\AIO\AIO-Homework\module2\week1\dog.jpeg')
gray_img_01 = rgb2gray_lightness(img)
print(gray_img_01[0, 0])

gray_img_02 = rgb2gray_average(img)
print(gray_img_02[0, 0])

gray_img_03 = rgb2gray_luminosity(img)
print(gray_img_03[0, 0])
