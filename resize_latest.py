import cv2
import glob
import os
from time import time
from urllib3.connectionpool import xrange

def resize_images(input_path, output_path, number_of_columns):
	sorted_files = sorted(glob.glob(input_path))
	batch_size = number_of_columns
	row = 0
	for i in xrange(0, len(sorted_files), batch_size):
		batch_files = sorted_files[i:i + batch_size]
		col = 0
		t = time()
		for file in batch_files:
			original_image = cv2.imread(file, 1)
			height, width, depth = original_image.shape
			for j in range(6):
				level = output_path +  "LEVEL_" + str(j)
				if os.path.exists(level):
					pass
				else:
					os.mkdir(level)
				file_name = "LEVEL_" + str(j) + "_R_" + str(row) + "_C_" + str(col) + ".jpg"
				resized = cv2.resize(original_image, (width, height))
				cv2.imwrite(os.path.join(level, str(file_name)), resized)
				original_image = resized
				width = int(width/2)
				height = int(height/2)
			col = col + 1
		row = row + 1
		print(time() - t)


if __name__ == "__main__":
	input_path = "/home/scanup01/Downloads/test/*.jpg"
	output_path = "/home/scanup01/Downloads/test/"
	number_of_columns = 41

	# print("Enter Input Path: \n")
	# print("Ex: '/home/scanup01/Downloads/tt1/*.jpg'")
	# input_path = input()
	# print("Enter Output Path: \n")
	# print("Ex: '/home/scanup01/Downloads/tt1/'")
	# output_path = input()
	# print("Enter Number of columns: \n")
	# print("Ex: 41")
	# number_of_columns = input()

	input_path = input_path
	output_path = output_path
	number_of_columns = number_of_columns

	ts = time()
	print('Started')
	resize_images(input_path, output_path, number_of_columns)
	print('Completed')
	print("Took %s seconds", + time() - ts)
