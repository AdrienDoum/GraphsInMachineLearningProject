''' Main file'''

import numpy as np
from inpaint import *

if __name__ == '__main__':
	im_path = './Images/Paris.jpg'
	mask_path = './Images/ParisMask.jpg'

	dst = fast_march(im_path,mask_path)
	im = cv2.imread(im_path)

	diff = im-dst
	cv2.imshow('im',im)
	cv2.imshow('dst',dst)
	cv2.imshow('diff',diff)
	cv2.waitKey(0)
	cv2.destroyAllWindows()