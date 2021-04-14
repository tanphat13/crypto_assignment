import cv2
from PIL import Image
import numpy as np
import math
import random
import json
import crypto.Cipher._XOR as xor
import sys
import warnings

if not sys.warnoptions:
	warnings.simplefilter("ignore")

sym_key = str(random.randrange(0, 3))
info = sym_key
xor_algo =  xor.new(sym_key)
file_path = '.'
file_name = 'image.png'
raw_file = file_path + '/' + file_name
text = 'NguyenHoangLong-NguyenNgocAnhTuan-CuTanPhat'
cipher = ' '.join(format(ord(x), 'b') for x in text)
cipher = cipher.split(" ")
for index in range(len(cipher)):
	if len(cipher[index]) < 7:
		cipher[index] = cipher[index].zfill(7)
cipher = ''.join(cipher[x] for x in range(len(cipher)))
img = Image.open(raw_file)
icc_profile = img.info.get("icc_profile")
exif = img.info.get("exif")
img.save('image.png', mode='PNG', icc_profile=icc_profile, exif=exif)
output = np.asarray(Image.open(raw_file)).astype(np.uint8)
height, width, channel = output.shape
number_lines = 1
if len(cipher) > width:
	number_lines = math.ceil(len(cipher)/width)
bits_per_line = math.ceil(len(cipher)/number_lines)
hstep = math.floor(width/bits_per_line)
vstep = int(random.randrange(1, int(height/number_lines)))
info += "&" + xor_algo.encrypt(str(number_lines)).decode() + "&" + xor_algo.encrypt(str(vstep)).decode() + "&" + xor_algo.encrypt(str(hstep)).decode() + "&" + xor_algo.encrypt(str(bits_per_line)).decode() + "&" + xor_algo.encrypt(str(len(cipher))).decode()

j = 0
count = 0
i = 0
while j < number_lines:
	i = 0
	info += ","
	while i < bits_per_line:
		info +=  xor_algo.encrypt(str(output[j*vstep][i*hstep][0])).decode()
		current= (output[j*vstep][i*hstep][0])
		if output[j*vstep][i*hstep][0] == 255:
			output[j*vstep][i*hstep][0] -= int(cipher[count])
		else:
			output[j*vstep][i*hstep][0] += int(cipher[count])
		count += 1
		i += 1
		if i == bits_per_line  or count == len(cipher):
			break
		info += "&"
	j += 1

output  = Image.fromarray(np.uint8(output))
output.save('img-out.png', mode='PNG', icc_profile=icc_profile, exif=exif)
key = open('./key.txt', "w")
key.write(info)