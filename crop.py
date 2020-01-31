import cv2
import os
import glob
# import pdb
from time import time
from urllib3.connectionpool import xrange


def crop_image(input_path, output_path, crop_height, crop_width):
	sorted_files = sorted(glob.glob(input_path))
	batch_size = 40
	for level, i in enumerate(xrange(0, len(sorted_files), batch_size)): # defining level 0-30 (31 levels);
		# pdb.set_trace()
		batch_files = sorted_files[i:i + batch_size]

		level_folder = output_path + "LEVEL_" + str(level)  # LEVEL_0
		if os.path.exists(level_folder):
			pass
		else:
			os.mkdir(level_folder)

		folder_level = 0
		for file in batch_files:     # Iterating batch of files = 41
			image_folder = output_path + "LEVEL_" + str(level) + "/" + str(level) + "_" + str(folder_level) # LEVEL_0/0_0/
			if os.path.exists(image_folder):
				pass
			else:
				os.mkdir(image_folder)
			image = cv2.imread(file)
			image_copy = image
			original_height, original_width, depth = image.shape
			i = 0
			for row in range(0, original_height, crop_height):
				j = 0
				for col in range(0, original_width, crop_width):
					cropped_image = image[row:row + crop_height, col:col + crop_width]
					image_name = "LEVEL_" + str(level) + "_R_" + str(i) + "_C_" + str(j) + ".jpg" # LEVEL_0/0_0/LEVEL_0_R_0_C_0.jpg
					cv2.imwrite(os.path.join(image_folder, str(image_name)), cropped_image)
					image = image_copy
					j = j + 1
				i = i + 1
			folder_level = folder_level + 1

if __name__ == "__main__":
	input_path = "/home/scanup01/Downloads/WSI_41x30/WSI/*.jpg"
	output_path = "/home/scanup01/Downloads/test/"
	crop_height = crop_width = 320

	# print("Enter Input Path: \n")
	# print("Ex: '/home/scanup01/Downloads/tt1/*.jpg'")
	# input_path = input()
	# print("Enter Output Path: \n")
	# print("Ex: '/home/scanup01/Downloads/tt1/'")
	# output_path = input()
	# print("Enter CropWidth: \n")
	# print("Ex: 320 ")
	# crop_width = input()
	# print("Enter CropHeight \n")
	# print("Ex: 320 ")
	# crop_height = input()


	input_path = input_path
	output_path = output_path
	crop_height = crop_height
	crop_width = crop_width

	ts = time()

	print('Started')
	print('--------------------------------------------------------------------')

	crop_image(input_path, output_path, crop_height, crop_width)

	print('Completed')
	print('--------------------------------------------------------------------')
	print("Took %s seconds", + time() - ts)
