import cv2
from PIL import Image
import numpy as np
import math
import json
from crypto.Cipher import _XOR as xor
import sys
import warnings

if not sys.warnoptions:
	warnings.simplefilter("ignore")

key_file = open('key.txt', 'r')
data = key_file.read()
image_info, initial_value_as_str = data.split(",", 1)
initial_value_as_str = initial_value_as_str.split(",")
sym_key, lines, vstep, hstep, bits_per_line, message_len= image_info.split("&", 5)
xor_algo = xor.new(sym_key)

def decrypt_key(cipher):
	value = xor_algo.decrypt(cipher).decode()
	return int(value)

# img = cv2.imread('./img-out.png')
img = np.asarray(Image.open('./img-out.png')).astype(np.uint8)
number_lines = decrypt_key(lines.encode())
vstep = decrypt_key(vstep.encode())
hstep = decrypt_key(hstep.encode())
bits_per_line =  decrypt_key(bits_per_line.encode())
message_len = decrypt_key(message_len.encode())

cipher = []
count = 0
for j in range(number_lines):
	initial_value = initial_value_as_str[j].split('&')
	for i in range(len(initial_value)):
		#print("%d %d" % (count, int(abs(img[j*vstep][i*hstep][0] - decrypt_key(initial_value[i])))))
		cipher.append(str(int(abs(img[j*vstep][i*hstep][0] - decrypt_key(initial_value[i])))))
		count += 1
array = [cipher[i:(i+7)] for i in range(0, len(cipher), 7)]
raw_bin = [''.join(array[i]) for i in range(len(array))]
raw_code = [int(raw_bin[i], 2) for i in range(len(raw_bin))]
print(''.join(chr(x) for x in raw_code))