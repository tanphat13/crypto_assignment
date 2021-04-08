import cv2
from PIL import Image
import numpy as np
import math
import random
import json

file_path = './'
file_name = 'image.png'
raw_file = file_path + '/' + file_name
text = 'NguyenHoangLong-NguyenNgocAnhTuan-CuTanPhat'
number_student = text.count('-', 0, -1)
cipher = ' '.join(format(ord(x), 'b') for x in text)
cipher = cipher.split(" ")
for index in range(len(cipher)):
	if len(cipher[index]) < 7:
		cipher[index] = cipher[index].zfill(7)
cipher = ''.join(cipher[x] for x in range(len(cipher)))
img = Image.open(raw_file)
icc_profile = img.info.get("icc_profile")
exif = img.info.get("exif")
img_as_array = np.asarray(img).astype(np.uint8)
height, width, channel = img_as_array.shape
output = img_as_array.copy()
number_lines = 1
if len(cipher) > width:
	number_lines = math.ceil(len(cipher)/width)
bits_per_line = math.ceil(len(cipher)/number_lines)
hstep = math.floor(width/bits_per_line)
vstep = int(random.randrange(1, int(height/number_lines)))
end_origin = []
initial_value = [[] for i in range(number_lines)]
j = 0
i = 0
count = 0
while j < number_lines:
	i = 0
	while i < bits_per_line:
		if count == len(cipher):
			break
		initial_value[j].append(int(output[j*vstep][i*hstep][0]))
		if output[j*vstep][i*hstep][0] + math.pow(2, int(cipher[i])) > 255:
			output[j*vstep][i*hstep][0] -= math.pow(2, int(cipher[i]))
		else:
			output[j*vstep][i*hstep][0] += math.pow(2, int(cipher[i]))
		count += 1
		i += 1
	j += 1

output  = Image.fromarray(np.uint8(output))

output = output.save('img-out.png', mode='PNG', icc_profile=icc_profile, exif=exif)
output = Image.open('img-out.jpeg')
end_origin.append(int((j-1)*vstep))
end_origin.append(int(i*hstep))

key = open('./key.txt', "w")
data = {'lines': number_lines, 'vstep': vstep, 'hstep': hstep, 'end_origin': end_origin,'initial_value': initial_value}
json.dump(data, key, indent = 4)

###---Int to ASCII character
# for i in range (0, len(cipher)):
#     print(chr(int(cipher[i])))
