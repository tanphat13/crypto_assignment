import numpy
import cv2
import binascii
import random
# def bin_to_str(bin)


file_path = '/home/long/crypto'
file_name = 'image.png'
raw_file = file_path + '/' + file_name
text = 'NguyenHoangLong-NguyenNgocAnhTuan-CuTanPhat'
cipher = ' '.join(format(ord(x), '') for x in text)
cipher = cipher.split(" ")
img = cv2.imread(raw_file)
height, width, channel = img.shape
output = img.copy()
print(cipher)
step = random.randrange(0, int(width/len(cipher)))
step = int(width/len(cipher))
print("Step: " + str(step))
count = 0
for i in range (0, height):
    if count == len(cipher):
        break
    output[0][i*step][0] = cipher[i]
    count += 1
    print(i*step)
cv2.imwrite("img-out.png", output)

print(output)
###---Int to ASCII character
# for i in range (0, len(cipher)):
#     print(chr(int(cipher[i])))
