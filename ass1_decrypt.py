import cv2
import json

key_file = open('key.txt', 'r')
data = json.load(key_file)

img = cv2.imread('./img-out.png')
height, width, channel = img.shape

number_lines = data['lines']
vstep = data['vstep']
hstep = data['hstep']
end_origin = data['end_origin']
initial_value = data['initial_value']

cipher = []
j = 0

while j < number_lines:
	if j*vstep != end_origin[0] and i*hstep != end_origin[1]:
		break
	for i in range(len(initial_value[j])):
		cipher.append(str(int(abs(img[j*vstep][i*hstep][0] - initial_value[j][i]) / 2)))
	j += 1

array = [cipher[i:(i+7)] for i in range(0, len(cipher), 7)]
raw_bin = [''.join(array[i]) for i in range(len(array))]
raw_code = [int(raw_bin[i], 2) for i in range(len(raw_bin))]
print(''.join(chr(x) for x in raw_code))
