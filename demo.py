''' Main file'''

import numpy as np
from inpaint.py import *

if __name__ == '__main__':
	im_path = './data/im1.jpg'
	mask_path = './data/mask1.jpg'

	dst = fast_march(im_path,mask_path)

	cv2.imshow('dst',dst)
	cv2.waitKey(0)
	cv2.destroyAllWindows()