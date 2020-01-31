import os
# import pdb

def rename_files(input_path, output_path):
	files = os.listdir(input_path)
	for index, file in enumerate(files):
		# pdb.set_trace()
		number = file.split('_')[3]
		os.rename(os.path.join(input_path, file), os.path.join(output_path, ''.join([str(number), '.jpg'])))

if __name__ == '__main__':
	input_path = "/home/scanup01/Downloads/WSI_41x30/WSI/"
	output_path = "/home/scanup01/Downloads/test/"

	# print("Enter Input Path: \n")
	# print("Ex: '/home/scanup01/Downloads/tt1/*.jpg'")
	# input_path = input()
	# print("Enter Output Path: \n")
	# print("Ex: '/home/scanup01/Downloads/tt1/'")
	# output_path = input()

	print("Started")
	rename_files(input_path, output_path)
	print("Completed")
