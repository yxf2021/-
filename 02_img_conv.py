# 图像卷积示例
from scipy import signal
from scipy import misc
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as sn

im = misc.imread('lily.png', flatten=True)

flt = np.array([[-1, 0, 1],
                [-2, 0, 2],
                [-1, 0, 1]])

flt2 = np.array([[1, 2, 1],
                 [0, 0, 0],
                 [-1, -2, -2]])

grad = signal.convolve2d(im,
                         flt,
                         boundary='symm',
                         mode='same').astype('int32')

grad2 = signal.convolve2d(im,
                          flt2,
                          boundary='symm',
                          mode='same').astype('int32')

plt.figure('Conv2D')
plt.subplot(131)
plt.imshow(im, cmap='gray')
plt.xticks([])
plt.yticks([])

plt.subplot(132)
plt.imshow(grad, cmap='gray')
plt.xticks([])
plt.yticks([])

plt.subplot(133)
plt.imshow(grad2, cmap='gray')
plt.xticks([])
plt.yticks([])

plt.show()
