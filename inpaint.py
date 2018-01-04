''' This file contains inpainting algorithms '''

import numpy as np
import cv2
import os
from skimage import data
from skimage.restoration import inpaint
from skimage import io


'''first inpainting algos based on the paper “An Image Inpainting Technique 
Based on the Fast Marching Method” by Alexandru Telea in 2004'''

def fast_march(im_path, mask_path):
	img = cv2.imread(im_file)
	mask = cv2.imread(mask_file)
	dst = cv2.inpaint(img,mask,3,cv2.INPAINT_TELEA)
	return dst

'''Second algorithm is based on the paper “Navier-Stokes, Fluid Dynamics, 
and Image and Video Inpainting” by Bertalmio, Marcelo, Andrea L. Bertozzi, 
and Guillermo Sapiro in 2001. '''
def fluid_dynamic(im_path, mask_path):
	img = cv2.imread(im_file)
	mask = cv2.imread(mask_file)
	dst = cv2.inpaint(img,mask,3,cv2.INPAINT_NS)
	return dst

def biharmonic_eq(im_path,mask_path):
	im = io.imread(im_path)
	mask = io.imread(mask_path)
	dst = inpaint.inpaint_biharmonic(image_defect, mask,
                                          multichannel=True)
	return dst