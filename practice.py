from glob import glob
import os
import cv2

def convert_png_to_jpg_image(path):
	print('Started converting')
	for root, dirs, files in os.walk(path):
		for i, file_ in enumerate(files):
			file_path = os.path.join(root, file_)
			img = cv2.imread(file_path)
			cv2.imwrite(file_path[:-3] + 'jpg', img)
			os.remove(file_path)
	print('Completed converting')

if __name__ == '__main__':
	path = input("Please enter the folder path: \n")
	convert_png_to_jpg_image(path)
