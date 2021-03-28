import cv2
import json

key_file = open('key.txt', 'r')
data = json.load(key_file)

img = cv2.imread('./img-out.png')
height, width, channel = img.shape

vstep = data['vertical_step']
hstep = data['horizontal_step']
cipher = []
j = 0
for i in range(0, height):
	if j*vstep == data['end_origin'][0] and i*hstep == data['end_origin'][1]:
		break
	cipher.append(img[j*vstep][i*hstep][0])
	if img[j*vstep][i*hstep][0] == int(ord('-')):
		j += 1
print(''.join(chr(x) for x in cipher))