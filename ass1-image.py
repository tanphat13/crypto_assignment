import cv2
import random
import json
	# def bin_to_str(bin)


file_path = './'
file_name = 'image1.png'
raw_file = file_path + '/' + file_name
text = 'NguyenHoangLong-NguyenNgocAnhTuan-CuTanPhat'
number_student = text.count('-', 0, -1)
cipher = ' '.join(format(ord(x), '') for x in text)
cipher = cipher.split(" ")
img = cv2.imread(raw_file)
height, width, channel = img.shape
output = img.copy()
print(cipher)
hstep = random.randrange(1, int(width/len(cipher)))
vstep = random.randrange(1, int(height/number_student))
data = {'horizontal_step': hstep, 'vertical_step': vstep, 'end_origin': []}
key = open('./key.txt', "w")

print("Horizontal Step: " + str(hstep))
print("Vertical Step: " + str(vstep))
count = 0
j = 0
for i in range (0, height):
    if count == len(cipher):
	    data['end_origin'].append(j*vstep)
	    data['end_origin'].append(i*hstep)
	    break
    output[j*vstep][i*hstep][0] = cipher[i] 
    if cipher[i] == format(ord('-'), ''):
	    j += 1
    count += 1
cv2.imwrite("img-out.png", output)
json.dump(data, key)

###---Int to ASCII character
# for i in range (0, len(cipher)):
#     print(chr(int(cipher[i])))
